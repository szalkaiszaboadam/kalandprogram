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
        
        
i = 0
leltar = ''

while i < 1:
  '''
  for i in range(len(mentsekOssz)):
        mentettNevek += mentsekOssz[i]["nev"] + "/"
  txt = open("mentesek.txt", "a+", encoding="utf8")
  print(f"{nev};100;0;0;0;0;0;0", file=txt)
  txt.close()'''



  
  os.system('cls')


  with open("mentesek.txt","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if f"{nev}" not in line:
            f.write(line)
    f.truncate()

  txt = open("mentesek.txt", "a+", encoding="utf8")
  print(f"{nev};{eletero};{penz};{kard};{pajzs};{alma};{kenyer};{gyogyital}", file=txt)
  txt.close()

  print(f"· ·:·: " + colored(f"{nev}", attrs=['bold']) + " :·:· ·\n\n")
  #print(colored(f"\t· ·:·: {nev} :·:· ·\n", attrs=['bold']))
  print(colored(f"Életerőd: ") + colored(f"{eletero}\n", attrs=['bold']))


  print(colored("Mit szeretnél csinálni?\n", 'red', attrs=['bold']))
  print(colored(" [F] felfedez  ", 'green') + colored("[L] leltár  ", 'yellow') + colored("[Á] árus  ", 'red') + colored("[K] kilépés", 'blue'))
  print("")

valasztas = ''


while True:
    valasztas = input("---> " + colored("[F/L/Á/K]", 'magenta', attrs=['bold']) + ": ")
        
    if valasztas == "F":
        break
    if valasztas == "L":
        break
    if valasztas == "Á":
        break
    if valasztas == "K":
        break
    else:
            print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))
  

if valasztas == "K": #Kilépés
        time.sleep(1)
        i += 1
if valasztas == "F": #Felfedez
        
        os.system('cls')

        #randomka = ['var', 'utszeliCsoves', 'lovag', 'ismeretlenLeny', 'falu', 'erdo', 'barlang']
        randomka = ['var', 'var']
        #'utszeliCsoves', 'utszeliCsoves', 'ut', 'ut', 'ut', 'ut', 'ut', 'var', 'var', 'lovag', 'lovag'
        randomValasztas = random.choice(randomka)

        #megtámadod? megfutamodsz?
        #bemész? elkerülöd?

        if randomValasztas == "ut":
            print("\n- Sétálsz egy úton, nem történik semmi...")

            visszateres = input(colored("\n[NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

        if randomValasztas == "utszeliCsoves":
            randomkaCsoves = ['1', '2', '3']
            randomValasztasCsoves = random.choice(randomkaCsoves)

            if randomValasztasCsoves == "1":
                print("- Összetalálkoztál egy útszélén lévő csövessel, mit teszel?")

            if randomValasztasCsoves == "2":
                print("- Meglátsz egy csövest az útszélén, mit akarsz tenni?")

            if randomValasztasCsoves == "3":
                print("- A távolban megpillantasz egy csövest, mit akarsz csinálni?")


            print(colored("\n [K] kifosztás  ", 'green') + colored("[E] elkerülés  ", 'yellow'))
            #valasztasCsoves = input("---> " + colored("[K/E]", 'magenta', attrs=['bold']) + ": ")

            while True:
                    valasztasCsoves = input("\n---> " + colored("[K/E]", 'magenta', attrs=['bold']) + ": ")
        
                    if valasztasCsoves == "K":
                        break
                    if valasztasCsoves == "E":
                        break
                    else:
                        print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))
                    
            if valasztasCsoves == "K":
                randomkaKifosztas = ['1', '1', '2', '2', '2', '3']
                randomValasztasKifosztas = random.choice(randomkaKifosztas)

                if randomValasztasKifosztas == "1":

                    randomkaKifoszottDolog = ['penz', 'alma', 'alma', 'kenyer', 'kenyer']
                    randomValasztasKifosztottDolog = random.choice(randomkaKifoszottDolog)

                    if randomValasztasKifosztottDolog == "penz":
                        penzRandom = random.randint(1,5)
                        penz += penzRandom
                        print(f"\nKifosztottad a csövest, találtál nála: {penzRandom}x aranyforintot. Továbbindulsz!")
                    if randomValasztasKifosztottDolog == "alma":
                        almaRandom = random.randint(1,3)
                        alma += almaRandom
                        print(f"\n- Kifosztottad a csövest, találtál nála: {almaRandom}x almát. Továbbindulsz!")

                    if randomValasztasKifosztottDolog == "kenyer":
                        kenyerRandom = random.randint(1,2)
                        kenyer += kenyerRandom
                        print(f"\n- Kifosztottad a csövest, találtál nála: {kenyerRandom}x kenyeret. Továbbindulsz!")

                if randomValasztasKifosztas == "2":
                    print("\n- Nem találtál semmit a csövesnél, ezért továbbindulsz.")

                if randomValasztasKifosztas == "3":
                    csovesTamadasRandom = random.randint(4,10)

                    eletero = eletero - csovesTamadasRandom

                    print(f"\n- Váratlanul rádtámad a csöves, {csovesTamadasRandom} sebzést okoz, így marad {eletero} életerőd.")

            if valasztasCsoves == "E":
                randomkaElkerules = ['1', '2']
                randomValasztasElkerules = random.choice(randomkaElkerules)

                if randomValasztasElkerules == "1":
                    print("\n- Elhaladtál a csöves mellett, furcsán nézett rád.")
                if randomValasztasElkerules == "2":
                    print("\n- Elkerülted a csövest, megkönnyebülten sóhajt fel.")

            
            visszateres = input(colored("\n[NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

        if randomValasztas == "var":
            randomkaVar = ['1', '2', '3']
            randomValasztasVar = random.choice(randomkaVar)

            if randomValasztasVar == "1":
                print("- A távolban, a ködből alig kilátszodó várat pillantasz meg, elindulsz az irányába?")

            if randomValasztasVar == "2":
                print("- A dombok tetjén egy vár magasodik ki, betérsz a várba?")

            if randomValasztasVar == "3":
                print("- Egy táblát pillantasz meg, észak irányába vár található, elindulsz felé?")


            print(colored("\n [I] igen  ", 'green') + colored("[N] nem  ", 'yellow'))
            #valasztasCsoves = input("---> " + colored("[K/E]", 'magenta', attrs=['bold']) + ": ")

            while True:
                    valasztasVar = input("\n---> " + colored("[I/N]", 'magenta', attrs=['bold']) + ": ")
        
                    if valasztasVar == "I":
                        break
                    if valasztasVar == "N":
                        break
                    else:
                        print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))

            if valasztasVar == "I":
                randomkaVarIgen = ['1', '2', '2', '2', '3', '3']
                randomValasztasVarIgen = random.choice(randomkaVarIgen)

                if randomValasztasVarIgen == "1":
                    forintRandom = random.randint(3,10)
                    print(f"\n- A vár lakói régóta várták már egy ilyen emberre mint te, meg is ajándékoznak téged, kapsz tőlük {forintRandom}x aranyforintot")

                if randomValasztasVarIgen == "2":

                    randomkaKifoszottDolog = ['alma', 'alma', 'kenyer']
                    randomValasztasKifosztottDolog = random.choice(randomkaKifoszottDolog)

                    if randomValasztasKifosztottDolog == "alma":
                        almaRandom = random.randint(1,2)
                        alma += almaRandom
                        print(f"\n- Nem fogadnak nagy örömmel a várban élők, de ígyis eltudsz lopni {almaRandom}x almát. Megmenekülsz!")

                    if randomValasztasKifosztottDolog == "kenyer":
                        kenyerRandom = random.randint(1,2)
                        kenyer += kenyerRandom
                        print(f"\n- Nem fogadnak nagy örömmel a várban élők, de ígyis eltudsz lopni {kenyerRandom}x kenyeret. Megmenekülsz!")


                if randomValasztasVarIgen == "3":
                    varTamadasRandom = random.randint(6,16)

                    eletero = eletero - varTamadasRandom

                    print(f"\n- Nem fogadnak jó szívvel a várlakók, megtámadnak és meg is sérülsz, {varTamadasRandom} sebzést kapsz, így marad {eletero} életerőd.")

                visszateres = input(colored("\n[NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

            if valasztasVar == "N":
                randomkaVarNem = ['1', '2']
                randomValasztasVarNem = random.choice(randomkaVarNem)

                if randomValasztasVarNem == "1":
                    print("\n- Lehet jól tetted, hogy nem merészkedtél a vár környékére.")

                if randomValasztasVarNem == "2":
                    print("\n- Lehet, hogy nagy lehetőséget szalasztottál el...")

                visszateres = input(colored("\n[NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

        if randomValasztas == "lovag":
            randomkaLovag = ['1', '1', '2', '3']
            randomValasztasLovag = random.choice(randomkaLovag)

            if randomValasztasLovag == '1':
                print("\n- Összetalálkozol egy lovaggal, majd egy jót beszélgettek, utatok elválik..")

            if randomValasztasLovag == '2':

                lovagTamadasRandom = random.randint(8,18)

                eletero = eletero - lovagTamadasRandom

                print(f"\n- Összetűzésbe kerülsz egy lovaggal aki az utadba állt, súlyos {lovagTamadasRandom} sebzést okozott, {eletero} életerőd maradt.")

            if randomValasztasLovag == '3':
                
                lovagTamadasRandomKetto = random.randint(3,7)

                eletero = eletero - lovagTamadasRandomKetto

                print(f"\n- A távolban meglátsz egy lovagot, elbeszélgettetek egymással és tapasztalatokat osztottatok meg, de ellentétbe kerültök egyással, {lovagTamadasRandomKetto} sebzést okozott, {eletero} életerőd maradt.")
            
            visszateres = input(colored("\n[NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")


if valasztas == "L": #Leltár
        
        os.system('cls')

        if penz != 0:
            leltar += colored(f" {penz}", attrs=['bold']) + " aranyforint, "

        if kard != 0:
            leltar += f"\n " + colored(f"{kard}x", attrs=['bold']) + " kard, " # sebzés 5d

        if pajzs != 0:
            leltar += f"\n " + colored(f"{pajzs}x", attrs=['bold']) + " pajzs, "




        if alma != 0:
            leltar += f"\n " + colored(f"{alma}x", attrs=['bold']) + " alma, " # +1

        if kenyer != 0:
            leltar += f"\n " + colored(f"{kenyer}x", attrs=['bold']) + " kenyér, " # +2

        if gyogyital != 0:
            leltar += f"\n " + colored(f"{gyogyital}x", attrs=['bold']) + " gyógyulás itala, " #10 és 20 között / ritka

        #átok kő

        #balta sebzés 4


        if leltar == '':
            leltar = colored(' Jelenleg nincs semmi a leltáradban', 'red')

            #visszateres = input(colored("\n[NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

        print(f"· ·:·: " + colored(f"Leltárad tartalma", attrs=['bold']) + " :·:· ·")
        #print(colored("Leltárad tartalma:", "yellow"))
        print(leltar)

        #visszateres = input(colored("\n[NYOMJ EGY ENTERT]", "green", attrs=['bold']) + ": ")

        print(colored("\n\nSzeretnél felhasználni egy tárgyat?", 'red', attrs=['bold']))

        print(colored("\n [I] igen  ", 'green') + colored("[N] nem  ", 'yellow'))
            #valasztasCsoves = input("---> " + colored("[K/E]", 'magenta', attrs=['bold']) + ": ")

        while True:
                valasztasIgenNem = input("\n---> " + colored("[I/N]", 'magenta', attrs=['bold']) + ": ")
        
                if valasztasIgenNem == "I":
                    break
                if valasztasIgenNem == "N":
                    break
                else:
                    print(colored("Kérjük, válassz egyet a rendelkezésre álló lehetőségek közül", 'red'))
