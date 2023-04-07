import pyfiglet
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
  
bannerKep = pyfiglet.figlet_format("Kalandprogram", font = "slant")
print("\n", bannerKep)

print("")
print("[green]|[/green]  scientifically accurate, survival text-based adventure\nset in the future where climate change is inevitable  [green]|[/green]")
print(" ")

print("[bold red]Welcome to Lost Cause.\nWould you like to load a save or start a new game?")
print(" ")
print("[bold yellow] [L] [/bold yellow] LOAD")
print("[bold yellow] [N] [/bold yellow] NEW GAME")