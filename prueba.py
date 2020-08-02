import pygame
import sys
#si se ve  
#si
#breves 
#parce por donde empezamos 
#estoy en el chat
#ok ya  voy


pygame.init()
pygame.display.set_mode((500,500))
pygame.display.set_caption("prueba")
salir=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             salir=True
    pygame.display.update()
pygame.quit()

print("prueba343443")
