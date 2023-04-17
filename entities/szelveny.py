
class Szelveny:
    # Acélszerkezeti szelvények keresztmetszeti jellemzői
    def __init__(self, id, nev, filenev, magassag, szelesseg, v, r, r1, r2, w, w1, u, u1, u2, z, c,
                h1, t, tgalfa, a, ex, ey, ix, kx, sx, inx, iy, ky, sy, iny,
                fmsuly, anyag, megnevezes, megjegyzes, felvitel):
        self.id = id                    # A sorazonosító
        self.nev = nev                  # A szelvény neve
        self.filenev = filenev          # A szelvény neve a kiíratáshoz
        self.magassag = magassag        # A szelvény horizontális mérete X - mm (h)
        self.szelesseg = szelesseg      # A szelvény vertikális mérete Y - mm  (b)
        self.v = v                      # A vastagsága mm
        self.r = r                      # Kerekítési sugár mm
        self.r1 = r1                    # mm
        self.r2 = r2                    # mm
        self.w = w                      # mm
        self.w1 = w1                    # mm
        self.u = u                      # mm
        self.u1 = u1                    # mm
        self.u2 = u2                    # mm
        self.z = z                      # mm
        self.c = c                      # mm
        self.h1 = h1                    # I profilnál a gerincszélesség - mm
        self.t = t                      # mm
        self.tgalfa = tgalfa            # mm
        self.a = a                      # A szelvény területe - cm^2
        self.ex = ex                    # A súlyponttávolság - X - mm
        self.ey = ey                    # A súlyponttávolság - Y - mm
        self.ix = ix                    # A szelvény X inerciája - cm^4
        self.kx = kx                    # A szelvény keresztmetszeti jellemzője X - cm^3
        self.sx = sx                    # A szelvény statikai jellemzője X - cm^3
        self.inx = inx                  # A szelvény inerciasugara X - cm
        self.iy = iy                    # A szelvény Y inerciája - cm^4
        self.ky = ky                    # A szelvény keresztmetszeti jellemzője Y - cm^3
        self.sy = sy                    # A szelvény statikai jellemzője Y - cm^3
        self.iny = iny                  # A szelvény inerciasugara Y - cm
        self.fmsuly = fmsuly            # A szelvény folyómétersúlya - kg/m
        self.anyag = anyag              # Az alapanyag neve -> alap: Acélok
        self.megnevezes = megnevezes    # A szervény bővebb megnevezése
        self.megjegyzes = megjegyzes    # A szabványszám vagy egyéb megjegyzés
        self.felvitel = felvitel        # A felvitel időpontja