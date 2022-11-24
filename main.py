import pygame as pg

pg.init()

#creamos una pantalla o surface
pantalla_principal = pg.display.set_mode((800, 600)) #tamaño ventana
pg.display.set_caption("Bolillas Rebotando") #título de la ventana

game_over = False
#contador = 0
x = 400
y = 300
vx = 1
vy = 1

while not game_over: #bucle para ejecutar los fotoramas para el repintado de pantalla

    for eventos in pg.event.get(): #captura los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT: 
            game_over == True

    pantalla_principal.fill((52, 152, 219)) #asignar un color a la pantalla
    x += vx
    y += vy
    if x >= 800 or x == 0: #para que llegue a los limites
        vx *= -1
    if y >= 600 or y == 0:
        vy *= -1

                #la surface o pantalla #color RGB   #posición(Posición Ancho, Posición Largo, tamaño del rectangulo Largo, tamaño Alto)
    pg.draw.rect(pantalla_principal, (192, 57, 43), (x, y, 20, 20)) #Método para dibujar un rectángulo

    pg.display.flip() #adjunta a la pantalla los parámetros

    #contador += 1
    #print(f"pintando el fotograma número:  {contador}")

pg.quit()