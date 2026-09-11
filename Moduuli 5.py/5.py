oikea_tunnus = "python"
oikea_salasana = "rules"
input_tunnus = input("Anna käyttäjätunnus: ")
input_salasana = input("Anna salasana: ")
yritykset = 0
yritykset_max = 5
while (input_tunnus != oikea_tunnus or input_salasana != oikea_salasana) and yritykset < yritykset_max:
    print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen. ")
    input_tunnus = input("Anna käyttäjätunnus: ")
    input_salasana = input("Anna salasana: ")
    yritykset = yritykset + 1
if yritykset >= yritykset_max:
    print("Pääsy evätty. ")
else:
    print("Tervetuloa!")