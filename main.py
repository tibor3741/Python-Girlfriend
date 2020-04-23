#!/usr/bin/python3
#-*- coding:utf-8 -*-
import os
import time
import random
clear = lambda: os.system('cls' if os.name=='nt'else 'clear')
clear()
greatings = ['Üdvözöllek','Szia','Helló','Halli','Hellóka'];
rnd1 = random.choice(greatings);
time.sleep(3)
print(rnd1+' az én nevem Kasszandra')
time.sleep(2)
nev = input("Téged hogy hívnak?: ")
while len(nev)== 0:
  clear()
  print(rnd1+' az én nevem Kasszandra')  
  nev = input("Téged hogy hívnak?: ")
  
eletkor = int(input("Hány éves vagy?: "))
greatings2 = ['Szia','Helló','Halli'];
rnd2 = random.choice(greatings2);
print(rnd2+ " {}.".format(nev))
time.sleep(2)
print('Milyen színű haj tetsszik neked?\n 1.Vörös \n 2.Barna \n 3.Fekete \n 4.Szöke \n 5.Őssz')
haj_szin = int(input("válasz egy számot: "))
time.sleep(1)
print('Milyen haj viselet teszik: \n 1.Rövid Göndör \n 2.Rövid Egyenes \n 3.Rövid Hullámos\n 4.Hosszú Egyenes \n 5.Hosszú Hulámos \n 6.Hosszú Göndör ')
haj_viselet = int(input ('Válasz egy számot: '))
haj_szinek = ["","Vörös", "Barna", "Fekete","Szőke", "Ősz"]
haj_viseletek = ["","Rövid Göndör","Rövid Egyenes","Rövid Hulámos","Hosszú Egyenes","Hosszú Hulámos","Hosszú Göndör"]
print("Nekem Pont "+ haj_szinek[haj_szin]+" és "+  haj_viseletek[haj_viselet]+" a Hajam")
time.sleep(3)
print('Szeretsz engem? \n Igen \n Nem ')
szeret = input('Mit választasz: ')
while len(szeret)== 0:
  clear()
  print(rnd1 +' az én nevem Kasszandra')
  print("Téged hogy hívnak {}".format(nev))
  print('Milyen színű haj tetsszik neked?\n 1.Vörös \n 2.Barna \n 3.Fekete \n 4.Szöke \n 5.Őssz')
  print('Válasz egy számot: {}'.format(haj_viselet))
  print('Milyen haj viselet teszik: \n 1.Rövid Göndör \n 2.Rövid Egyenes \n 3.Rövid Hullámos\n 4.Hosszú Egyenes \n 5.Hosszú Hulámos \n 6.Hosszú Göndör ')
  print('Válasz egy számot: {}'.format(haj_szin))
  print("Nekem Pont "+ haj_szinek[haj_szin]+" és "+  haj_viseletek[haj_viselet]+" a Hajam")

  print('Szeretsz engem? \n Igen \n Nem ')
  szeret = input('Mit választasz: ')


  

if  szeret.casefold() == "igen" :
   print('Én is Szeretlek')
   with open("./datas.txt", "a") as f:
     szoveg= '\n------------- \nNév: {} \nÉletkor: {}'.format(nev,eletkor)+'\n-------------\n\n'
     f.write(szoveg)
     f.close
else:
  print('Oké, Erre majd visszatérünk')
  time.sleep(4)
  szin = input('Melyk a Kedvenc Szined ?:')
  time.sleep(1)
  print ('Nekem is a '+szin+ ' a kedvencem')
goodbyes = ['Viszlát','Szia','Helló']
rnd = random.choice(goodbyes)
time.sleep(3)
print(rnd+ " {}.".format(nev))
time.sleep(2)
exit()
