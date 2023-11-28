class Move:

    def __init__(self, xfrom, yfrom, xto, yto):
        self.xfrom = xfrom
        self.yfrom = yfrom
        self.xto = xto
        self.yto = yto

    

    # Retorna verdadeiro se (xfrom,yfrom) e (xto,yto) forem iguais.
    def equals(self, other_move):
        return self.xfrom == other_move.xfrom and self.yfrom == other_move.yfrom and self.xto == other_move.xto and self.yto == other_move.yto

    def to_string(self):
        return "(" + str(self.xfrom) + ", " + str(self.yfrom) + ") -> (" + str(self.xto) + ", " + str(self.yto) + ")"
