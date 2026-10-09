# Monster Hazzle - Fanny Tervala TXK26S1-B

# Pelin idea: Pelaaja taistelee hirviöitä vastaan ja kerää pisteitä. Pisteillä voi ostaa varusteita.

import random
import sys

HAHMOT = {"1": "Moldmorph", "elämä": 100, "vahinko": 20, "2": "Slimey", "elämä": 100, "vahinko": 20, "3": "Sewer", "elämä": 100, "vahinko": 20}
KAUPPA = {"1": "Pölypallo", "hinta": 10, "2": "Luonnonkivi", "hinta": 20, "3": "Myrkky", "hinta": 30}

# Kysy pelaajan nimi ja ikä

player_name = input("Anna pelaajan nimi:")
player_age = input("Anna pelaajan ikä:")

# Tallenna tiedot muuttujiin ja tulosta ne
print(f"Pelaajan nimi: {player_name}")
print(f"Pelaajan ikä: {player_age}")

# Jos pelaaja on alle 12 vuotta, ilmoita alaikäisyys ja lopeta peli.
if int(player_age) < 12:
    print("Olet alaikäinen, ohjelma suljetaan.")
    while True:
        sys.exit()
else: 
    print(f"Tervetuloa, {player_name}!")
    print(f"Päävalikko \n1. Käynnistä peli \n2. Asetukset \n3. Poistu")
    komento = input("Anna komento: ")

    if komento == "1":
        print("Ladataan...")
        print(f"Päävalikko\n1. Käynnistä peli \n2. Asetukset \n3. Poistu")

    if komento == "2":
        print("1. Kieli\n2. Ääni \n3. Grafiikat")
        komento = input("Anna komento: ")

        if komento == "1":
            print("Valitse kieli: Suomi, Svenska, English")

        if komento == "2":
            print("Säädä ääntä 1...100")

        if komento == "3":
            print("Säädä grafiikat: matala, keski, korkea")
            print(f"Päävalikko \n1. Käynnistä peli \n2. Asetukset \n3. Poistu")

    komento = input("Anna komento: ")

    if komento == "3":
        print("Suljetaan...")

# Peli käynnistyy, kun pelaaja valitsee "Käynnistä peli" päävalikosta

komento = input("1. Uusi peli 2 \n2. Jatka peliä \n3.Poistu")

if komento == "2":
    print("Haetaan tallennettuja pelejä...")
    print("Ladataan peliä...")

if komento == "3":
    print("Suljetaan...")

elif komento == "1":
    print("Aloitetaan uusi peli...")
    print("Ladataan...")
    print("Valitse hahmo: 1. Moldmorph \n2. Slimey \n3. Sewer")

    komento = input("Anna komento: ")

    if komento == "1":
        print("Moldmorph mädättää vihollisia")

    elif komento == "2":
        print("Slimey heittää limaa vihollisia kohti")

    elif komento == "3":
        print("Sewer myrkyttää vihollisten juomavettä")

while True:
      print("\n1. Kauppaan \n2. Suoraan peliin")

      komento = input("Anna komento: ")

      if komento == "1":
            kauppa(pelaaja)

      elif komento == "2":
            break

def kauppa(pelaaja): 
    print("Tervetuloa kauppaan! Valitse varuste: 1. Pölypallo (10 pistettä) \n2. Luonnonkivi (20 pistettä) \n3. Myrkky (30 pistettä)")

    komento = input("Anna komento: ")

    if komento == "1":
        if pelaaja["pisteet"] >= 10:
            print("Haluatko ostaa Pölypallon? (Kyllä/Ei)")
            vastaus = input("Anna vastaus: ")

    elif vastaus == "Kyllä":
                
                print("Ostit Pölypallon!")
    elif vastaus == "Ei":
                print("Valitse varuste: 1. Pölypallo (10 pistettä) \n2. Luonnonkivi (20 pistetä) \n3. Myrkky (30 pistettä)")

    elif pelaaja["pisteet"] >= 20:
            print("Haluatko ostaa Luonnonkiven? (Kyllä/Ei)")

            vastaus = input("Anna vastaus: ")

    elif vastaus == "Kyllä":
                print("Ostit Luonnonkiven!")

    elif vastaus == "Ei":
                print("Valitse varuste: 1. Pölypallo (10 pistettä) \n2. Luonnonkivi (20 pistetä) \n3. Myrkky (30 pistettä)")

    elif pelaaja["pisteet"] >= 30:
            print("Haluatko ostaa Myrkyn? (Kyllä/Ei)")

            vastaus = input("Anna vastaus: ")

    elif vastaus == "Kyllä":
                print("Ostit Myrkyn!")

    elif vastaus == "Ei":
                print("Valitse varuste: 1. Pölypallo (10 pistettä) \n2. Luonnonkivi (20 pistetä) \n3. Myrkky (30 pistettä)")
    else: 
          print("Sinulla ei ole tarpeeksi pisteitä varusteita varten.")

start_game = input("Haluatko aloittaa pelin? (Kyllä/Ei)")

if start_game == "Ei":
      print("Takaisn päävalikkoon...")

elif start_game == "Kyllä":
      print("Peli alkaa!")

def taistelu(pelaaja, hirviö):
    while True:
        print(f"Taistelu alkaa! Pelaaja: {pelaaja["nimi"]} vastaan Hirviö: {hirviö["nimi"]}")
        komento = input("1. Hyökkää \n2. Puolusta \n3. Käytä [varuste]")

        if komento == "1": 
            vahinko = random.randint(10, 30)
            hirviö["elämä"] -= vahinko
            print(f"Hyökkäsit {hirviö["nimi"]} ja teit {vahinko} vahinkoa! Hirviön elämä: {hirviö["elämä"]}")
            print(f"Hirviö hyökkää takaisin! {hirviö["nimi"]} tekee {hirviö["vahinko"]} vahinkoa! Pelaajan elämä: {pelaaja["elämä"]}")

        elif hirviö["elämä"] <= 0:
            print(f"Voitit taistelun! Saat 10 pistettä.")
            pelaaja["pisteet"] += 10

        elif komento == "2": 
            print("Puolustauduit hyökkäykseltä!")

        elif komento == "3": 
            print("Käytä varuste: [varuste]")
            print("Käytit varustetta! Vastustaja menettää + (10, 20, 30) elämää.")

def lopputeksti(pelaaja):
    print("\n=== PELI LÄPÄISTY ===")
    print(f"Onneksi olkoon, {pelaaja['nimi']}!")
    print(f"{pelaaja['hahmo']} voitti kaikki hirviöt.")
    print(f"Loppupisteet: {pelaaja['pisteet']}")
    print("Kiitos pelaamisesta!")

    sys.exit()

def tallenna_peli(pelaaja):
    varusteet = ",".join(pelaaja["varusteet"])
    with open("save.txt", "a", encoding="utf-8") as tiedosto:
        tiedosto.write(f"{pelaaja['nimi']};{pelaaja['hahmo']};{pelaaja['elämä']};{pelaaja['pisteet']};{varusteet}\n")
    print("Peli tallennettu!")