kuhan_pituus = float(input("Anna kuhan pituus (cm): "))
if kuhan_pituus < 37:
    alamitta = 37 - kuhan_pituus
    print("Kuha on " + str(alamitta) + " cm liian lyhyt. Laske kuha takaisin veteen.")