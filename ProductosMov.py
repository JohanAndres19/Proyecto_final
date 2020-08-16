import pygame

class PrincipalFinn:
  def __init__(self):
    self.Pygame= pygame.image.load('Sprites/Finn_Movimiento.png')
  def Get_image(self):
    return self.Pygame

class PrincipalJake:
  def __init__(self):
    self.Pygame= pygame.image.load('Sprites/jakeconfondo5.png')
  def Get_image(self):
    return self.Pygame

class PrincipalBomberman:
  def __init__(self):
    self.Pygame= pygame.image.load('Sprites/BombermanMod.png')
  def Get_image(self):
    return self.Pygame

class PrincipalLink:
    def __init__(self):
        self.Pygame= pygame.image.load('Sprites/links2.gif')
    def Get_image(self):
     return self.Pygame

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

#----------------------------------FINN
class SpritesRightFinn(AbstractRight,PrincipalFinn):
    
    def Sprites_Right(self):
        self.right_states={0:(0,174,22,34),1:(22,174,22,34),2:(45,174,22,34),3:(69,174,22,34),4:(92,174,22,34),5:(115,174,22,34)}
        self.imagenesRight=Image(self.right_states,self.Get_image()).clip()
        return self.imagenesRight

class SpritesLeftFinn(AbstractLeft,PrincipalFinn):
    def Sprites_Left(self):
        self.left_states={0:(0,137,22,34),1:(22,137,22,34),2:(45,137,22,34),3:(69,137,22,34),4:(92,137,22,34),5:(115,137,22,34)}
        self.image = Image(self.left_states,self.Get_image()).clip()
        return self.image

class SpritesUpFinn(AbstractUp,PrincipalFinn):
    def Sprites_Up(self):
        self.up_states={0:(0,210,22,34),1:(22,210,22,34),2:(45,210,22,34),3:(69,210,22,34),4:(92,210,22,34),5:(115,210,22,34)}
        self.image = Image(self.up_states,self.Get_image()).clip()
        return self.image

class SpritesDownFinn(AbstractDown,PrincipalFinn):
    def Sprites_Down(self):
        self.down_states={0:(0,34,22,34),1:(22,34,22,34),2:(45,34,22,34),3:(69,34,22,34),4:(92,34,22,34),5:(115,34,22,34)}
        self.image = Image(self.down_states,self.Get_image()).clip()
        return self.image     

#-------------------------------------------JAKE
class SpritesRightjake(AbstractRight,PrincipalFinn):
    
    def Sprites_Right(self):
        self.right_states={0:(41,57,21,32),1:(13,58,24,31),2:(65,58,25,31)}
        self.image = Image(self.right_states,self.Get_image()).clip()
        return self.image

class SpritesLeftjake(AbstractLeft,PrincipalJake):
    def Sprites_Left(self):
        self.left_states={0:(39,103,21,32),1:(11,104,25,31),2:(64,104,24,31)}
        self.image= Image(self.left_states,self.Get_image()).clip()
        return self.image

class SpritesUpjake(AbstractUp,PrincipalJake):
    def Sprites_Up(self):
       self.up_states ={0:(41,150,19,32),1:(15,151,20,31),2:(66,151,20,31)}
       self.image=Image(self.up_states,self.Get_image()).clip()   
       return self.image

class SpritesDownjake(AbstractDown,PrincipalJake):
    def Sprites_Down(self):
        self.down_states = {0:(42,13,19,32),1:(17,14,19,31),2:(67,14,19,31)}
        self.image=Image(self.down_states,self.Get_image()).clip()
        return self.image

#-----------------------------------------------------BOMBERMAN
class SpritesRightBomberman(AbstractRight,PrincipalBomberman):
    
    def Sprites_Right(self):
        self.right_states={0:(39,161,18,30),1:(5,161,18,31),2:(71,161,18,31)}
        self.image = Image(self.right_states,self.Get_image()).clip()
        return self.image
class SpritesLeftBomberman(AbstractLeft,PrincipalBomberman):
    def Sprites_Left(self):
        self.left_states={0:(39,65,18,30),1:(9,65,18,30),2:(71,65,18,31)}
        self.image= Image(self.left_states,self.Get_image()).clip()
        return self.image

class SpritesUpBomberman(AbstractUp,PrincipalBomberman):
    def Sprites_Up(self):
       self.up_states ={0:(40,35,17,29),1:(6,35,20,28),2:(71,35,17,29)}
       self.image=Image(self.up_states,self.Get_image()).clip()   
       return self.image

class SpritesDownBomberman(AbstractDown,PrincipalBomberman):
    def Sprites_Down(self):
        self.down_states = {0:(40,0,16,31),1:(6,0,20,31),2:(72,0,16,31)}
        self.image=Image(self.down_states,self.Get_image()).clip()
        return self.image
#--------------------------------------------------LINK
class SpritesRightLink(AbstractRight,PrincipalLink):
    
    def Sprites_Right(self):
        self.right_states={0:(0,0,21,29),1:(32,0,19,29),2:(62,0,20,29),3:(94,1,20,28),4:(124,1,20,28),5:(155,1,20,29),6:(186,1,20,29),7:(218,1,19,27)}
        self.image = Image(self.right_states,self.Get_image()).clip()
        return self.image

class SpritesLeftLink(AbstractLeft,PrincipalLink):
    def Sprites_Left(self):
        self.left_states={0:(498,1,21,29),1:(529,0,22,31),2:(560,1,22,30),3:(591,1,22,30),4:(622,1,21,30),5:(653,0,22,31),6:(684,0,21,31),7:(715,1,21,30)}
        self.image= Image(self.left_states,self.Get_image()).clip()
        return self.image

class SpritesUpLink(AbstractUp,PrincipalLink):
    def Sprites_Up(self):
       self.up_states ={0:(745,2,20,29),1:(776,2,20,29),2:(808,4,19,27),3:(838,4,19,26),4:(869,2,20,28),5:(900,1,19,29),6:(930,3,20,28),7:(962,3,20,27)}
       self.image=Image(self.up_states,self.Get_image()).clip()   
       return self.image

class SpritesDownLink(AbstractDown,PrincipalLink):
    def Sprites_Down(self):
        self.down_states = {0:(248,2,20,27),1:(279,2,20,27),2:(311,1,19,28),3:(341,0,20,29),4:(372,2,20,27),5:(403,2,20,27),6:(434,1,20,28),7:(466,1,19,29)}
        self.image=Image(self.down_states,self.Get_image()).clip()
        return self.image

