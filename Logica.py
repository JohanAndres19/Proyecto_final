from FabricasMov import *
import pygame
class Director():
    _Builder=None

    def set_builder(self,builder):
       self._Builder=builder

    def Get_personaje(self,opcion):
        if opcion ==1:
            finn=Finn()
            finn.Set_imagenes(self._Builder.Get_sprites())    
        return finn
        
            
class ConstructorPersonaje():
    def __init__(self,fabrica):
        self.fabrica=fabrica
    def Get_sprites(self):
        return[self.fabrica.Mover_derecha(), 
               self.fabrica.Mover_izquierda(),
               self.fabrica.Mover_arriba(), 
               self.fabrica.Mover_abajo()]   


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
        self.contador =0  
        self.fila=0  
    
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
        print(str(self.Get_ImageAc())," <- esta es lo que retorna")
        self.screen.blit(self.Get_ImageAc(),(self.Get_posx(),self.Get_posy()))
    
    # dibuja una imagen cunado no hay movimiento en la ultima posicion que este se encuentra    
    """
    def Detener(self, screen):
        self.screen=screen
        imagen=util().cargar_imagen("Imagenes/11.gif")
        self.screen.blit(imagen,(self.Get_posx(),140))
    """    
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



