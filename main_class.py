import pygame as pg
from class_figura import Rectangulo, Bolillas

pg.init()

pantalla_principal = pg.display.set_mode((800, 600)) 
pg.display.set_caption("Bolillas Rebotando") 

game_over = False

rect1 = Rectangulo(400, 300)
rect2 = Rectangulo(300, 200, color = (192, 57, 43))

bola1 = Bolillas(300, 200)
bola2 = Bolillas(100, 50, color = (192, 57, 43))

while not game_over: 

    for eventos in pg.event.get(): 
        print(eventos)
        if eventos.type == pg.QUIT: 
            game_over = True

    pantalla_principal.fill((52, 152, 219)) 
    
    rect1.movimiento(800, 600)
    rect2.movimiento(800, 600)

    rect1.draw(pantalla_principal)
    rect2.draw(pantalla_principal)
    
    bola1.movimiento(800, 600)
    bola2.movimiento(800, 600)

    bola1.draw(pantalla_principal)
    bola2.draw(pantalla_principal)

    pg.display.flip() 

pg.quit()