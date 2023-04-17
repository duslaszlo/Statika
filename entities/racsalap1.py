
class Racsalap1:
    # A Python-os programhoz a kiindulási adatbázis - a részek
    def __init__(self, id, nev, szekcio, koz, racs1, racs2, racs3, racs4, racs5, racs6, racs7, racs8, felvitel):
        self.id = id                    # A sorazonosító
        self.nev = nev                  # A rácsszerkezet neve
        self.szekcio = szekcio          # A szekció azonosítója
        self.koz = koz                  # A szekción belüli köz azonosítója
        self.racs1 = racs1              # Az aktuális köz rácseleme (1-4)
        self.racs2 = racs2              # Az aktuális köz rácseleme (1-2)
        self.racs3 = racs3              # Az aktuális köz rácseleme (1-5)
        self.racs4 = racs4              # Az aktuális köz rácseleme (1-4,5-8 tükrözve)
        self.racs5 = racs5              # Az aktuális köz rácseleme (1-3,4-6:tükrözve)
        self.racs6 = racs6              # Az aktuális köz rácseleme (1-3,4-6:tükrözve)
        self.racs7 = racs7              # Az aktuális köz rácseleme (1-3,4-6:tükrözve)
        self.racs8 = racs8              # Egyéb rácselemek (1-6)
        self.felvitel = felvitel        # A felvitel időpontja