import pygame
import sys
from pygame.locals import *
from Logica import *
from FabricasMov import *
"""
class Controlador():
   def __init__(self):
        self.teclas=pygame.key.get_pressed()
        self
    
   def Tecla_precionada(self,personaje):
        if self.teclas[K_RIGHT]:
            self.personaje.Move_Right()
            self.personaje.Dibujar(self.screen)
        elif self.teclas[K_LEFT]:
            self.movimiento = self.teclas[K_LEFT]
            self.personaje.Move_Left()
            self.personaje.Dibujar(self.screen)
        elif self.teclas[K_UP]:
            self.movimiento = self.teclas[K_UP]
            self.personaje.Move_Up()
            self.personaje.Dibujar(self.screen)
        elif self.teclas[K_DOWN]:
            self.movimiento = self.teclas[K_DOWN]
            self.personaje.Move_Down() 
            self.personaje.Dibujar(self.screen)       
        else:
            self.personaje.Detener(self.screen)

"""

class Modelo():
    # constructor  Inicializa la ventana y el director para poder obtener el personaje que 
    # se solicite
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((910,616))
        pygame.display.set_caption("Animacion")
        self.director = Director()
        self.ejecuntado=True
        self.mov=0
        self.director.set_builder(ConstructorPersonaje(FabricaLink()))
        self.personaje = self.director.Get_personaje()
        self.Ventana()
  # metodo que dibuja el personaje que se selecciona y lo anima 
    def Dibujar(self):
        self.background_image= util().cargar_imagen("Sprites/Mapa4.jpg")
        self.screen.blit(self.background_image,(0,0))
        self.teclas=pygame.key.get_pressed() 
        if self.teclas[K_RIGHT]:
            self.personaje.Move_Right()
            self.personaje.Dibujar(self.screen)
        elif self.teclas[K_LEFT]:
            self.movimiento = self.teclas[K_LEFT]
            self.personaje.Move_Left()
            self.personaje.Dibujar(self.screen)
        elif self.teclas[K_UP]:
            self.movimiento = self.teclas[K_UP]
            self.personaje.Move_Up()
            self.personaje.Dibujar(self.screen)
        elif self.teclas[K_DOWN]:
            self.movimiento = self.teclas[K_DOWN]
            self.personaje.Move_Down() 
            self.personaje.Dibujar(self.screen)       
        else:
            self.personaje.Detener(self.screen)
    
    # metodo que mantiene la ventana activa y realiza la llamada continua del metodo dibujar  
    def Ventana(self):
        while self.ejecuntado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ejecuntado=False
                    sys.exit() 
            self.Dibujar()
            pygame.display.update()
            pygame.time.delay(90) 




if __name__ == "__main__":
    Modelo()