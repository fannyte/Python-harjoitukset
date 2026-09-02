# Kysy pelaajan nimi ja ikä
player_name = input("Anna pelaajan nimi: ")
player_age = input("Anna pelaajan ikä: ")

# Tallenna tiedot muuttujiin ja tulosta ne
print(f"Pelaajan nimi: {player_name}")
print(f"Pelaajan ikä: {player_age}")

# Jos pelaaja alle 12 vuotta, ilmoita alaikäisyys ja lopeta peli.
if int(player_age) < 12:
    print("Pelaaja on alaikäinen.")
    break
    print("Peli lopetetaan.")
else: 
    print(f"Tervetuloa, {player_name}!")
    print(f"Päävalikko: Käynnistä peli, Asetukset, Poistu")
if