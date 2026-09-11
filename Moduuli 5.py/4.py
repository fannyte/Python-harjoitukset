import random
oikein_arvaus = random.randint(1, 10)
arvaus = int(input("Arvaa kokonaisluku väliltä 1..10: "))
while arvaus != oikein_arvaus:
    if arvaus < oikein_arvaus:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")
    arvaus = int(input("Arvaa kokonaisluku väliltä 1..10: "))
    print("Oikein!")
