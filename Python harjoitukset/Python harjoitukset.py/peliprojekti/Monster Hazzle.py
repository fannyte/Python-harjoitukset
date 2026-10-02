# Pelin idea: Pelaaja taistelee hirviöitä vastaan ja kerää pisteitä. Pisteillä voi ostaa varusteita.

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
        print("Suljetaan...")
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
else: 
    print("Aloitetaan uusi peli...")
    print("Ladataan...")
    print("Valitse hahmo: 1. Moldmorph \n2. Slimey \n3. Sewer")
    komento = input("Anna komento: ")
    if komento == "1":
        print("Moldmorph mädättää vihollisia")
    if komento == "2":
        print("Slimey heittää limaa vihollisia kohti")
    if komento == "3":
        print("Sewer myrkyttää vihollisten juomavettä")

