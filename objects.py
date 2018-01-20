class Bicicleta:
  def __init__(self, culoare, viteze, frane):
    self.culoare = culoare
    self.viteze = viteze
    self.frane = frane

  def getColor(self):
    print self.culoare

  def getViteze(self):
    print self.viteze

  def getFrane(self):
    print self.frane


bicicleta1 = Bicicleta("rosu", "35", "disc")
bicicleta2 = Bicicleta("albastru", "25", "saboti")

bicicleta1.getColor()
bicicleta2.getColor()

bicicleta1.getViteze()
bicicleta2.getViteze()

bicicleta1.getFrane()
bicicleta2.getFrane()
