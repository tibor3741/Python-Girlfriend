#!/usr/bin/python3
#-*- coding:utf-8 -*-
print('Helló az én nevem Kasszandra')
nev = input("Téged hogy hívnak?: ")
eletkor = int(input("Hány éves vagy?: "))
if eletkor < 20:
  print("Szia {}.".format(nev))
else:
   print("Helló {}.".format(nev))

print('Milyen színű haj tetsszik neked?\n 1.Vörös \n 2.Barna \n 3.Fekete \n 4.Szöke \n 5.Őssz')
haj_szin = int( input ('Válasz egy számot: '))
    
print('Milyen haj viselet teszik: \n 1.Rövid Göndör \n 2.Rövid Egyenes \n 3.Hosszú Göndör \n 4.Hosszú Egyenes ')
haj_viselet = int(input ('Válasz egy számot: '))
#Hajviselet 1
#-----------------------------------------------------
if haj_szin == 1 and haj_viselet == 1:
  print('Nekem Pont Vörös és Rövid Göndör a Hajam')
elif haj_szin == 2 and haj_viselet == 1:
  print('Nekem Pont Barna és Rövid Göndör a Hajam')
elif haj_szin == 3 and haj_viselet == 1:
  print('Nekem Pont Fekete és Rövid Göndör a Hajam')
elif haj_szin == 4 and haj_viselet == 1:
  print('Nekem Pont Szőke és Rövid Göndör a Hajam')
elif haj_szin == 5 and haj_viselet == 1:
  print('Nekem Pont Őssz és Rövid Göndör a Hajam')
#Hajviselet 2
# ------------------------------------------------------
elif haj_szin == 1 and haj_viselet == 2:
  print('Nekem Pont Vörös és Rövid Egyenes a Hajam')
elif haj_szin == 2 and haj_viselet == 2:
  print('Nekem Pont Barna és Rövid Egyenes a Hajam')
elif haj_szin == 3 and haj_viselet == 2:
  print('Nekem Pont Fekete és Rövid Egyenes a Hajam')
elif haj_szin == 4 and haj_viselet == 2:
  print('Nekem Pont Szöke és Rövid Egyenes a Hajam')
elif haj_szin == 5 and haj_viselet == 2:
  print('Nekem Pont Őssz és Rövid Egyenes a Hajam')
#Hajviselet 3 
# ------------------------------------------------------
elif haj_szin == 1 and haj_viselet == 3:
  print('Nekem Pont Vörös és Hosszú Göndör a Hajam')
elif haj_szin == 2 and haj_viselet == 3:
  print('Nekem Pont Barna és Hosszú Göndör a Hajam')
elif haj_szin == 3 and haj_viselet == 3:
  print('Nekem Pont Fekete és Hosszú Göndör a Hajam')
elif haj_szin == 4 and haj_viselet == 3:
  print('Nekem Pont Szőke és Hosszú Göndör a Hajam')
elif haj_szin == 5 and haj_viselet == 3:
  print('Nekem Pont Őssz és Hosszú Göndör a Hajam')

#Hajviselet4
#----------------------------------------------------------
elif haj_szin == 1 and haj_viselet == 4:
  print('Nekem Pont Vörös és Hosszú Egyenes  a Hajam')
elif haj_szin == 2 and haj_viselet == 4:
  print('Nekem Pont Barna és Hosszú Egyenes a Hajam')
elif haj_szin == 3 and haj_viselet == 4:
  print('Nekem Pont Fekete és Hosszú Egyenes a Hajam')
elif haj_szin == 4 and haj_viselet == 4:
  print('Nekem Pont Szőke és Hosszú  Egyenes a Hajam')
elif haj_szin == 5 and haj_viselet == 4:
  print('Nekem Pont Őssz és Hosszú Egyenes a Hajam')

print('Szeretsz engem? \n Igen \n Nem ')


szeret = input('Mit választasz: ')

if  szeret.casefold() == "igen" :
   print('Én is Szeretlek')
else:
  print('Oké, Erre majd visszatérünk')


with open("./datas.txt", "w") as f:
   szoveg = 'Név: {}\nÉletkor: {}'.format(nev, eletkor)+'\n'
   f.write(szoveg)

f.close()
exit()
