import pygame
import constantes
from personaje import Personaje
from enemigo import Enemigo



# Función para crear enemigos según la cantidad especificada por el jugador
def crear_enemigos(cantidad):
    enemigos = []
    for _ in range(cantidad):
        enemigo = Enemigo()
        enemigos.append(enemigo)
    return enemigos


def mostrar_menu():
    print("BIENVENIDO AL JUEGO DE LA ATRAPAME SI PUEDES!!! \n" 
          
           "DEBES SER ESTRATÉGICO Y MOVERTE CON CUIDADO \n"
           "INTENTA NO DEJARTE ATRAPAR POR NINGÚN ENEMIGO \n"
           "MUCHA SUERTE AMIGOOO !!!!!")
    cantidad_enemigos = 0
    while cantidad_enemigos <= 0:
        try:
            cantidad_enemigos = int(input("Ingrese la cantidad de enemigos que desea crear: "))
            if cantidad_enemigos <= 0:
                print("La cantidad de enemigos debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número entero.")

    return cantidad_enemigos

pygame.init()

jugador = Personaje(100, 100)
cantidad_enemigos = mostrar_menu()
enemigos = crear_enemigos(cantidad_enemigos)

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VETANA))


pygame.display.set_caption("Juego") 


mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()

run = True
while run:
    
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_FONDO)
    jugador.dibujar(ventana)

    

    delta_x = 0
    delta_y = 0

    if mover_arriba == True:
        delta_y= -constantes.VELOCIDAD

    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    if mover_derecha == True:
        delta_x= constantes.VELOCIDAD

    if mover_izquierda == True:
        delta_x= -constantes.VELOCIDAD     


    jugador.movimiento(delta_x, delta_y)

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True

            if event.key == pygame.K_d:
                mover_derecha = True            

            if event.key == pygame.K_w:
                mover_arriba = True 

            if event.key == pygame.K_s:
                mover_abajo = True        


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                mover_izquierda = False

            if event.key == pygame.K_d:
                mover_derecha =False      

            if event.key == pygame.K_w:
                mover_arriba = False

            if event.key == pygame.K_s:
                mover_abajo = False        
    
    for enemigo in enemigos:
        enemigo.movimiento()
        enemigo.dibujar(ventana)

        if jugador.shape.colliderect(enemigo.shape):
            print("¡Has perdido!")
            run = False
    pygame.display.update()


pygame.quit()            