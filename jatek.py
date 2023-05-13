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

'''
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
'''

os.system('cls')
time.sleep(1)
#sys.stdout.write("fgdfgdfg")


   

#, 'light_grey',  attrs=['bold']))


#print("") 
bannerKep = pyfiglet.figlet_format("Szoveges kaland")
#print(colored(bannerKep, 'light_grey')) #light_grey
print("\n" + bannerKep)

print("")


print(colored("|  ", 'grey') + "Nagy Gábor és Szalkai-Szabó Ádám által készített szöveges\nkalandprogram ami Python programozási nyelveben írodott" + colored("  |", 'grey'))
print(colored("\nSzeretnél betölteni egy mentést vagy új játékot kezdeni?\n", 'red',  attrs=['bold']))
print(colored(" [B] ", 'yellow',  attrs=['bold']) + "Betöltés")
print(colored(" [Ú] ", 'yellow',  attrs=['bold']) + "Új játék")
print(colored(" [K] ", 'yellow',  attrs=['bold']) + "Kilépés")


kezdoValasztas = ''

while True:
    kezdoValasztas = input("---> " + colored("[B/Ú/K]", 'magenta', attrs=['bold']) + ": ")
    
    if kezdoValasztas == "B":
        break
    if kezdoValasztas == "Ú":
        break
    if kezdoValasztas == "K":
        break
    else:
        print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))


nev = ""
eletero = 0
penz = 0
kard = 0
pajzs = 0
alma = 0
kenyer = 0
gyogyital = 0

if kezdoValasztas == "K":
    time.sleep(1)
    exit()

if kezdoValasztas == "B":
    print(colored("\nJelenleg elmentett karakterek:", 'yellow'))

    mentsekOssz = []
    mentettNevek = ''

    
    if os.stat("mentesek.txt").st_size == 0:
        print("\n Nincs elmentett karakter.")
        
        ujatekValasztas = ''

        while True:
            ujatekValasztas = input("\nSzeretnél új játékot kezdeni?\n" + "---> " + colored("[I/N]", 'magenta', attrs=['bold']) + ": ")
        
            if ujatekValasztas == "I":
                mentsekOssz = []
                nevTemp = ""
                mentettNevek = ''

                mentesekTxt = open("mentesek.txt",  "r", encoding="utf8")
                sorok = mentesekTxt.readlines()#[1:]

                for i in sorok:
                    sor_darab = i.strip().split(";")
                    adat = {
                        "nev": sor_darab[0],
                        "eletero": int(sor_darab[1]),
                        "penz": int(sor_darab[2]),
                        "kard": int(sor_darab[3]),
                        "pajzs": int(sor_darab[4]),
                        "alma": int(sor_darab[5]),
                        "kenyer" : int(sor_darab[6]),
                        "gyogyital" : int(sor_darab[7]),
                    }
                    mentsekOssz.append(adat)

                mentesekTxt.close()

                for i in range(len(mentsekOssz)):
                    mentettNevek += mentsekOssz[i]["nev"] + "/"

                while True:
                    nevTemp = input(colored("\nMilyen nevet szeretnél magadnak adni? ") + colored("(", 'red', attrs=['bold']) + colored("Ezt később már nem lehet megváltoztatni", 'red') + colored(")", 'red', attrs=['bold']) + "\n--->: ")
                    
                    if nevTemp != "" and nevTemp != "/" and nevTemp not in mentettNevek:
                        nev += nevTemp
                        
                        txt = open("mentesek.txt", "a+", encoding="utf8")
                        print(f"{nev};100;0;1;1;0;0;0", file=txt)
                        txt.close()

                        #write(colored("\n" + nev + "!", 'green', attrs=['bold'])); time.sleep(1); write(colored(" Örülök, hogy megismerhetlek! ", 'green') + colored("(", attrs=['bold']) + "Reméljük, hogy hamarosan semmi rossz nem történik ott." + colored(")", attrs=['bold'])); 

                        print(colored("\nLétrehozunk téged...", "green")); time.sleep(2)

                        print("Készen állsz a kalandra?", end='')
                        time.sleep(1)
                        var = input(colored(" [NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

                        os.system('cls')

                        write("\n  Utad legelején egy varázslóval találkozol össze. Látja, hogy nincs felszerelésed\n  ezért megszán egy karddal, egy pajjzsal és néhány jó tanáccsal.")
                        time.sleep(2.7)
                        os.system('cls')


                        break
                        


                    else:
                        print(colored("Kérjük érvényes nevet adj a karakterednek", 'red'))

                break

            if ujatekValasztas == "N":
                exit()
            else:
                print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))


    else:

        mentesekTxt = open("mentesek.txt",  "r", encoding="utf8")
        sorok = mentesekTxt.readlines()#[1:]

        for i in sorok:
            sor_darab = i.strip().split(";")
            adat = {
                "nev": sor_darab[0],
                "eletero": int(sor_darab[1]),
                "penz": int(sor_darab[2]),
                "kard": int(sor_darab[3]),
                "pajzs": int(sor_darab[4]),
                "alma": int(sor_darab[5]),
                "kenyer" : int(sor_darab[6]),
                "gyogyital" : int(sor_darab[7]),
            }
            mentsekOssz.append(adat)

        mentesekTxt.close()

        for i in range(len(mentsekOssz)):
            print(" " + mentsekOssz[i]["nev"])
            mentettNevek += mentsekOssz[i]["nev"] + "/"

        mentesValasztas = ''
        while True:
            mentesValasztas = input("\n---> " + colored(f"[{mentettNevek}]", 'magenta', attrs=['bold']) + ": ")
            
            if mentesValasztas != "/" and mentesValasztas != "" and mentesValasztas in mentettNevek:
                for i in range(len(mentsekOssz)):
                    if mentesValasztas == mentsekOssz[i]["nev"]:
                        nev = mentsekOssz[i]["nev"]
                        eletero = mentsekOssz[i]["eletero"]
                        penz = mentsekOssz[i]["penz"]
                        kard = mentsekOssz[i]["kard"]
                        pajzs = mentsekOssz[i]["pajzs"]
                        alma = mentsekOssz[i]["alma"]
                        kenyer = mentsekOssz[i]["kenyer"]
                        gyogyital = mentsekOssz[i]["gyogyital"]

                os.system('cls') 
                break
            else:
                print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))




if kezdoValasztas == "Ú":

    mentsekOssz = []
    nevTemp = ""
    mentettNevek = ''

    mentesekTxt = open("mentesek.txt",  "r", encoding="utf8")
    sorok = mentesekTxt.readlines()#[1:]

    for i in sorok:
        sor_darab = i.strip().split(";")
        adat = {
            "nev": sor_darab[0],
            "eletero": int(sor_darab[1]),
            "penz": int(sor_darab[2]),
            "kard": int(sor_darab[3]),
            "pajzs": int(sor_darab[4]),
            "alma": int(sor_darab[5]),
            "kenyer" : int(sor_darab[6]),
            "gyogyital" : int(sor_darab[7]),
        }
        mentsekOssz.append(adat)

    mentesekTxt.close()

    for i in range(len(mentsekOssz)):
        mentettNevek += mentsekOssz[i]["nev"] + "/"

    while True:
        nevTemp = input(colored("\nMilyen nevet szeretnél magadnak adni? ") + colored("(", 'red', attrs=['bold']) + colored("Ezt később már nem lehet megváltoztatni", 'red') + colored(")", 'red', attrs=['bold']) + "\n--->: ")
        
        if nevTemp != "" and nevTemp != "/" and nevTemp not in mentettNevek:
            nev += nevTemp

            txt = open("mentesek.txt", "a+", encoding="utf8")
            print(f"{nev};100;0;1;1;0;0;0", file=txt)
            txt.close()


            mentesekTxt = open("mentesek.txt",  "r", encoding="utf8")
            sorok = mentesekTxt.readlines()#[1:]

            for i in sorok:
                sor_darab = i.strip().split(";")
                adat = {
                    "nev": sor_darab[0],
                    "eletero": int(sor_darab[1]),
                    "penz": int(sor_darab[2]),
                    "kard": int(sor_darab[3]),
                    "pajzs": int(sor_darab[4]),
                    "alma": int(sor_darab[5]),
                    "kenyer" : int(sor_darab[6]),
                    "gyogyital" : int(sor_darab[7]),
                }
            mentsekOssz.append(adat)

            mentesekTxt.close()

            for i in range(len(mentsekOssz)):
                if nevTemp == mentsekOssz[i]["nev"]:
                        eletero = mentsekOssz[i]["eletero"]
                        penz = mentsekOssz[i]["penz"]
                        kard = mentsekOssz[i]["kard"]
                        pajzs = mentsekOssz[i]["pajzs"]
                        alma = mentsekOssz[i]["alma"]
                        kenyer = mentsekOssz[i]["kenyer"]
                        gyogyital = mentsekOssz[i]["gyogyital"]

            #write(colored("\n" + nev + "!", 'green', attrs=['bold'])); time.sleep(1); write(colored(" Örülök, hogy megismerhetlek! ", 'green') + colored("(", attrs=['bold']) + "Reméljük, hogy hamarosan semmi rossz nem történik ott." + colored(")", attrs=['bold'])); 

            print(colored("\nLétrehozunk téged...", "green")); time.sleep(2)


            print("Készen állsz a kalandra?", end='')
            time.sleep(1)
            var = input(colored(" [NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

            os.system('cls')

            write("\n  Utad legelején egy varázslóval találkozol össze. Látja, hogy nincs felszerelésed\n  ezért megszán egy karddal, egy pajjzsal és néhány jó tanáccsal.")
            time.sleep(2.7)
            os.system('cls')

            break
        else:
            print(colored("Kérjük érvényes nevet adj a karakterednek", 'red'))