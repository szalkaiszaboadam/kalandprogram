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

test = r'''

   .                                                                         ...                     
  @88>                                                                   .xH8%"```"%.                
  %8P                                                                   x888~ xnHhx. ".         u.   
   .                              .                                    X888X 8**8888k `.  ...ue888b  
 .@88u                           d8c                                   8888X<~  `8888L !  888R Y888r 
''888E`                        ^*888%                                  88888!   .!8*"" `  888R I888> 
  888E                           "8                                    `88888!"*888x      888R I888> 
  888E                                                                  `*8888  8888L     888R I888> 
  888E       .          .         .      88888888                      .x.`888X X888X    u8888cJ888  
  888&      z8k       .@8c      .@8c     88888888                     '888> %8X !8888..-  "*888*P"   
  R888"    %888*"    '%888"    '%888"                                 '888   8  '8888%`     'Y"      
   ""       ?8F        ^*        ^*                                     "*=="     ""                 
            .8                                                                                       
            d"                                       8888888888888                                   
           ~                                                                                         

'''


print('''


       ...                           .x+=:.                   s                                .    
   .xH8%"```"%.                     z`    ^%                 :8                               @88>  
  x888~ xnHhx. ".         u.           .   <k      ..       .88           u.      .u    .     %8P   
 X888X 8**8888k `.  ...ue888b        .@8Ned8"    .@88i     :888ooo  ...ue888b   .d88B :@8c     .    
 8888X<~  `8888L !  888R Y888r     .@^%8888"    ""%888>  -*8888888  888R Y888r ="8888f8888r  .@88u  
 88888!   .!8*"" `  888R I888>    x88:  `)8b.     '88%     8888     888R I888>   4888>'88"  ''888E` 
 `88888!"*888x      888R I888>    8888N=*8888   ..dILr~`   8888     888R I888>   4888> '      888E  
  `*8888  8888L     888R I888>     %8"    R88  '".-%88b    8888     888R I888>   4888>        888E  
 .x.`888X X888X    u8888cJ888       @8Wou 9%    @  '888k  .8888Lu= u8888cJ888   .d888L .+     888E  
'888> %8X !8888..-  "*888*P"      .888888P`    8F   8888  ^%888*    "*888*P"    ^"8888*"      888&  
'888   8  '8888%`     'Y"         `   ^"F     '8    8888    'Y"       'Y"          "Y"        R888" 
  "*=="     ""                                '8    888F                                       ""   
                                               %k  <88F                                             
                                                "+:*%`                                              
                                                                                                    


''')

#print("") 
#bannerKep = pyfiglet.figlet_format("A kovek meselnek...", font = "banner3-D" )
#print(colored(bannerKep, 'light_grey')) #light_grey
#print("\n" + bannerKep)

print(colored("\t  | ", 'grey') + "Nagy Gábor és Szalkai-Szabó Ádám által készített kalandprogram Python nyelveben" + colored(" |", 'grey'))
print("")
write(colored("Üdvözöllek a farmon.\ndfgdsf", 'light_grey',  attrs=['bold']))
print("")
print(colored(" [B] ", 'yellow',  attrs=['bold']) + "Betöltés")
print(colored(" [Ú] ", 'yellow',  attrs=['bold']) + "Új játék")
print(colored(" [K] ", 'yellow',  attrs=['bold']) + "Kilépés")


kezdoValasztas = ''

while True:
    kezdoValasztas = input("---> " + colored("[B/Ú]", 'grey') + ": ")
    
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






print("Before the sleep statement")
time.sleep(1)
print("After the sleep statement")



outc = ['good', 'not', 'maybe']
outc = random.choice(outc)
emon = random.randint(100,500)
# emon = round(emon)

print(outc)
print(emon)


