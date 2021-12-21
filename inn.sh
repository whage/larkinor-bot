#!/bin/bash

set -euo pipefail

time=23937
key=tY2ZyXyR43QVC

while :
do
	sleep 0.5

	time=$((time+1))
	
	response=$(curl \
		-sS \
		-L \
		-H "Host: l1.larkinor.hu" \
		-H "Referer: http://l1.larkinor.hu/cgi-bin/larkinor" \
		-H "Content-Type: application/x-www-form-urlencoded" \
		-d "oldalTipus=otKocsma&loginname=zokniur&kulcs=${key}&idopont=${time}&Submit=svFizetBor&par1=&par2=&par3=" \
		http://l1.larkinor.hu/cgi-bin/larkinor)

	echo "$response" | grep -a -i "bort a pult" 2>&1 >> /tmp/inn.log
done