# Kysy pelaajan nimi ja ikä
player_name = input("Anna pelaajan nimi: ")
player_age = input("Anna pelaajan ikä: ")

# Tallenna tiedot muuttujiin ja tulosta ne
print(f"Pelaajan nimi: {player_name}")
print(f"Pelaajan ikä: {player_age}")

# Jos pelaaja alle 12 vuotta, ilmoita alaikäisyys ja lopeta peli.
if int(player_age) < 12:
    print("Olet alaikäinen, ohjelma suljetaan.")
else: 
    print(f"Tervetuloa, {player_name}!")
    print(f"Päävalikko\n1.  Käynnistä peli\n2. Asetukset\n3. Poistu")
    komento = input("Anna komento: ")
    if komento == "1":
        print("Ladataan...")
        print(f"Päävalikko\n1.  Käynnistä peli\n2. Asetukset\n3. Poistu")
    komento = input("Anna komento: ")
    if komento == "2":
        print("Kieli, ääni, grafiikat")
        print(f"Päävalikko\n1.  Käynnistä peli\n2. Asetukset\n3. Poistu")
    komento = input("Anna komento: ")
    if komento == "3":
        print("Suljetaan...")