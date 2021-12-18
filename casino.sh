#!/bin/bash

set -euo pipefail

bet_size=40
time=17908
key=KDAOULKtVEwZB

while :
do
	time=$((time+1))
	
	response=$(curl \
		-sS \
		-L \
		-H "Host: l1.larkinor.hu" \
		-H "Referer: http://l1.larkinor.hu/cgi-bin/larkinor" \
		-H "Content-Type: application/x-www-form-urlencoded" \
		-d "oldalTipus=otKaszino&loginname=zokniur&kulcs=${key}&idopont=${time}&Submit=svRulett&par1=0%2C1%2C1&par2=${bet_size}%2C%2C&par3=" \
		http://l1.larkinor.hu/cgi-bin/larkinor)

	#echo "$response"

	if echo "$response" | grep "szesen nyert"; then
		echo "Won"
		echo "W" >> /tmp/larkinor_casino.log
		#bet_size=2
	else
		echo "Lost"
		echo "L" >> /tmp/larkinor_casino.log
		#bet_size=$((bet_size*2))
	fi

	echo "Bet size is ${bet_size}"

	if echo "$response" | grep "nincs ennyi pzed"; then
		exit 1
	fi

	sleep 0.5
done

# szesen nyert
# szesen vesztett
