import pyfiglet
from termcolor import colored

'''from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console'''
  
print("") 

bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "slant") # , font = "slant"
# bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "banner3-D" )
print(colored(bannerKep, 'light_grey'))
# print(bannerKep)

print(colored("| ", 'green') + "scientifically accurate, survival text-based adventure\nset in the future where climate change is inevitabl", colored(" |", 'green'))
print(" ")
print(colored("Welcome to Lost Cause.\nWould you like to load a save or start a new game?", 'red',  attrs=['bold']))
print(" ")
print(colored(" [L] ", 'yellow',  attrs=['bold']) + "LOAD")
print(colored(" [N] ", 'yellow',  attrs=['bold']) + "NEW GAME")

elsoinput = input("---> " + colored("[N/L]", 'magenta') + ": ")

