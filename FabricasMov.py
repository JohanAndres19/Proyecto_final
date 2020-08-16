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
        return PrincipalFinn().Get_image()     
 

class FabricaJake(FabricaAbstracta):
    def Mover_derecha(self):
        return SpritesRightjake().Sprites_Right()

    def Mover_izquierda(self):
        return SpritesLeftjake().Sprites_Left()

    def Mover_abajo(self):
        return SpritesDownjake().Sprites_Down()

    def Mover_arriba(self):
        return SpritesUpjake().Sprites_Up()

    def Get_principal(self):
        return PrincipalJake().Get_image()

class FabricaBomberman(FabricaAbstracta):
 
    def Mover_derecha(self):
        return SpritesRightBomberman().Sprites_Right()

    def Mover_izquierda(self):
        return SpritesLeftBomberman().Sprites_Left()

    def Mover_abajo(self):
        return SpritesDownBomberman().Sprites_Down()

    def Mover_arriba(self):
        return SpritesUpBomberman().Sprites_Up()

    def Get_principal(self):
        return PrincipalBomberman().Get_image()

class FabricaLink(FabricaAbstracta):
 
    def Mover_derecha(self):
        return SpritesRightLink().Sprites_Right()

    def Mover_izquierda(self):
        return SpritesLeftLink().Sprites_Left()

    def Mover_abajo(self):
        return SpritesDownLink().Sprites_Down()

    def Mover_arriba(self):
        return SpritesUpLink().Sprites_Up()

    def Get_principal(self):
        return PrincipalLink().Get_image()