import random
# Arvo kolmenumeroinen koodi (numerot 0..9)
kolme_numeroa = "".join(str(random.randint(0, 9)) for _ in range(3))
# Arvo nelinumeroinen koodi (numerot 1..6)
nelja_numeroa = "".join(str(random.randint(1, 6)) for _ in range(4))
# Tulosta arvotut koodit
print(f"Kolmenumeroinen koodi (0..9):", kolme_numeroa)
print(f"Nelinumeroinen koodi (1..6):", nelja_numeroa)