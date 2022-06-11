import configparser, platform
from tkinter import messagebox

global update
global force
global update_ver
global VERSION
global skip

config = configparser.ConfigParser()
config.read('config.ini')
force = config['Update']['ForceUpdate']
skip = config['Update']['SkipUpdates']
VERSION = config['Version']['ConfigVersion']
update = configparser.ConfigParser()
update.read ('latest.ini')
update_ver = update['Version']['LatestVersion']
print('Suche nach updates...')
if VERSION != update_ver:
    if skip == 'no':
        print('Es wurden updates gefunden')
        if force == "yes":
            print('Update forced')
        else: 
            yesno = messagebox.askyesno("Update", "Es sind Updates verfügbar :) \nSollen diese Installiert werden?")
            if yesno: 
                print('Updating...')
            else:
                exit()
        quit()
    else:
        print('Skiped Update')
else:
    print('Kein Update gefunden')