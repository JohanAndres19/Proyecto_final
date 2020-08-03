from ProductosMov import *
class FabricaAbstracta:
    def Mover_derecha(self):
        pass

    def Mover_izquierda(self):
        pass

    def Mover_arriba(self):
        pass

    def Mover_abajo(self):
        pass 

    def Get_principal(self):
        pass

class FabricaFinn(FabricaAbstracta):
 
    def Mover_derecha(self):
        return SpritesRightFinn().Sprites_Right()

    def Mover_izquierda(self):
        return SpritesLeftFinn().Sprites_Left()

    def Mover_abajo(self):
        return SpritesDownFinn().Sprites_Down()

    def Mover_arriba(self):
        return SpritesUpFinn().Sprites_Up()

    def Get_principal(self):
        return Principal().Get_image()     
 