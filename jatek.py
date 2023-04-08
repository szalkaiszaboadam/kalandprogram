import pyfiglet
import time
import random
import sys
from time import sleep
from termcolor import colored

def write(write):
    for i in write:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
    next = input()

'''from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console'''


print("") 

bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "slant") # , font = "slant"
# bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "banner3-D" )
print(colored(bannerKep, 'light_grey'))
# print(bannerKep)

print("\n") 

print(colored("| ", 'green') + "scientifically accurate, survival text-based adventure\nset in the future where climate change is inevitabl", colored(" |", 'green'))
print(" ")
print(colored("Welcome to Lost Cause.\nWould you like to load a save or start a new game?", 'red',  attrs=['bold']))
print(" ")
print(colored(" [L] ", 'yellow',  attrs=['bold']) + "LOAD")
print(colored(" [N] ", 'yellow',  attrs=['bold']) + "NEW GAME")

elsoinput = input("---> " + colored("[N/L]", 'magenta') + ": ")


print("Before the sleep statement")
time.sleep(1)
print("After the sleep statement")

outc = ['good', 'not', 'maybe']
outc = random.choice(outc)
emon = random.randint(100,500)
# emon = round(emon)

print(outc)
print(emon)

write(colored(" [L]sdfsdfsfsfdsd ", 'yellow',  attrs=['bold']) + "LOsf sf sdfs dfsdfsdfAD")

# Függvények létrehozása majd!!!! https://sulipy.hu/eljarasok_fuggvenyek/fuggveny?tab=peldak