class Koira:
     def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi


koirat = []
svuosi = 2016
nimi = "A"
for i in range(10):
   koirat.append(Koira(nimi, svuosi))
   svuosi += 1
   nimi = chr(ord(nimi) + 1)
for koira in koirat:
   print(koira.nimi)
   print(koira.syntymävuosi)


   class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

koira1.hauku(2)
koira2.hauku(5)


class Koira:

    väri = ""

    def __init__(self, nimi, syntymävuosi, minun_väri, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.väri = minun_väri 

koira1 = Koira("Muro", 2018, "musta")
print(Koira.väri)
koira2 = Koira("Rekku", 2022, "ruskea","Viu viu viu")
print(Koira.väri)
