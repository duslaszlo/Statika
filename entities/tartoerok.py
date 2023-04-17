
class Tartoerok:
    # A statikai tartókra feltett erők listája
    def __init__(self, id, projekt, tartonev, jelleg, ertek, hely, hossz, szelveny, felvitel):
        self.id = id                    # A sorazonosító
        self.projekt = projekt          # A statikai számítások főfeladatának a neve
        self.tartonev = tartonev        # A tartó neve
        self.jelleg = jelleg            # Erő-1, megoszló teher-2, nyomaték-3
        self.ertek = ertek              # A teher értéke kN vagy kNpercm vagy kNcm
        self.hely = hely                # A teher helye - cm
        self.hossz = hossz              # A megoszló teher hossza - cm
        self.szelveny = szelveny        # A tartó szelvényeiből származó megoszló terhelések
        self.felvitel = felvitel        # A felvitel időpontja