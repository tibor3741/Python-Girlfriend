#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import time
import random
from variables import *
# Függvények
# ==========
# Képernyő törlése
def clear(): return os.system('cls' if os.name == 'nt' else 'clear')

# Egy Szöveges kérdés a felhasználótól


def user_kerdez(kerdes):
    valasz = input(kerdes)
    while len(valasz) == 0:
        print('Mit akartál kérdezni ?')
        valasz = input(kerdes)
    return valasz
# Egy szöveges Kérsdés


def kerdez(kerdes):
    valasz = input(kerdes)
    while len(valasz) == 0:
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


def guess(x):
    random_number = random.randint(1, x)
    tipp = 0
    while tipp != random_number:
        tipp = int(input(f'Gondoltam egy Számra  1 és {x}-között: '))
        if tipp < random_number:
            print('Bocsi, a tipelj újra. túl kevés a tiped.')
        else:
            print('Bocsi, tipelj újra. túl nagy a tipped.')

    print(
        f'Yay, Gratulálok. kitaláltad a {random_number} gondoltam ügyes vagy!!')


# Fő ciklus
# =========
clear()
time.sleep(3)
# Üdvözlés
print(random.choice(greetings), 'az én nevem Kasszandra.')
time.sleep(2)def check_user_input(input):
input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any
# Alapadatok
nev = kerdez('Téged hogy hívnak? ')
nev.lower()
eletkor = int(kerdez('Hány éves vagy? '))


mods_changer = valaszt('mit akkarsz tenni velem?', mods)
if (mods_changer == 1):
    print('játèkok')
    game_changer = valaszt('Mit játszunk?', games)

    if (game_changer == 1):
        print('folytköv')
    else:

        time.sleep(2)
        # Először akkar ujra jatszani
        ujra = True
        while ujra:
            guess(10)
            ujra = eldont('Jatszunk egyet ùjra? ')

# ilyen felhasználó van vagy nincs
elif (nev in nev_adat):
    # van ilyen
    def get_value(quest_dict, quest_key):  # kereső:
        for key, value in quest_dict.items():
            if key == quest_key:
                return value
        return "nem értem a kérdést"
    print('Besszélgesünk...')  # szövegbekérés
    szoveg = ' '
    while szoveg != 'viszlát':
        szoveg = input('')
        talalat = get_value(quest_dict, szoveg)
        print(talalat)

    # már vége a kérdezésnek
    print(random.choice(kifogas))
    print(goodbyes[1]+' '+nev)

    exit()
else:
    # nincs ilyen
    # listához hozzáad valamit
    def rekord(nev, eletkor):
        nev_adat.append(nev)
        ev_adat.append(eletkor)
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
        print('Nekem Pont', haj_szinek[haj_szin], 'és',
              haj_hosszok[haj_hossz], haj_viseletek[haj_viselet], 'a Hajam')
        # Megkérdezzük, hogy szeret-e
        time.sleep(3)
        szeret = eldont('Szeretsz engem? ')
        if not szeret:
            print('Oké, Erre majd visszatérünk')
            time.sleep(4)
    # Itt már kilépett a ciklusból, szóval biztos, hogy szeret
    print('Én is Szeretlek')
    rekord(nev_adat, ev_adat)

   # Kedvenc szín
    szin = kerdez('Melyik a kedvenc színed? ')
    szin.lower()
    print('Nekem is a', szin, 'a kedvencem')
    time.sleep(1)
    # Elköszönés
    print(random.choice(kifogas))
    print(random.choice(goodbyes), nev)
    print(rekord)
exit()
