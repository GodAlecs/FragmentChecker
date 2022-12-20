#   By GodAlecs
#   GitHub: github.com/GodALecs/FragmentChecker

#   Librerie
import requests
import os
import platform
from colorama import Fore

#   Variabili
saves = "saves.txt" # Variabile del file Saves.txt
link = "https://fragment.com/username/" # Link fragment
banner = f"""
{Fore.RED}▄████  █▄▄▄▄ ██     ▄▀  █▀▄▀█ ▄███▄      ▄     ▄▄▄▄▀ 
█▀   ▀ █  ▄▀ █ █  ▄▀    █ █ █ █▀   ▀      █ ▀▀▀ █    
█▀▀    █▀▀▌  █▄▄█ █ ▀▄  █ ▄ █ ██▄▄    ██   █    █    
█      █  █  █  █ █   █ █   █ █▄   ▄▀ █ █  █   █     
█       █      █  ███     █  ▀███▀   █  █ █  ▀      
▀     ▀      █          ▀           █   ██         
            ▀                                      
{Fore.YELLOW}▄█▄     ▄  █ ▄███▄   ▄█▄    █  █▀ ▄███▄   █▄▄▄▄      
█▀ ▀▄  █   █ █▀   ▀  █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀      
█   ▀  ██▀▀█ ██▄▄    █   ▀  █▀▄   ██▄▄    █▀▀▌       
█▄  ▄▀ █   █ █▄   ▄▀ █▄  ▄▀ █  █  █▄   ▄▀ █  █       
▀███▀     █  ▀███▀   ▀███▀    █   ▀███▀     █        
        ▀                   ▀             ▀     
        
    {Fore.RED}github.com/GodAlecs/FragmentChecker
    """ #   Banner

#   Funzione check_user
def check_user(username): 
    username = username.strip()
    r = requests.get(f"https://fragment.com/username/{username}", allow_redirects=False) #  Controlla se l'username è in asta
    response = str(r.text).split('\n')
    if len(response) != 1:
        print(f"{Fore.GREEN}[+]{Fore.RESET} {username} è possibile acquistarlo su fragment.com")
    else:
        print(f"{Fore.RED}[-]{Fore.RESET} {username} non è possibile acquistarlo su fragment.com")
        #   Qui sotto salva gli username NON in asta in un file
        saves_file = open(saves, "a")
        saves_file.write(f"[-] {username}\n")
        saves_file.close()

#   Funzione Main
def main():
    if "linux" in str(platform.platform()).lower(): #   Cancella le scritte sullo schermo
        os.system("clear")
    else: 
        os.system("cls")
    print(banner)
    wordlist = input(f"{Fore.RESET}[>>] Inserire il nome del file {Fore.GREEN}wordlist{Fore.RESET} -> ") #  Inserire nome della wordlist
    try: #  Vede se esiste la wordlist
        wordlist_file = open(wordlist, "r")
        print(f"{Fore.RESET}[>>] File {wordlist} {Fore.GREEN}caricato{Fore.RESET}!")
        try: #  Vede se esiste il file che salva gli username non in asta
            saves_file = open(saves, "r+")
            print(f"{Fore.RESET}[>>] File {saves} {Fore.GREEN}caricato{Fore.RESET}!")
            saves_file.truncate(0) #    Cancella tutti i dati
            saves_file.close() #   Chiude il file Saves.txt
            pass
        except FileNotFoundError: # Crea il file Saves.txt
            saves_file = open(saves, "w")
            print(f"{Fore.RESET}[>>] File {saves} {Fore.GREEN}creato{Fore.RESET}!")
            saves_file.close()
    except FileNotFoundError: # File wordlist non trovato
        print(f"{Fore.RESET}[>>] File {wordlist} {Fore.RED}non trovato{Fore.RESET}!")
        exit() #    Finisce il programma
    print() #   Spazio vuoto
    for username in wordlist_file.readlines():
        check_user(username.lower())
main() #    Richiama classe Main
