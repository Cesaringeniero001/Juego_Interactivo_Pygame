import pygame
import random
import constantes

class Enemigo():
    def __init__(self):
        self.shape = pygame.Rect(random.randint(0, constantes.ANCHO_VENTANA - constantes.ANCHO_PERSONAJE),
                                 random.randint(0, constantes.ALTO_VETANA - constantes.ALTO_PERSONAJE),
                                 constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.direccion_x = random.choice([-1, 1])  
        self.direccion_y = random.choice([-1, 1])  

    def movimiento(self):
        self.shape.x += self.direccion_x * constantes.VELOCIDAD_ENEMIGO
        self.shape.y += self.direccion_y * constantes.VELOCIDAD_ENEMIGO

    
        if self.shape.left < 0 or self.shape.right > constantes.ANCHO_VENTANA:
            self.direccion_x *= -1
        if self.shape.top < 0 or self.shape.bottom > constantes.ALTO_VETANA:
            self.direccion_y *= -1

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes.COLOR_ENEMIGO, self.shape)
