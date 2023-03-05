import os
import menuSelect as ms
from termcolor import colored

x = os.walk(".\\")
count = 0
for root, dirs, files in x:
	for name in files:
		dirs[:] = [d for d in dirs if d not in ['venv']]
		(base, ext) = os.path.splitext(name)
		if ext in ('.jar', '.bat'):
			count += 1
			fullname = os.path.join(root, name)
			#print(fullname)
			os.remove(fullname)
	break

def server():
	ms.Clear()
	print(colored('Server Jar Menu', 'green'))
	serverMenu = {
		"1": ("Purpur", ms.Purpur),
		"2": ("Paper", ms.Paper),
		"q": ("Exit", SystemExit)
	}

	for sKey in sorted(serverMenu.keys()):
		print(sKey + " -> " + serverMenu[sKey][0])

	sServer = input(colored('> ', 'magenta'))
	serverMenu.get(sServer, [None, ms.Invalid])[1]()

def proxy():
	ms.Clear()
	print(colored('Proxy Jar Menu', 'green'))
	proxyMenu = {
		"1": ("Velocity", ms.Velocity),
		"2": ("Waterfall", ms.Waterfall),
		"3": ("BungeeCord", ms.BungeeCord),
		"q": ("Exit", SystemExit)
	}

	for pKey in sorted(proxyMenu.keys()):
		print(pKey + " -> " + proxyMenu[pKey][0])

	sProxy = input(colored('> ', 'magenta'))
	proxyMenu.get(sProxy, [None, ms.Invalid])[1]()

def menu():
	# ms.Clear()
	print(colored('Main Menu', 'green'))
	mainMenu = {
		"1": ("Server", server),
		"2": ("Proxy", proxy),
		"q": ("Exit", SystemExit)
	}

	for mKey in sorted(mainMenu.keys()):
		print(mKey + " -> " + mainMenu[mKey][0])

	sMenu = input(colored('> ', 'magenta'))
	mainMenu.get(sMenu, [None, ms.Invalid])[1]()

menu()
