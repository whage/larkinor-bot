from neo4j import GraphDatabase

import re


pattern = '(hogy |fiam: )(.+) készíthetõ (\d+) (.+)\, (\d+) (.+) és (\d+) (.+) felhasználásával'
inn_log_file = "/tmp/inn.2.log"


class Recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


class ItemGraphBuilder:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_item(self, message):
        with self.driver.session() as session:
            result = session.write_transaction(self._insert_nodes, message)
            #print(result)

    @staticmethod
    def _insert_nodes(tx, message):
        result = tx.run(message)
        return result.single()


if __name__ == "__main__":
    igb = ItemGraphBuilder("bolt://localhost:7687", "neo4j", "admin")

    with open(inn_log_file) as file:
        for line in file:
            m = re.search(pattern, line)
            if m is not None:
                r = Recipe(m.group(2), [
                    (int(m.group(3)), m.group(4)),
                    (int(m.group(5)), m.group(6)),
                    (int(m.group(7)), m.group(8))
                ])
                print(r.name, r.ingredients)

                igb.add_item('MERGE (i:Item {name: "%s"})' % (r.name))
                igb.add_item('MERGE (i:Item {name: "%s"})' % (r.ingredients[0][1]))
                igb.add_item('MERGE (i:Item {name: "%s"})' % (r.ingredients[1][1]))
                igb.add_item('MERGE (i:Item {name: "%s"})' % (r.ingredients[2][1]))

                igb.add_item('MATCH (i:Item), (j:Item) WHERE i.name = "%s" AND j.name = "%s" MERGE (i)-[r:MadeOf {amount: %d}]->(j)' % (r.name, r.ingredients[0][1], r.ingredients[0][0]))
                igb.add_item('MATCH (i:Item), (j:Item) WHERE i.name = "%s" AND j.name = "%s" MERGE (i)-[r:MadeOf {amount: %d}]->(j)' % (r.name, r.ingredients[1][1], r.ingredients[1][0]))
                igb.add_item('MATCH (i:Item), (j:Item) WHERE i.name = "%s" AND j.name = "%s" MERGE (i)-[r:MadeOf {amount: %d}]->(j)' % (r.name, r.ingredients[2][1], r.ingredients[2][0]))

    igb.close()
