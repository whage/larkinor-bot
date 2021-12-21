import re

pattern = '(hogy |fiam: )(.+) készíthetõ (\d+) (.+)\, (\d+) (.+) és (\d+) (.+) felhasználásával'

inn_log_file = "/tmp/inn.log"

class Recipe():
	def __init__(self, name, ingredients):
		self.name = name
		self.ingredients = ingredients

recipes = []

with open(inn_log_file) as file:
    for line in file:
        m = re.search(pattern, line)
        if m is not None:
        	r = Recipe(m.group(2), [
        		(m.group(3), m.group(4)),
        		(m.group(5), m.group(6)),
        		(m.group(7), m.group(8))
        	])
        	print(r.name, r.ingredients)
        	recipes.append(r)
