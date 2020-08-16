from FabricasMov import *
import pygame

class Director():
    _Builder=None

    def set_builder(self,builder):
       self._Builder=builder
       self._personaje=None

    def Get_personaje(self,opcion):
        if opcion == 0:
            finn=Finn()
            finn.Set_imagenes(self._Builder.Get_sprites())
            finn.Set_imagedibu(self._Builder.Get_principal()) 
            self._personaje=finn
            return self._personaje
        elif opcion== 1:
            jake = Jake()
            jake.Set_imagenes(self._Builder.Get_sprites())
            jake.Set_imagedibu(self._Builder.Get_principal())
            self._personaje=jake
            return self._personaje
        elif opcion==2:
            bomberman = Bomberman()
            bomberman.Set_imagenes(self._Builder.Get_sprites())
            bomberman.Set_imagedibu(self._Builder.Get_principal())
            self._personaje=bomberman
            return self._personaje  
        elif opcion==3:
            link = Link()
            link.Set_imagenes(self._Builder.Get_sprites())
            link.Set_imagedibu(self._Builder.Get_principal())
            self._personaje=link
            return self._personaje 

         
        
            
class ConstructorPersonaje():
    def __init__(self,fabrica):
        self.fabrica=fabrica

    def Get_sprites(self):
        return[self.fabrica.Mover_derecha(), 
               self.fabrica.Mover_izquierda(),
               self.fabrica.Mover_arriba(), 
               self.fabrica.Mover_abajo()]   

    def Get_principal(self):
        return self.fabrica.Get_principal()

class Movimiento():
    
    def Move_Right(self):
        pass
    def Move_Left(self):
        pass    
    def Move_Up(self):
        pass
    def Move_Down(self):
        pass
    def Dibujar(self,screen):
        pass
    def Detener(self,screen):
        pass


class Finn(Movimiento):
     
    def __init__(self):
        self.posx=0
        self.posy=0
        self.imagenes=[]
        self.imageAc=None
        self.imagedibu=None
        self.contador =0  
        self.fila=0  
    
    def Set_imagedibu(self,image):
        self.imagedibu=image
    
    def Get_imagedibu(self):
        return self.imagedibu

    def Set_imagenes(self,imagenes):
        self.imagenes=imagenes

    def Get_imagenes(self):
        return self.imagenes     
    
    # Actualiza la imagenn corresponiente al movimiento que se realice
    def Actualizar(self):
        self.Set_ImageAc(self.Get_imagenes()[self.fila][self.contador])
        self.contador+=1
        self.contador%=len(self.Get_imagenes()[self.fila])
   
   #cdibuja la imagen correspondiente en la actual posicion
    def Dibujar(self,screen):
        self.screen= screen
        image= self.Get_imagedibu().subsurface(self.Get_ImageAc())
        self.screen.blit(image,(self.Get_posx(),self.Get_posy()))
    
    # dibuja una imagen cunado no hay movimiento en la ultima posicion que este se encuentra    
    
    def Detener(self, screen):
        self.screen=screen
        imagen =self.Get_imagedibu().subsurface(self.Get_imagenes()[3][0])
        self.screen.blit(imagen,(self.Get_posx(),self.Get_posy()))

    def Move_Right(self):
        self.posx+=5
        self.fila=0
        self.Actualizar()

    def Move_Left(self):
        self.posx-=5
        self.fila=1
        self.Actualizar()

    def Move_Up(self):
        self.posy-=5
        self.fila=2
        self.Actualizar()

    def Move_Down(self):
        self.posy+=5
        self.fila=3
        self.Actualizar()

    def Get_ImageAc(self):
        return self.imageAc

    def Set_ImageAc(self,imagen):
        self.imageAc=imagen
    
    def Get_posx(self):
        return self.posx
   
    def Get_posy(self):
        return self.posy

class Jake(Movimiento):
     
    def __init__(self):
        self.posx=0
        self.posy=0
        self.imagenes=[]
        self.imageAc=None
        self.imagedibu=None
        self.contador =0  
        self.fila=0  
    
    def Set_imagedibu(self,image):
        self.imagedibu=image
    
    def Get_imagedibu(self):
        return self.imagedibu

    def Set_imagenes(self,imagenes):
        self.imagenes=imagenes

    def Get_imagenes(self):
        return self.imagenes     
    
    # Actualiza la imagenn corresponiente al movimiento que se realice
    def Actualizar(self):
        self.Set_ImageAc(self.Get_imagenes()[self.fila][self.contador])
        self.contador+=1
        self.contador%=len(self.Get_imagenes()[self.fila])
   
   #cdibuja la imagen correspondiente en la actual posicion
    def Dibujar(self,screen):
        self.screen= screen
        image= self.Get_imagedibu().subsurface(self.Get_ImageAc())
        self.screen.blit(image,(self.Get_posx(),self.Get_posy()))
    
    # dibuja una imagen cunado no hay movimiento en la ultima posicion que este se encuentra    
    
    def Detener(self, screen):
        self.screen=screen
        imagen =self.Get_imagedibu().subsurface(self.Get_imagenes()[3][0])
        self.screen.blit(imagen,(self.Get_posx(),self.Get_posy()))

    def Move_Right(self):
        self.posx+=5
        self.fila=0
        self.Actualizar()

    def Move_Left(self):
        self.posx-=5
        self.fila=1
        self.Actualizar()

    def Move_Up(self):
        self.posy-=5
        self.fila=2
        self.Actualizar()

    def Move_Down(self):
        self.posy+=5
        self.fila=3
        self.Actualizar()

    def Get_ImageAc(self):
        return self.imageAc

    def Set_ImageAc(self,imagen):
        self.imageAc=imagen
    
    def Get_posx(self):
        return self.posx
   
    def Get_posy(self):
        return self.posy

class Bomberman(Movimiento):
     
    def __init__(self):
        self.posx=0
        self.posy=0
        self.imagenes=[]
        self.imageAc=None
        self.imagedibu=None
        self.contador =0  
        self.fila=0  
    
    def Set_imagedibu(self,image):
        self.imagedibu=image
    
    def Get_imagedibu(self):
        return self.imagedibu

    def Set_imagenes(self,imagenes):
        self.imagenes=imagenes

    def Get_imagenes(self):
        return self.imagenes     
    
    # Actualiza la imagenn corresponiente al movimiento que se realice
    def Actualizar(self):
        self.Set_ImageAc(self.Get_imagenes()[self.fila][self.contador])
        self.contador+=1
        self.contador%=len(self.Get_imagenes()[self.fila])
   
   #cdibuja la imagen correspondiente en la actual posicion
    def Dibujar(self,screen):
        self.screen= screen
        image= self.Get_imagedibu().subsurface(self.Get_ImageAc())
        self.screen.blit(image,(self.Get_posx(),self.Get_posy()))
    
    # dibuja una imagen cunado no hay movimiento en la ultima posicion que este se encuentra    
    
    def Detener(self, screen):
        self.screen=screen
        imagen =self.Get_imagedibu().subsurface(self.Get_imagenes()[3][1])
        self.screen.blit(imagen,(self.Get_posx(),self.Get_posy()))

    def Move_Right(self):
        self.posx+=5
        self.fila=0
        self.Actualizar()

    def Move_Left(self):
        self.posx-=5
        self.fila=1
        self.Actualizar()

    def Move_Up(self):
        self.posy-=5
        self.fila=2
        self.Actualizar()

    def Move_Down(self):
        self.posy+=5
        self.fila=3
        self.Actualizar()

    def Get_ImageAc(self):
        return self.imageAc

    def Set_ImageAc(self,imagen):
        self.imageAc=imagen
    
    def Get_posx(self):
        return self.posx
   
    def Get_posy(self):
        return self.posy
class Link(Movimiento):
     
    def __init__(self):
        self.posx=0
        self.posy=0
        self.imagenes=[]
        self.imageAc=None
        self.imagedibu=None
        self.contador =0  
        self.fila=0  
    
    def Set_imagedibu(self,image):
        self.imagedibu=image
    
    def Get_imagedibu(self):
        return self.imagedibu

    def Set_imagenes(self,imagenes):
        self.imagenes=imagenes

    def Get_imagenes(self):
        return self.imagenes     
    
    # Actualiza la imagenn corresponiente al movimiento que se realice
    def Actualizar(self):
        self.Set_ImageAc(self.Get_imagenes()[self.fila][self.contador])
        self.contador+=1
        self.contador%=len(self.Get_imagenes()[self.fila])
   
   #cdibuja la imagen correspondiente en la actual posicion
    def Dibujar(self,screen):
        self.screen= screen
        image= self.Get_imagedibu().subsurface(self.Get_ImageAc())
        self.screen.blit(image,(self.Get_posx(),self.Get_posy()))
    
    # dibuja una imagen cunado no hay movimiento en la ultima posicion que este se encuentra    
    
    def Detener(self, screen):
        self.screen=screen
        imagen =self.Get_imagedibu().subsurface(self.Get_imagenes()[3][0])
        self.screen.blit(imagen,(self.Get_posx(),self.Get_posy()))

    def Move_Right(self):
        self.posx+=5
        self.fila=0
        self.Actualizar()

    def Move_Left(self):
        self.posx-=5
        self.fila=1
        self.Actualizar()

    def Move_Up(self):
        self.posy-=5
        self.fila=2
        self.Actualizar()

    def Move_Down(self):
        self.posy+=5
        self.fila=3
        self.Actualizar()

    def Get_ImageAc(self):
        return self.imageAc

    def Set_ImageAc(self,imagen):
        self.imageAc=imagen
    
    def Get_posx(self):
        return self.posx
   
    def Get_posy(self):
        return self.posy
class util():
    def cargar_imagen(self,nombre):
        image=pygame.image.load(nombre)
        return image.convert()



