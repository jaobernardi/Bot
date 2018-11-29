from time import sleep
from sys import argv
from os import system
while True:
	actual = open(f'{argv[0]}', 'r').read()
	sleep(1)
	system('git pull')
	noww = open(f'{argv[0]}', 'r').read()
	print("yooo")
	if actual == noww:
		print("yup")
	if f'{actual}' != f'{noww}':
		print("yeeeeeee")
		sleep(4)
		system('pkill py* && screen python3.6 Checker.py')
		