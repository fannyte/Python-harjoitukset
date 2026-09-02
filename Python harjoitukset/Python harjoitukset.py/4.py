# Kysy kolme kokonaislukua käyttäjältä
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))
# Laske ja tulosta lukujen summa, tulo ja keskiarvo
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3
print(f"Lukujen summ on {summa}")
print(f"Lukujen tulo on {tulo}")
print(f"Lukujen keskiarvo on {keskiarvo}")