import os
import time
from colorama import Fore,Back,Style
from colorama import init,AnsiToWin32
import sys
init(wrap= False)
stream= AnsiToWin32(sys.stderr).stream
def caythong (*mau):
	for item in mau:
		print(item+'\n'.join(
		[''.join(
		[
		(
		'noel'[(x-y) % len('noel')] if x>y and x <-y
		else ' '
		)
		for x in range(-80, 50)
		]
		)
		for y in range(0, -30, -1)
		]
		)
		,file=stream)

		# 1
		print(item +'\n'.join(
		[''.join(
		[
		("noel"[(x-y) %len("noel")]if x>=y and x>0
		else ' '
		)
		for x in range(-73,14)
		]
		)
		for y in range(0,-5,-1)
		]
		)
		,file=stream)
		time.sleep(0.01)
		os.system("cls")
		# 

		print(item+'\n\n\n'.join(
		['         '.join(
		[
		(
		'**'[(x-y) % len('**')] if x!=y
		else ' '
		)
		for x in range(-10, 10)
		]
		)
		for y in range(0, -20, -1)
		]
		)
		,file=stream)
		time.sleep(0.005)
		os.system("cls")
		

while True:
	caythong(Fore.RED,Fore.BLUE,Fore.CYAN,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA)

