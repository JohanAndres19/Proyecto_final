import pygame

class Principal:
  def __init__(self):
    self.Pygame= pygame.image.load('Sprites/Finn_Movimiento.png')
  def Get_image(self):
    return self.Pygame


class AbstractRight(Principal):
    def Sprites_Right(self):
        pass

class AbstractLeft(Principal):
    def Sprites_Left(self):
        pass

class AbstractUp(Principal):
    def Sprites_Up(self):
        pass

class AbstractDown(Principal):
    def Sprites_Down(self):
        pass

class SpritesRightFinn(AbstractRight):
    
    def Sprites_Right(self):
        self.right_states={0:(0,174,22,34),1:(22,174,22,34),2:(45,174,22,34),3:(69,174,22,34),4:(92,174,22,34),5:(115,174,22,34)}
        self.imagenesRight=Image(self.right_states,self.Get_image()).clip()
        return self.imagenesRight

class SpritesLeftFinn(AbstractLeft):
    def Sprites_Left(self):
        self.left_states={0:(0,137,22,34),1:(22,137,22,34),2:(45,137,22,34),3:(69,137,22,34),4:(92,137,22,34),5:(115,137,22,34)}
        self.image = Image(self.left_states,self.Get_image()).clip()
        return self.image

class SpritesUpFinn(AbstractUp):
    def Sprites_Up(self):
        self.up_states={0:(0,210,22,34),1:(22,210,22,34),2:(45,210,22,34),3:(69,210,22,34),4:(92,210,22,34),5:(115,210,22,34)}
        self.image = Image(self.up_states,self.Get_image()).clip()
        return self.image

class SpritesDownFinn(AbstractDown):
    def Sprites_Down(self):
        self.down_states={0:(0,34,22,34),1:(22,34,22,34),2:(45,34,22,34),3:(69,34,22,34),4:(92,34,22,34),5:(115,34,22,34)}
        self.image = Image(self.down_states,self.Get_image()).clip()
        return self.image     


class Image():
    def __init__(self,estados,sheet):
        self.estados=estados
        self.sheet= sheet
        self.imagenes=[]

    def clip(self):
        for i in range(len(self.estados)):
            self.sheet.set_clip(pygame.Rect(self.estados[i]))
            self.imagenes.append(self.sheet.get_clip())
        return self.imagenes
        
        