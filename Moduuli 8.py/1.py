VUODENAJAT = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")
kuukausi = int(input("Anna kuukauden numero (1-12): "))
if 1 <= kuukausi <= 12:
    print(f"Kuukauden {kuukausi} vuodenaika on {VUODENAJAT[kuukausi - 1]}")
else: 
    print("Kuukauden numeron tulee olla väliltä 1-12")
