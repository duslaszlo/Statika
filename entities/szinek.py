
class Szinek:
    # A Pantone-s szinskala
    def __init__(self, id, szinnev, r, g, b, felvitel):
        self.id = id                    # A sorazonosító
        self.szinnev = szinnev          # A Pantone-s szinazonosito nev
        self.r = r                      # A piros komponens
        self.g = g                      # A zöld komponens
        self.b = b                      # A kék komponens
        self.felvitel = felvitel        # A felvitel időpontja