
class Kontur:
    # A kontúr rajzoláshoz szükséges egyenesek és görbék
    def __init__(self, id, nev, vonal, sorszam, jelleg, x1, y1, x2, y2, r1, r2, irany, felvitel):
        self.id = id                # A sorazonosító
        self.nev: str = nev         # A szelvény neve
        self.vonal: int = vonal     # A körvonal sorszáma 1-külső, 2 és több belső
        self.sorszam: int = sorszam # Az elem sorszáma
        self.jelleg: int = jelleg   # Egyenes vagy görbe (E->1/G->2)
        self.x1: int = x1           # Vonal: x1, görbe: KözéppontX
        self.y1: int = y1           # Vonal: y1, görbe: Középponty
        self.x2: int = x2           # Vonal: x2, görbe: Sugárx
        self.y2: int = y2           # Vonal: y2, görbe: Sugáry
        self.r1: int = r1           # Vonal: 0, görbe: Kezdőszög
        self.r2: int = r2           # Vonal: 0, görbe: Végszög
        self.irany: int = irany     # A görbék rajzolásánál az irány (1->CCW,2->CW)
        self.felvitel = felvitel    # A rögzítés időpontja
