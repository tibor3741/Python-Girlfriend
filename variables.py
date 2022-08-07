#!/usr/bin/python3
import random
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
how_was_your_day = ['Jó','Fantasztikus','Rossz', ]
love_me = ['Igen','Persze','Imádlak','Naná','Szeretlek']
kifogas=['Mennem kell','ne haragudj de most mennem kell','Bocsi de most mennem kell','Bocsi de mennem kell','Ne haragudj de menem kell','később beszélünk',]

#kérdések és  válasz lista  hivatkozások
quest_dict =    {
  "csá": random.choice(greetings),
  "szia": random.choice(greetings),
  "helló": random.choice(greetings),
  "üdv": random.choice(greetings),
  "szió": random.choice(greetings),                                      "hali": random.choice(greetings),
  "Hellóka": random.choice(greetings),
  "hogy vagy?": random.choice(how_are_you),
  "hogy érzed magad?": random.choice(how_are_you),                       "milyen volt a napod?": random.choice(how_was_your_day),
  "milyen volt a heted?":random.choice(how_was_your_day),
  "milyen napod volt?": random.choice(how_was_your_day),
  "milyen heted volt?":random.choice(how_was_your_day),
  "szeretsz?": random.choice(love_me),
  "szeretsz engem?": random.choice(love_me),
  "szeretel?": random.choice(love_me),
  "imádsz engem?": random.choice(love_me),
  "imádsz?": random.choice(love_me),
  "imádasz?": random.choice(love_me),
  "imádol?": random.choice(love_me),
  "imádasz engem?": random.choice(love_me),
  "imádol engem?":  random.choice(love_me)
}
                                                                       
#Felhasználók                                                          nev_adat = ['']
ev_adat = []

