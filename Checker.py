from time import sleep
from sys import argv
from os import system
while True:
	actual = open(f'{argv[0]}', 'r').read()
	sleep(1)
	system('git pull')
	noww = open(f'{argv[0]}', 'r').read()
	if actual != noww:
		system('pkill py* && screen python3.6 Checker.py')
		