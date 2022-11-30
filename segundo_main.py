import pygame as pg
from class_figura import Rectangulo, Bolillas
import random

pg.init()

pantalla_principal = pg.display.set_mode((800, 600)) 
pg.display.set_caption("Bolillas Rebotando") 

game_over = False
"""
rect1 = Rectangulo(random.randint(0, 800),random.randint(0, 600), w = random.randint(10, 40), h = random.randint(10, 40))
rect2 = Rectangulo(random.randint(0, 800), random.randint(0, 600), color = (192, 57, 43), w = random.randint(10, 40), h = random.randint(10, 40))
"""
lista_bolas = []

for i in range(1, 101):

    lista_bolas.append(Bolillas(random.randint(0, 800), random.randint(0, 600), color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)), radio = random.randint(5, 30)))

    #bola1 = Bolillas(random.randint(0, 800), random.randint(0, 600), radio = random.randint(10, 40))
    #bola2 = Bolillas(random.randint(0, 800), random.randint(0, 600), color = (192, 57, 43), radio = random.randint(10, 40))

while not game_over: 

    for eventos in pg.event.get(): 
        print(eventos)
        if eventos.type == pg.QUIT: 
            game_over = True

    pantalla_principal.fill((52, 152, 219)) 

    for bolilla in lista_bolas:
        bolilla.movimiento(800, 600)
        bolilla.draw(pantalla_principal)

    """
    rect1.movimiento(800, 600)
    rect2.movimiento(800, 600)

    rect1.draw(pantalla_principal)
    rect2.draw(pantalla_principal)
    
    bola1.movimiento(800, 600)
    bola2.movimiento(800, 600)

    bola1.draw(pantalla_principal)
    bola2.draw(pantalla_principal)
    """
    pg.display.flip() 

pg.quit()