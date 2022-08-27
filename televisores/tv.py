from televisores.marca import Marca

class TV:

    numTv = 0

    def __init__(self, marca:Marca, estado:bool) -> None:
        self._marca = marca
        self._estado = estado
        self._volumen = 1
        self._canal = 1
        self._precio = 500
        TV.numTv+=1

    # attributes 
    def getMarca(self): return self._marca
    def setMarca(self, marca:Marca): self._marca = marca

    def getControl(self): return self._control
    def setControl(self, control): self._control = control

    def getPrecio(self): return self._precio
    def setPrecio(self, precio:int): self._precio = precio

    def getVolumen(self): return self._volumen
    def setVolumen(self, volumen:int):
        if(self._estado and (volumen >= 0 and volumen <= 7)):
             self._volumen = volumen

    def getCanal(self): return self._canal
    def setCanal(self, canal:int):
        if(self._estado and (canal >=1 and canal <= 120)):
             self._canal = canal

    @classmethod
    def getNumTV(cls): return cls.numTv

    @classmethod
    def setNumTV(cls, cantidad): cls.numTv = cantidad

    # tv's state
    def turnOn(self): self._estado = True
    def turnOff(self): self._estado = False
    def getEstado(self): return self._estado

    # tv's volume
    def volumenUp(self):
        if(self._estado and self._volumen < 7):
            self._volumen+=1

    def volumenDown(self):
        if(self._estado and self._volumen > 0):
            self._volumen-=1

    # tv's channels
    def canalUp(self):
        if(self._estado and self._canal < 120):
            self._canal+=1
        
    def canalDown(self): 
        if(self._estado and self._canal > 1):
            self._canal-=1