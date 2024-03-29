#####################################################################
#                          Vok Train Master                         #
#                     by Simon, ico277 and BReep                    #
#####################################################################

#Module laden

print(f' ')
print(f' ')
print(f' ')
print('Import Modules')
from os import path
from tkinter import Tk, simpledialog, messagebox
from os.path import exists
import random, toml, configparser, platform
from xml.etree.ElementTree import VERSION
print('Modules imported sucess')
print('Loding GLOBAL Variables')
global VERSION
global ver
global folder
global debugmode
global vok
global datei
global cfg
global username
global config
global configver
VERSION	= '1.0.2'
print (VERSION)
print('Variables loaded sucess')
print('loading Config parameters')
if not exists(f"./config.ini"):
    yesno = messagebox.askyesno("Config fehler", "Die Configurations-Datei existiert nicht.\nSoll eine neue erstellt werden?")
    if yesno: 
        with open(f"./config.ini", "w") as file:
            file.write("[DEFAULT]\npfad = .\nDeinName = Nutzer\n\n[DEBUG]\ndebug = false\n\n[Update]\nForceUpdate = no\nSkipUpdates = no\n\n[Version]\nConfigVersion = 1.0.1\n#do not change this")
            file.close()
    else:
        exit()
config = configparser.ConfigParser()
config.read('config.ini')
datei = config['DEFAULT']['pfad']
debugmode = config['DEBUG']['debug']
username = config['DEFAULT']['DeinName']
configver = config['Version']['ConfigVersion']
print('Config parameters imported sucess')
print('Parsing Version')
if VERSION != configver:
    print('Fehler: Code 1926 | Bitte melde dich im Discord-Support')
    quit()
print('Parsing Version completed')
print('Check for Vok file')
if datei == '.':
    print ('Verzeichnis: Intern')
else:
    print ('Verzeichnis:' + datei)
folder = datei
if not exists(f"{folder}/vok.toml"):
    yesno = messagebox.askyesno("vok.toml", "Die vok.toml Datei existiert nicht.\nSoll eine neue erstellt werden?")
    if yesno: 
        with open(f"{folder}/vok.toml", "w") as file:
            file.write("[vocab]\n")
            file.close()
    else:
        exit()
vok = toml.load(f"{folder}/vok.toml")
print('Vok File was found')
print(f' ')
print(f'-------------------------------------------')
print(f'Inizialisieren erfolgreich abgeschlossen')
print(f'-------------------------------------------')
print(f' ')
print(f' ')
print(f' ')
print(f' ')
print(f'-------------------------------------------------------------------------------------------')
print(f' ')
print(f'        Vokabel Trainer by ItzSimmi, BReep und ico277, Version {VERSION}')
print(f' ')
print(f'-------------------------------------------------------------------------------------------')
root = Tk()
root.withdraw()
print(f'Willkommen, ' + username)
print(f' ')

if debugmode == 'true':
    print(f' ')
    print(f'--------------------| Debug Mode |---------------------------')
    print(f'Debug Mode')
    print(f' ')
    print ('OS: ' + platform.platform())
    print ('Build: ' + platform.machine())
    print ('CPU: ' + platform.processor())
    print ('Python: ' + platform.python_version())
    print(f' ')
    print(f'-------------------------------------------------------------')


while True:
    aufgabe = simpledialog.askstring('Aufgabe', '1: Abfrage   2: Eingeben')
    if aufgabe == '1':
        global rnd_key_old
        rnd_key_old = None
        while True:
            keys = list(vok["vocab"].keys())
            if len(keys) < 1:
                messagebox.askokcancel("Vocab", "Es sind keine Vokabeln gespeichert oder weniger als 2 Vokablen verfügbar.\nBitte fügen sie Vokabeln hinzu.")
                break
            rnd_key = random.choice(keys)
            while rnd_key == rnd_key_old:
                rnd_key = random.choice(keys)
            rnd_value = vok["vocab"][rnd_key]
            if random.randrange(2) == 1:
                antwort = simpledialog.askstring("Deutsch", f"Deutsch: Was heißt '{rnd_key}'?")
                if antwort == None:
                    break
                elif antwort.lower() == rnd_value.lower():
                    messagebox.askokcancel("Richtig!", f"Richtig!\nDie Antwort ist '{rnd_value}'.")
                else:
                    messagebox.askokcancel("Falsch!", f"Die Antwort ist falsch!\nDie richtige Antwort war '{rnd_value}'.")
            else:
                antwort = simpledialog.askstring("Fremdsprache", f"Fremdsprache: Was heißt '{rnd_value}'?")
                if antwort == None:
                    break
   
                elif antwort.lower() == rnd_key.lower():
                    messagebox.askokcancel("Richtig!", f"Richtig!\nDie Antwort ist '{rnd_key}'.")
                else:
                    messagebox.askokcancel("Falsch!", f"Die Antwort ist falsch!\nDie richtige Antwort war '{rnd_key}'.")
            rnd_key_old = rnd_key
    elif aufgabe == '2':
        while True:
            neues_deutsch = simpledialog.askstring('Deutsch', 'Wie ist das Deutsche Wort?')
            if neues_deutsch == 'exit':
                break
            elif neues_deutsch == '':
                break
            elif neues_deutsch == None:
                break
            else:
                print(neues_deutsch)
                neues_fremdsprache = simpledialog.askstring('Fremdsprache', 'Wie ist das Wort in der Fremdsprache?')
                if neues_fremdsprache == '':
                    break
                elif neues_fremdsprache == None:
                    break
                else:
                    print(neues_fremdsprache)
                    vok["vocab"][neues_deutsch] = neues_fremdsprache
    elif aufgabe == 'credits':
        print('Created with <3 by Simon ,Enrico and BReep')
    elif aufgabe == 'Simon':
        print('Simon ist der Gründer dieses Projekts und auch der Haupt-Programmierer')
    elif aufgabe == 'Enrico':
        print('Enrico ist der zweite Projektentwickler und ein risieger Ehrenmann')
    elif aufgabe == 'BReep':
        print('BReep ist der dritte Projektentwickler')
    elif aufgabe == 'Apfel':
        print('Das ist mein Mittagessen | ~Simon')
    elif aufgabe == 'Kaesekuchen' or aufgabe == 'Käsekuchen':
        print('Lecker')
    elif aufgabe == 'exit':
        break
    else:
        break

try:
    vok_file = open(f"{folder}/vok.toml", "w")
    vok_file.write(toml.dumps(vok))
    vok_file.close()
except Exception as ex:
    messagebox.askokcancel("Fehler", "Ein fehler ist aufgetreten beim speichern der Vokabeln!")
    raise ex
