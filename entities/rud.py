
class Rud:
    # A rudak koordinatai
    def __init__(self, id, projekt, azonosito, kezdocsp, vegecsp, anyag, piros, zold, kek, vastagsag, szelveny, mark):
        self.id = id                         # A sorazonosító
        self.projekt: str = projekt          # A statikai számítások főfeladatának a neve
        self.azonosito: str = azonosito      # A vázszerkezet azonosítója
        self.kezdocsp: int = kezdocsp        # A rúd kezdő-csomópontja
        self.vegecsp: int = vegecsp          # A rúd vég-csomópontja
        self.anyag: str = anyag              # A rúd rugalmassági modulusa ????
        self.piros: int = piros              # A kijelzés piros komponense
        self.zold: int = zold                # A kijelzés zöld komponense
        self.kek: int = kek                  # A kijelzés kék komponense
        self.vastagsag: float = vastagsag    # A rúd vastagsaga
        self.szelveny: str = szelveny        # A szelvény neve
        self.mark: int = mark                # A kijelzés megjelölése
