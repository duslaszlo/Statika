
class Mintacsp:
    # Drótváz minta csomópont koordináták
    def __init__(self, id, irany, csomopont, x, y, z, jellegxy, jellegyz, kezdcspxy, vegecspxy,
                 kezdcspyz, vegecspyz, felvitel):
        self.id = id                          # A sorazonosító
        self.irany : int = irany              # Az irány: 1-függőleges, 2-vízszintes, 3-kéttámaszú
        self.csomopont: int = csomopont
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.jellegxy: int = jellegxy        # 1-fix, 2-változik, 3-számolódik
        self.jellegyz: int = jellegyz        # 1-fix, 2-változik, 3-számolódik
        self.kezdcspxy: int = kezdcspxy      # 3-as jellegnél a kezdőcsp XY-sík
        self.vegecspxy: int = vegecspxy      # 3-as jellegnél a végecsp XY-sík
        self.kezdcspyz: int = kezdcspyz      # 3-as jellegnél a kezdocsp YZ-sík
        self.vegecspyz: int = vegecspyz      # 3-as jellegnél a vegecsp YZ-sík
        self.felvitel = felvitel        # A felvitel időpontja