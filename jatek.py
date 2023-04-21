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


   
print('''                                            
          .-.    .'-           .-.                     
         (_) )  / //     .--.-'       /            .-. 
            /  /.-._.   (  (_).-. ---/---.-._.).--.`-' 
          _/_.'(   )     `-.     )_ /   (   )/    /    
       .  /   \ `-'    _    ) (   )/     `-'/  _.(__.  
      (_.'     `-'    (_.--'   `-'
''')#, 'light_grey',  attrs=['bold']))


#print("") 
#bannerKep = pyfiglet.figlet_format("A kovek meselnek...", font = "banner3-D" )
#print(colored(bannerKep, 'light_grey')) #light_grey
#print("\n" + bannerKep)

#print(colored("\t| ", 'grey') + "Nagy Gábor és Szalkai-Szabó Ádám által készített kalandprogram Python nyelveben" + colored(" |", 'grey'))
print("")

write(colored("\t\tÜdvözöllek a farmon.\ndfgdsf", 'light_grey',  attrs=['bold']))
print("")
print(colored(" [B] ", 'yellow',  attrs=['bold']) + "Betöltés")
print(colored(" [Ú] ", 'yellow',  attrs=['bold']) + "Új játék")
print(colored(" [K] ", 'yellow',  attrs=['bold']) + "Kilépés")


kezdoValasztas = ''

while True:
    kezdoValasztas = input("---> " + colored("[B/Ú/K]", 'grey') + ": ")
    
    if kezdoValasztas == "B":
        break
    if kezdoValasztas == "Ú":
        break
    if kezdoValasztas == "K":
        break
    else:
        print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))


nev = ""
penz = ""

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

            print('''

                           .-.            
                          /_  \           
                         /.:\  \          
                        /:::|_  .         
                        \ |:::) |         
                         \|::/  |         
                       _,´\:|    `--.     
           _     __.--´    )|   ´    \    
           \`--'´      )   \|         \   
           |        _.-\    !    \     \  
           | ´   ,-´    `.        `.   |  
           !   .´         `.        \  /  
           '.  |            \       | /   
            '| '             \      |´    
                              !     |   

            ''')



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



#ascii teszt
import os,time
os.system('cls') 
#szörny

szorny = ["./images/szörny/img1.txt", "./images/szörny/img2.txt", "./images/szörny/img3.txt", "./images/szörny/img4.txt", 
            "./images/szörny/img5.txt", "./images/szörny/img6.txt", "./images/szörny/img7.txt", "./images/szörny/img8.txt",
            "./images/szörny/img9.txt", "./images/szörny/img10.txt", "./images/szörny/img11.txt", "./images/szörny/img12.txt", 
            "./images/szörny/img13.txt", "./images/szörny/img14.txt", "./images/szörny/img15.txt", "./images/szörny/img16.txt", 
            "./images/szörny/img17.txt", "./images/szörny/img18.txt", "./images/szörny/img19.txt", "./images/szörny/img20.txt", 
            "./images/szörny/img21.txt", "./images/szörny/img22.txt", "./images/szörny/img23.txt", "./images/szörny/img24.txt", 
            "./images/szörny/img25.txt", "./images/szörny/img26.txt", "./images/szörny/img27.txt", "./images/szörny/img28.txt", 
            "./images/szörny/img29.txt", "./images/szörny/img30.txt", "./images/szörny/img31.txt", "./images/szörny/img32.txt", 
            "./images/szörny/img33.txt", "./images/szörny/img34.txt", "./images/szörny/img35.txt", "./images/szörny/img36.txt", 
            "./images/szörny/img37.txt", "./images/szörny/img38.txt", "./images/szörny/img39.txt", "./images/szörny/img40.txt", 
            "./images/szörny/img41.txt", "./images/szörny/img42.txt", "./images/szörny/img43.txt", "./images/szörny/img44.txt",
            "./images/szörny/img45.txt", "./images/szörny/img46.txt"]
framesszorny = []

for name in szorny:
    with open(name, "r", encoding="utf8") as f:
        framesszorny.append(f.readlines())


for frame in framesszorny:
    print("".join(frame))
    time.sleep(0.09)
    os.system('cls')


#boszorkany
boszorkany = ["./images/boszorkany/img1.txt", "./images/boszorkany/img2.txt", "./images/boszorkany/img3.txt", 
              "./images/boszorkany/img4.txt", "./images/boszorkany/img5.txt", "./images/boszorkany/img6.txt", 
              "./images/boszorkany/img7.txt", "./images/boszorkany/img8.txt", "./images/boszorkany/img9.txt", 
              "./images/boszorkany/img10.txt"]
framesboszorkany = []

for name in boszorkany:
    with open(name, "r", encoding="utf8") as f:
        framesboszorkany.append(f.readlines())


for frame in framesboszorkany:
    print("".join(frame))
    time.sleep(0.1)
    os.system('cls')
    

#piramis
piramis = ["./images/piramis/img1.txt","./images/piramis/img2.txt","./images/piramis/img3.txt"
            ,"./images/piramis/img4.txt","./images/piramis/img5.txt","./images/piramis/img6.txt"]
framespiramis = []

for name in piramis:
    with open(name, "r", encoding="utf8") as f:
        framespiramis.append(f.readlines())


for frame in framespiramis:
    print("".join(frame))
    time.sleep(0.3)
    os.system('cls')