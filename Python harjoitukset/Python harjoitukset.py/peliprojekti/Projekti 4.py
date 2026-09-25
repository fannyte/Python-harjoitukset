class Esine: 
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino
        
class Huone: 
    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine

class Pelaaja: 
    def __init__(self, nimi, esineet, sijainti):
        self.nimi = nimi
        self.esineet = esineet
        self.sijainti = sijainti