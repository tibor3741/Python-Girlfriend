#!/usr/bin/python3
#-*- coding:utf-8 -*-

import os
import time
import random

# Függvények
# ==========
# Képernyő törlése
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')             

#Egy Szöveges kérdés a felhasználótól
def user_kerdez(kerdes):
        valasz = input(kerdes)
        while len(valasz)== 0:
                print('Mit akartál kérdezni ?')
                valasz = input(kerdes)
        return valasz  
#Egy szöveges Kérsdés    
def kerdez(kerdes):
        valasz = input(kerdes)
        while len(valasz)== 0:
                print('Mondd el légyszi! ')
                valasz = input(kerdes)
        return valasz
# Választás egy listából a sorszám használatávan
def valaszt(kerdes, opciok):
    print(kerdes)
    for i in range(len(opciok)):
        print(str(i+1) + '. ' + opciok[i])
    valasz = int(input('Válassz egy számot: ')) - 1
    while valasz < 0 or valasz >= len(opciok):
        print('Ilyen sorszámú opció nincs! ')
        valasz = int(input('Válassz egy számot: ')) - 1
    return valasz

# Eldönti, hogy igen, vagy nem
def eldont(kerdes):
        while True:
            valasz = input(kerdes).casefold()
            if valasz in ['i', 'igen', 'persze', 'nagyon']:
                return True
            elif valasz in ['n', 'nem', 'dehogy']:
                return False
            else:
                print('Ezt nem értem. ')

#jatek1

import random

def guess(x):
    random_number = random.randint(1, x)
    tipp = 0
    while tipp != random_number:
        tipp = int(input(f'Gondoltam egy Számra  1 és {x}-között: '))
        if tipp < random_number:
            print('Bocsi, a tipelj újra. túl kevés a tiped.')
        elif tipp > random_number:
            print('Bocsi, tipelj únra. túl nagy a tipped.')

    print(f'Yay, Gratulálok. kitaláltad a {random_number} gondoltam ügyes vagy!!')

#Változók
#--------------------------------------
# Beállítások
mods=['Beszèlgesünk','Játszunk valamit']
games=['Gondoltam egy Számra','Kő Papìr Ollò']
haj_szinek = ['Vörös', 'Barna','Szőke', 'Fekete', 'Ősz']
haj_hosszok = ['Rövid', 'Vállig érő', 'Hosszú']
haj_viseletek = ['Göndör', 'Egyenes','Hullámos']

# Kommunikációs részek válasz listák
greetings = ['Üdvözöllek','Szia','Helló','Halli','Hellóka'];
goodbyes = ['Viszlát','Szia','Helló']
how_are_you = ['Jól','Fantasztikusan','Rosszul','Hiányoztál','Ha veled lehetek akkor jól'];
how_was_your_day = ['Jó','Fantasztikus','Rossz', ]
love_me = ['Igen','Persze','Imádlak','Naná','Szeretlek']
kifogas=['Mennem kell','ne haragudj de most mennem kell','Bocsi de most mennem kell','Bocsi de mennem kell','Ne haragudj de menem kell','később beszélünk',]

#kérdések és  válasz lista  hivatkozások
quest_dict =	{
  "csá": random.choice(greetings),
  "szia": random.choice(greetings),
  "helló": random.choice(greetings),
  "üdv": random.choice(greetings),
  "szió": random.choice(greetings),
  "hali": random.choice(greetings),
  "Hellóka": random.choice(greetings),
  "hogy vagy?": random.choice(how_are_you),
  "hogy érzed magad?": random.choice(how_are_you),
  "milyen volt a napod?": random.choice(how_was_your_day),
  "milyen volt a heted?":random.choice(how_was_your_day),
  "milyen napod volt?": random.choice(how_was_your_day),
  "milyen heted volt?":random.choice(how_was_your_day),
  "szeretsz?": random.choice(love_me),
  "szeretsz engem?": random.choice(love_me),
  "szeretel?": random.choice(love_me),
  "imádsz engem?": random.choice(love_me),
  "imádsz?": random.choice(love_me),
  "imádasz?": random.choice(love_me),
  "imádaol?": random.choice(love_me),
  "imádasz engem?": random.choice(love_me), 
  "imádol engem?":  random.choice(love_me)
}
 

#Felhasználók
nev_adat = ['tibor','tibi']
ev_adat = [19, 19, 19]

# Fő ciklus
# =========
clear()
time.sleep(3)
# Üdvözlés
print(random.choice(greetings), 'az én nevem Kasszandra.')
time.sleep(2)
# Alapadatok
nev = kerdez('Téged hogy hívnak? ')
nev.lower()
eletkor = int(kerdez('Hány éves vagy? '))


mods_changer = valaszt('Akkarsz tenni velem?', mods)
if (mods_changer ==1):
    print('játèkok')
    game_changer = valaszt('Mit játszunk?', games)
    
    if (game_changer ==1):
        print('folytköv')
    else:
        guess(10)











#ilyen felhasználó van vagy nincs
elif (nev in nev_adat):
        #van ilyen
        def get_value(quest_dict, quest_key):#kereső
                for key,value in quest_dict.items():
                        if key == quest_key:
                                return value
                return "nem értem a kérdést"
        print ('Besszélgesünk...')#szövegbekérés
        szoveg=' '
        while szoveg !='viszlát':
                szoveg = input('')
                talalat = get_value(quest_dict, szoveg)
                print(talalat)
                
        #már vége a kérdezésnek
        print('mennem kell')
        print(goodbyes[1]+' '+nev)
        
        exit()
else:
        #nincs ilyen
        # listához hozzáad valamit
        def rekord(nev, eletkor):
                nev_adat.append(nev)
                ev_adat.append (eletkor)
        clear()
        time.sleep(2)

        # Először nem szeret
        szeret = False
        # Addig kérdezgetjük, amíg nem mondja, hogy szeret
        time.sleep(2)
        while not szeret:
                # Nőideál
                haj_szin = valaszt('Milyen színű haj tetszik neked?', haj_szinek)
                haj_hossz = valaszt('Milyen hosszú haj tetszik neked?', haj_hosszok)
                haj_viselet = valaszt('Milyen haj viselet teszik?', haj_viseletek)
                # Nahát, pont ilyen a hajam :D
                print('Nekem Pont', haj_szinek[haj_szin], 'és', haj_hosszok[haj_hossz], haj_viseletek[haj_viselet], 'a Hajam')
                # Megkérdezzük, hogy szeret-e
                time.sleep(3)
                szeret = eldont('Szeretsz engem? ')
                if not szeret:
                        print('Oké, Erre majd visszatérünk')
                        time.sleep(4)
        # Itt már kilépett a ciklusból, szóval biztos, hogy szeret
        print('Én is Szeretlek')
        rekord(nev, eletkor)
        # Kedvenc szín
        szin = kerdez('Melyik a kedvenc színed? ')
        szin.lower()
        print('Nekem is a', szin, 'a kedvencem')
        time.sleep(1)
        # Elköszönés
        print(random.choice(kifogas))
        print(random.choice(goodbyes), nev)
exit()

