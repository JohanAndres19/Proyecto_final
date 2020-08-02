import pygame

class AbstractRight():
    def Sprites_Right(self):
        pass

class AbstractLeft():
    def Sprites_Left(self):
        pass

class AbstractUp():
    def Sprites_Up(self):
        pass

class AbstractDown():
    def Sprites_Down(self):
        pass

class SpritesRightFinn(AbstractRight):
    def Sprites_Right(self):
        pygame.image.load('Sprites/Finn_Movimiento.png')
        return super().Sprites_Right()

class SpritesLeftFinn(AbstractLeft):
    def Sprites_Left(self):
        pygame.image.load('Sprites/Finn_Movimiento.png')
        return super().Sprites_Left()

class SpritesUpFinn(AbstractUp):
    def Sprites_Up(self):
        pygame.image.load('Sprites/Finn_Movimiento.png')
        return super().Sprites_Up()

class SpritesDownFinn(AbstractDown):
    def Sprites_Down(self):
        pygame.image.load('Sprites/Finn_Movimiento.png')
        return super().Sprites_Down()        
