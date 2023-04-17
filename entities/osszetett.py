
class Osszetett:
    # Az összetett szelvények tételei
    def __init__(self, id, ossznev, nev, diffx, diffy, szog, mirrorx, mirrory, bazis, hiba, felvitel):
        self.id = id                    # A sorazonosító
        self.ossznev = ossznev          # Az összetett szelvény neve
        self.nev = nev                  # Az alszelvény neve / azonosítója
        self.diffx = diffx              # Az eltolás mérete X - mm (0-bázis)
        self.diffy = diffy              # Az eltolás mérete Y - mm (0-bázis)
        self.szog = szog                # A súlypont körüli forgatás mértéke
        self.mirrorx = mirrorx          # Az X-irányú tükrözés (0/1)
        self.mirrory = mirrory          # Az Y-irányú tükrözés (0/1)
        self.bazis = bazis              # A bázist jelölő sorszám (0->bázis)
        self.hiba = hiba                # Az átfedés jelzése
        self.felvitel = felvitel        # A felvitel időpontja