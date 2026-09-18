class Auto:
   nopeudenmuutos = 0
   matka = 0

   def __init__(self, rekisteritunnus, huippunopeus):
      self.rekisteritunnus = rekisteritunnus
      self.huippunopeus = huippunopeus

   def kiihdytä(self, muutos):
      self.nopeus += muutos
      if self.nopeus > self.huippunopeus:
         self.nopeus

auto1 = Auto("ABC_123", 142)

print(f"Ensimmäisen auton rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus}km/h.")