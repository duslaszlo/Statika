
class Tartok:
    # A statikai tartók megnevezései
    def __init__(self, id, projekt, tartonev, tipus, hossz, konzol1, konzol2, szelveny, aktiv, note, felvitel):
        self.id = id                    # A sorazonosító
        self.projekt = projekt          # A statikai számítások főfeladatának a neve
        self.tartonev = tartonev        # A tartó neve
        self.tipus = tipus              # Kéttámaszú-1, konzolos-2, kéttámaszú konzolos-3
        self.hossz = hossz              # A tartó belsö támaszköze
        self.konzol1 = konzol1          # A tartó FA melletti konzol hossza
        self.konzol2 = konzol2          # A tartó FB melletti konzol hossza
        self.szelveny = szelveny        # A szelvény neve
        self.aktiv = aktiv              # Az éppen aktuális tartó
        self.note = note                # A tartóhoz tartozó egyéb információk
        self.felvitel = felvitel        # A felvitel időpontja