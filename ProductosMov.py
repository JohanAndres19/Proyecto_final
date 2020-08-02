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
        self.Pygame= pygame.image.load('Sprites/Finn_Movimiento.png')
        self.right_states={0:(0,174,22,34),1:(22,174,22,34),2:(45,174,22,34),3:(69,174,22,34),4:(92,174,22,34),5:(115,174,22,34)}
        return self.Pygame.clip(self.right_states)

class SpritesLeftFinn(AbstractLeft):
    def Sprites_Left(self):
        self.Pygame= pygame.image.load('Sprites/Finn_Movimiento.png')
        self.left_states={0:(0,137,22,34),1:(22,137,22,34),2:(45,137,22,34),3:(69,137,22,34),4:(92,137,22,34),5:(115,137,22,34)}
        return self.Pygame.clip(self.left_states)

class SpritesUpFinn(AbstractUp):
    def Sprites_Up(self):
        self.Pygame=pygame.image.load('Sprites/Finn_Movimiento.png')
        self.up_states={0:(0,210,22,34),1:(22,210,22,34),2:(45,210,22,34),3:(69,210,22,34),4:(92,210,22,34),5:(115,210,22,34)}
        return self.Pygame.clip(self.up_states)

class SpritesDownFinn(AbstractDown):
    def Sprites_Down(self):
        self.Pygame=pygame.image.load('Sprites/Finn_Movimiento.png')
        self.down_states={0:(0,34,22,34),1:(22,34,22,34),2:(45,34,22,34),3:(69,34,22,34),4:(92,34,22,34),5:(115,34,22,34)}
        return self.Pygame.clip(self.down_states)       
