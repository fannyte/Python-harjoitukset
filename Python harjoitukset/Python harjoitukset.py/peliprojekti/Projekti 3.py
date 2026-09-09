# Luo jokaiselle päävalikon toiminnolle funktio

def Käynnistä_peli(aseet):
    print("Valitse ase:")
    for aseet in aseet:
        print("Aseet: limapallo, mönjä, myrkky")

def Asetukset(kieli, ääni, grafiikat):
    print("Valitse asetus: ")
    for kieli in kieli:
        print("Kieli: Suomi, Ruotsi, Englanti")
    for ääni in ääni:
        print("Ääni: 1...100")
    for grafiikat in grafiikat:
        print("Grafiikat: matala, keski, korkea")

def Poistu(poistu):
    print("Suljetaan...")
    for poistu in poistu:
        print("Miksi haluat poistua? En usko että olet vielä valmis...")