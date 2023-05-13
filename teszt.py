
print('''                                            
          .-.    .'-           .-.                     
         (_) )  / //     .--.-'       /            .-. 
            /  /.-._.   (  (_).-. ---/---.-._.).--.`-' 
          _/_.'(   )     `-.     )_ /   (   )/    /    
       .  /   \ `-'    _    ) (   )/     `-'/  _.(__.  
      (_.'     `-'    (_.--'   `-'
''')




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
    time.sleep(0.13)
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

