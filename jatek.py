import pyfiglet
import time
import random
import sys
from time import sleep
from termcolor import colored

import os


def write(write):
    for i in write:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
    #next = input()

'''from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console'''


print("") 

bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "slant") # , font = "slant"
# bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "banner3-D" )
print(colored(bannerKep, 'light_grey'))
# print(bannerKep)

print("") 


print(colored("| ", 'green') + "Nagy Gábor és Szalkai-Szabó Ádám által készített kalandprogram Python nyelveben" + colored(" |", 'green'))
print("")
write(colored("Welcome to Lost Cause.\nWould you like to load a save or start a new game?", 'red',  attrs=['bold']))
print("\n")
print(colored(" [B] ", 'yellow',  attrs=['bold']) + "BETÖLTÉS")
print(colored(" [Ú] ", 'yellow',  attrs=['bold']) + "ÚJ JÁTÉK")

elsoinput = ""

while elsoinput == "B" or "Ú":
    elsoinput = input("---> " + colored("[B/Ú]", 'magenta') + ": ")
    '''if elsoinput == "B":
        print("B")
    elif elsoinput == "Ú":
        print("Ú")'''
else:
    clear = lambda: os.system('cls')
    clear()

    print(colored(bannerKep, 'light_grey'))
    print("") 
    print(colored("| ", 'green') + "Nagy Gábor és Szalkai-Szabó Ádám által készített kalandprogram Python nyelveben" + colored(" |", 'green'))
    print("")
    print(colored("Welcome to Lost Cause.\nWould you like to load a save or start a new game?", 'red',  attrs=['bold']))
    print("\n")
    print(colored(" [B] ", 'yellow',  attrs=['bold']) + "BETÖLTÉS")
    print(colored(" [Ú] ", 'yellow',  attrs=['bold']) + "ÚJ JÁTÉK")
    elsoinput = input("---> " + colored("[B/Ú]", 'magenta') + ": ")




























'''
print("Before the sleep statement")
time.sleep(1)
print("After the sleep statement")
'''

outc = ['good', 'not', 'maybe']
outc = random.choice(outc)
emon = random.randint(100,500)
# emon = round(emon)

print(outc)
print(emon)






# Függvények létrehozása majd!!!! https://sulipy.hu/eljarasok_fuggvenyek/fuggveny?tab=peldak