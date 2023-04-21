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

os.system('cls')
time.sleep(1)
#sys.stdout.write("fgdfgdfg")



#colored('''    
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

filnames = ["./images/img1.txt", "./images/img2.txt", "./images/img3.txt", "./images/img4.txt", 
            "./images/img5.txt", "./images/img6.txt", "./images/img7.txt", "./images/img8.txt",
            "./images/img9.txt", "./images/img10.txt", "./images/img11.txt", "./images/img12.txt", 
            "./images/img13.txt", "./images/img14.txt", "./images/img15.txt", "./images/img16.txt", 
            "./images/img17.txt", "./images/img18.txt", "./images/img19.txt", "./images/img20.txt", 
            "./images/img21.txt", "./images/img22.txt", "./images/img23.txt", "./images/img24.txt", 
            "./images/img25.txt", "./images/img26.txt", "./images/img27.txt", "./images/img28.txt", 
            "./images/img29.txt", "./images/img30.txt", "./images/img31.txt", "./images/img32.txt", 
            "./images/img33.txt", "./images/img34.txt", "./images/img35.txt", "./images/img36.txt", 
            "./images/img37.txt", "./images/img38.txt", "./images/img39.txt", "./images/img40.txt", 
            "./images/img41.txt", "./images/img42.txt", "./images/img43.txt", "./images/img44.txt",
            "./images/img45.txt", "./images/img46.txt"]
frames = []

for name in filnames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())


for frame in frames:
    print("".join(frame))
    time.sleep(0.09)
    os.system('cls')

