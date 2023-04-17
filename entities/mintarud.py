
class Mintarud:
    # A minta drótváz rúdjai
    def __init__(self, id, irany, tipus, verzio, kezdocsp, vegecsp):
        self.id = id                    # A sorazonosító
        self.irany = irany              # Az irány: 1-függőleges, 2-vízszintes, 3-kéttámaszú
        self.tipus = tipus
        self.verzio = verzio
        self.kezdocsp = kezdocsp
        self.vegecsp = vegecsp
