#!/usr/bin/python3
#-*- coding:utf-8 -*-

import os
import time
import random

# Függvények
# ==========

# Képernyő törlése
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# Egy szöveges kérdés
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

# Fájlhoz hozzáad valamit
def rekord(nev, eletkor):
	f = open('./datas.txt', 'a')
	f.write('Név: ' + nev + '\nÉletkor: ' + str(eletkor) +'\n\n-------------\n\n')
	f.close()


# Változók
# ========

# Kommunikációs részek
greetings = ['Üdvözöllek','Szia','Helló','Halli','Hellóka'];
goodbyes = ['Viszlát','Szia','Helló']

# Beállítások
haj_szinek = ['Vörös', 'Barna','Szőke', 'Fekete', 'Ősz']
haj_hosszok = ['Rövid', 'Vállig érő', 'Hosszú']
haj_viseletek = ['Göndör', 'Egyenes','Hullámos']


# Fő ciklus
# =========
clear()
time.sleep(3)
# Üdvözlés
print(random.choice(greetings), 'az én nevem Kasszandra.')
time.sleep(2)
# Alapadatok
nev = kerdez('Téged hogy hívnak? ')
eletkor = int(kerdez('Hány éves vagy? '))

# Üdvözlés a név használatával
print(random.choice(greetings), nev)
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
print('Nekem is a', szin, 'a kedvencem')
time.sleep(1)
# Elköszönés
print('Most mennem kell')
print(random.choice(goodbyes), nev)

exit()

