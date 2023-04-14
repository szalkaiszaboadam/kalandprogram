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

bannerKep = r'''
                                                      __/_
                                                       /|___            
                                                    .'T'. - -'.        
                                                 .'/|||||\'. - -'.             
                                               .'/|||||||||\'. - -'.                     
                                             .'/|||||___|||||\'. - -'.     .    
                                            //|||||||||||||||||\\ - - \   /|\          
                                           //|||||||||||||||||||\\ - - \ //|\\            
                                          //|||||||||||||||||||||\\_____\//|\\
                    ____________::___      ||||||||||/-\||||||||| ||||| ///|\\\
     _        _    /_)_)_)_)_)_)_)_)/\     ||||| \\       // |||| ||||| ///|\\\
    ( )_    _( )  /_)_)_)_)_)_)_)_)/ _\    |||||   \\   //   |||| |||||////|\\\\
   (  )_)  (  )_)  | :__:    :__: |: |     |||||     \x\     |||| |||||////|\\\\
  (_(_ (_)(_) _)_) |  _         _ | :|     |||||   //   \\   |||| ||||/////|\\\\\
____)\_(____)_/(___|_'_'o8|"|8o'_'|:_o8o._.o8%8o_//_______\\_||||.o88o8&8o)/(88o.____
'''
#print("") 
# bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "slant") # , font = "slant"
# bannerKep = pyfiglet.figlet_format("Lost", font = "5lineoblique" )
#print(colored(bannerKep, 'light_grey')) #light_grey
print(bannerKep)
print(colored("| ", 'green') + "Nagy Gábor és Szalkai-Szabó Ádám által készített kalandprogram Python nyelveben" + colored(" |", 'green'))
print("")
write(colored("Üdvözöllek a farmon.\ndfgdsf", 'red',  attrs=['bold']))
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


nev = ""
penz = ""

 

if kezdoValasztas == "B":
    print(colored("\nJelenleg elmentett karakterek:", 'yellow'))

    mentsekOssz = []
    mentettNevek = ''

    
    if os.stat("mentesek.txt").st_size == 0:
        print("\n Nincs elmentett karakter.")
        
        ujatekValasztas = ''

        while True:
            ujatekValasztas = input("\nSzeretnél új játékot kezdeni?\n" + "---> " + colored("[I/N]", 'magenta') + ": ")
        
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
                        #"penz": sor_darab[1],
                    }
                    mentsekOssz.append(adat)

                mentesekTxt.close()

                for i in range(len(mentsekOssz)):
                    mentettNevek += mentsekOssz[i]["nev"] + "/"

                while True:
                    nevTemp = input(colored("\nMilyen nevet szeretnél magadnak adni? ", 'red') + colored("(", 'red', attrs=['bold']) + colored("Ezt később már nem változtathatja meg, mert a karaktered ezen a néven lesz elmentve", 'red') + colored(")", 'red', attrs=['bold']) + "\n--->: ")
                    
                    if nevTemp != "" and nevTemp != "/" and nevTemp not in mentettNevek:
                        nev += nevTemp
                        
                        txt = open("mentesek.txt", "a+", encoding="utf8")
                        print(f"{nev};0;0;0;0;0;0", file=txt)
                        txt.close()

                        write(colored("\n" + nev + "!", 'green', attrs=['bold'])); time.sleep(1); write(colored(" Örülök, hogy megismerhetlek! ", 'green') + colored("(", attrs=['bold']) + "Reméljük, hogy hamarosan semmi rossz nem történik ott." + colored(")", attrs=['bold'])); 


                        time.sleep(2)

                        non = input("\n Készen állsz?" + colored(" [NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

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
                "penz": sor_darab[1],
            }
            mentsekOssz.append(adat)

        mentesekTxt.close()

        for i in range(len(mentsekOssz)):
            print(" " + mentsekOssz[i]["nev"])
            mentettNevek += mentsekOssz[i]["nev"] + "/"

        mentesValasztas = ''
        while True:
            mentesValasztas = input("---> " + colored(f"[{mentettNevek}]", 'magenta') + ": ")
            
            if mentesValasztas != "/" and mentesValasztas != "" and mentesValasztas in mentettNevek:
                for i in range(len(mentsekOssz)):
                    if mentesValasztas == mentsekOssz[i]["nev"]:
                        nev = mentsekOssz[i]["nev"]
                        penz = mentsekOssz[i]["penz"]

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
            #"penz": sor_darab[1],
        }
        mentsekOssz.append(adat)

    mentesekTxt.close()

    for i in range(len(mentsekOssz)):
        mentettNevek += mentsekOssz[i]["nev"] + "/"

    while True:
        nevTemp = input(colored("\nMilyen nevet szeretnél magadnak adni? ", 'red') + colored("(", 'red', attrs=['bold']) + colored("Ezt később már nem változtathatja meg, mert a karaktered ezen a néven lesz elmentve", 'red') + colored(")", 'red', attrs=['bold']) + "\n--->: ")
        
        if nevTemp != "" and nevTemp != "/" and nevTemp not in mentettNevek:
            nev += nevTemp
            
            txt = open("mentesek.txt", "a+", encoding="utf8")
            print(f"{nev};0;0;0;0;0;0", file=txt)
            txt.close()

            write(colored("\n" + nev + "!", 'green', attrs=['bold'])); time.sleep(1); write(colored(" Örülök, hogy megismerhetlek! ", 'green') + colored("(", attrs=['bold']) + "Reméljük, hogy hamarosan semmi rossz nem történik ott." + colored(")", attrs=['bold'])); 


            time.sleep(2)

            non = input("\n Készen állsz?" + colored(" [NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

            break
        else:
            print(colored("Kérjük érvényes nevet adj a karakterednek", 'red'))














'''
print("Before the sleep statement")
time.sleep(1)
print("After the sleep statement")
'''

'''
outc = ['good', 'not', 'maybe']
outc = random.choice(outc)
emon = random.randint(100,500)
# emon = round(emon)

print(outc)
print(emon)
'''


# Függvények létrehozása majd!!!! https://sulipy.hu/eljarasok_fuggvenyek/fuggveny?tab=peldak