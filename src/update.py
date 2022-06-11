import configparser, wget, os, time
from tkinter import messagebox

global update
global force
global update_ver
global VERSION
global skip

print('Suche nach letzer Version-ID')
url = 'https://raw.githubusercontent.com/ItzSimmi/VokTrainMaster-Updater/main/latest.ini'
wget.download(url)
time.sleep (10)

config = configparser.ConfigParser()
config.read('config.ini')
force = config['Update']['ForceUpdate']
skip = config['Update']['SkipUpdates']
VERSION = config['Version']['ConfigVersion']
update = configparser.ConfigParser()
update.read ('latest.ini')
update_ver = update['Version']['LatestVersion']
print('\nSuche nach updates...')
if VERSION != update_ver:
    if skip == 'no':
        print('Es wurden updates gefunden')
        if force == "yes":
            print('Update forced')
            os.remove("main.py")
            os.remove("config.ini")
            wget.download('https://raw.githubusercontent.com/ItzSimmi/VokTrainData/latest/src/main.py')
            wget.download('https://raw.githubusercontent.com/ItzSimmi/VokTrainData/latest/src/config.ini')
        else: 
            yesno = messagebox.askyesno("Update", "Es sind Updates verfügbar :) \nSollen diese Installiert werden?")
            if yesno: 
                print('Updating...')
                os.remove("main.py")
                os.remove("config.ini")
                wget.download('https://raw.githubusercontent.com/ItzSimmi/VokTrainData/latest/src/main.py')
                wget.download('https://raw.githubusercontent.com/ItzSimmi/VokTrainData/latest/src/config.ini')
            else:
                time.sleep (2)
    else:
        print('Skiped Update')
else:
    print('Kein Update gefunden')
os.remove("latest.ini")
