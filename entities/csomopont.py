
class Csomopont:
    # Rúdszerkezet csomópont koordináták
    def __init__(self, id, projekt, azonosito, csomopont, x, y, z,mark):
        self.id = id                        # A sorazonosító
        self.projekt: str = projekt         # A statikai számítások főfeladatának a neve
        self.azonosito: str = azonosito     # A vázszerkezet azonosítója
        self.csomopont: int = csomopont     # A csomópont sorszáma
        self.x: float = x                   # A csomópont X-koordinátája
        self.y: float = y                   # A csomópont Y-koordinátája
        self.z: float = z                   # A csomópont Z-koordinátája
        self.mark: int = mark               # A kijelzés megjelölése