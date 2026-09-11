vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0 and vuosi % 100 == 0 and vuosi % 400 == 0:
    print("On karkausvuosi")
else:
    print("Ei ole karkausvuosi")