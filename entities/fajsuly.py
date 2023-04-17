
class Fajsuly:
    # Alapanyagsúlyok Kg/dm3-ben
    def __init__(self, id, megnevezes, fajsuly, rugmodulus, felvitel):
        self.id = id                           # A sorazonosító
        self.megnevezes: str = megnevezes      # Az alapanyag neve
        self.fajsuly: float = fajsuly          # Az anyag fajsúlya - Kg/dm3
        self.rugmodulus: float = rugmodulus    # Az anyag rugalmassági modulusa kN/cm2
        self.felvitel = felvitel               # A rögzítés időpontja
