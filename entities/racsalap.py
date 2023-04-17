
class Racsalap:
    # A Python-os programhoz a kiindulási adatbázis - fő elemek
    def __init__(self, id, nev, szekcio, magassag, alsoszelxy, felsoszelxy, alsoszelyz, felsoszelyz, x, y, z, irany,
                 teljes, eltolasxy, eltolasyz, nev1, nev2, nev3, nev4, nev5, nev6, nev7, nev8, felvitel):
        self.id = id                    # A sorazonosító
        self.nev = nev                  # A rácsszerkezet neve
        self.szekcio = szekcio          # A beazonosítható szekció száma
        self.magassag = magassag        # A szekció magassága/kinyúlása
        self.alsoszelxy = alsoszelxy    # A szekció alsó szélessége X-Y /kezdő magassága
        self.felsoszelxy = felsoszelxy  # A szekció felső szélessége X-Y/végső magassága
        self.alsoszelyz = alsoszelyz    # A szekció alsó szélessége Y-Z /kezdő szélessége
        self.felsoszelyz = felsoszelyz  # A szekció felső szélessége Y-Z/végső szélessége
        self.x = x                      # A szekció X-koordinátája
        self.y = y                      # A szekció Y-koordinátája
        self.z = z                      # A szekció Z-koordinátája
        self.irany = irany              # A szekció iránya (Vertikális=1 / Horizontális=2)
        self.teljes = teljes            # A konzol teljes kinyúlása
        self.eltolasxy = eltolasxy      # A felső rész eltolása-XY sík
        self.eltolasyz = eltolasyz      # A felső rész eltolása-YZ sík
        self.nev1 = nev1                # Az aktuális rúd szelvényneve
        self.nev2 = nev2                # Az aktuális rúd szelvényneve
        self.nev3 = nev3                # Az aktuális rúd szelvényneve
        self.nev4 = nev4                # Az aktuális rúd szelvényneve
        self.nev5 = nev5                # Az aktuális rúd szelvényneve
        self.nev6 = nev6                # Az aktuális rúd szelvényneve
        self.nev7 = nev7                # Az aktuális rúd szelvényneve
        self.nev8 = nev8                # Az aktuális rúd szelvényneve
        self.felvitel = felvitel        # A felvitel időpontja