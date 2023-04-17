
class Projectek:
    # A statikai számítások főfeladatainak felsorolása
    def __init__(self, id, projekt, megrendelo, leiras, aktiv, felvitel):
        self.id = id                    # A sorazonosító
        self.projekt = projekt          # A statikai számítások főfeladatának a neve
        self.megrendelo = megrendelo    # A számítás megrendelője
        self.leiras = leiras            # A project bővebb leírása
        self.aktiv = aktiv              # A project státusza: 1-Aktív
        self.felvitel = felvitel        # A felvitel időpontja