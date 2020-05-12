greetings = ['Üdvözöllek','Szia','Helló','Halli','Hellóka'];
goodbyes = ['Viszlát','Szia','Helló']
how_are_you = ['Jól','Fantasztikusan','Rosszul','Hiányoztál','Ha veled lehetek akkor jól'];
how_was_your_day = ['Jó','Fantasztikus','Rossz', ]
love_me = ['Igen','Persze','Imádlak','Naná','Szeretlek']
#Felhasználók
nev_adat = ['Tibor', 'tibor', 'Tibi','tibi']
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
eletkor = int(kerdez('Hány éves vagy? '))

#ilyen felhasználó van vagy nincs
if (nev in nev_adat):
        #van ilyen
        print('Űdvözöllek újra')
        user = user_kerdez('')
        if(user=='szia' or 'helló' or 'Szia' or 'Helló'):
                print(random.choice(greetings), nev)
        else:
                print('erre nem tudom a választ')
        user = user_kerdez('')
        if(user=="hogy vagy?"or"hogy érzed magad?"):
                print(random.choice(how_are_you))
        else:
                print('erre nem tudom a választ')
        user = user_kerdez('')
        if(user=="milyen volt a napod?"or"milyen volt a heted ?"or"milyen napod volt?"):
                print(random.choice(how_was_your_day))
        if(user=="szeretsz?"or'szeretel?'or'szeretszengem?'):
                print(random.choice(love_me))
        else:
                print('erre nem tudom a választ')
        #már vége a kérdezésnek
        print('mennem kell')
        print('Szia')
        
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
        print('Nekem is a', szin, 'a kedvencem')
        time.sleep(1)
        # Elköszönés
        print('Most mennem kell')
        print(random.choice(goodbyes), nev)
exit()

