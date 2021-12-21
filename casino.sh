#!/bin/bash

set -euo pipefail

bet_size=16
time=19377
key=xBgCQHJ6S5pKG

while :
do
	sleep 0.5
	echo "Bet size is ${bet_size}"

	time=$((time+1))
	
	response=$(curl \
		-sS \
		-L \
		-H "Host: l1.larkinor.hu" \
		-H "Referer: http://l1.larkinor.hu/cgi-bin/larkinor" \
		-H "Content-Type: application/x-www-form-urlencoded" \
		-d "oldalTipus=otKaszino&loginname=zokniur&kulcs=${key}&idopont=${time}&Submit=svRulett&par1=0%2C1%2C1&par2=${bet_size}%2C%2C&par3=" \
		http://l1.larkinor.hu/cgi-bin/larkinor)

	if echo "$response" | grep "szesen nyert"; then
		echo "Won"
		echo "W" >> /tmp/larkinor_casino.log
		bet_size=16
		continue
	fi

	if echo "$response" | grep "szesen vesztett"; then
		echo "Lost"
		echo "L" >> /tmp/larkinor_casino.log
		bet_size=$((bet_size*2))
		continue
	fi

	echo "$response"
done
