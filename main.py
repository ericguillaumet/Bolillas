import pygame as pg
from class_figura import Rectangulo, Bolillas
from all_inclusive_class import Figura
import random

pg.init()

pantalla_principal = pg.display.set_mode((800, 600)) 
pg.display.set_caption("Bolillas Rebotando") 

game_over = False

lista_bolas = []

for i in range(1, 101):

    lista_bolas.append(Figura(random.randint(0, 800), random.randint(0, 600), color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)), radio = random.randint(5, 30)))

while not game_over: 

    for eventos in pg.event.get(): 
        print(eventos)
        if eventos.type == pg.QUIT: 
            game_over = True

    pantalla_principal.fill((52, 152, 219)) 

    for bolilla in lista_bolas:
        bolilla.move_circle(800, 600)
        bolilla.draw_circle(pantalla_principal)

    pg.display.flip() 

pg.quit()