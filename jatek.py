import pyfiglet
from termcolor import colored

'''from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console'''
  
print("") 

bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "slant") # , font = "slant"
# pyfiglet.figlet_format("Kalandprogram", font = "banner3-D" )
print(colored(bannerKep, 'blue'))
print(bannerKep)

print(colored("| ", 'green'), "scientifically accurate, survival text-based adventure\nset in the future where climate change is inevitabl", colored(" |", 'green'))

print(" ")

print("[bold red]Welcome to Lost Cause.\nWould you like to load a save or start a new game?")
print(" ")
print("[bold yellow] [L] [/bold yellow] LOAD")
print("[bold yellow] [N] [/bold yellow] NEW GAME")