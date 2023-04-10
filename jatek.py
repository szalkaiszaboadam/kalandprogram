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



kezdoValasztas = ''

while True:
    kezdoValasztas = input("---> " + colored("[B/Ú]", 'magenta') + ": ")
    
    if kezdoValasztas == "B":
        break
    if kezdoValasztas == "Ú":
        break
    else:
        print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))



if kezdoValasztas == "B":
    print(colored("\nJelenleg elmentett játékok:", 'yellow'))

    mentsekOssz = []

    mentesekTxt = open("mentesek.txt",  "r", encoding="utf8")
    sorok = mentesekTxt.readlines()[1:]

    for i in sorok:
        sor_darab = i.strip().split(";")
        adat = {
            "nev": sor_darab[0],
            "penz": sor_darab[1],
        }
        mentsekOssz.append(adat)

    mentesekTxt.close()

    for i in range(len(mentsekOssz)):
        if os.stat("mentesek.txt").st_size == 0:
            print("\n There are no saved characters. Do [red]CTRL + C[/red] to [blue]quit[/blue] and [yellow]start the game again.[/yellow]")

    

        else:
            print("\n " + mentsekOssz[i]["nev"])

            mentesValasztas = ''

            while True:
                mentesValasztas = input("---> " + colored("[B/Ú]", 'magenta') + ": ")
                
                if mentesValasztas == "B":
                    break
                if kezdoValasztas == "Ú":
                    break
                else:
                    print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))


    









#print(mentsekOssz)

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