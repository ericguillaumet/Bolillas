import pygame as pg

pg.init()

#creamos una pantalla o surface
pantalla_principal = pg.display.set_mode((800, 600)) #tamaño ventana
pg.display.set_caption("Bolillas Rebotando") #título de la ventana

game_over = False
#contador = 0

x = 390
y = 290
vx = 1 #velocidad 
vy = 1

x2 = 290
y2 = 190
vx2 = 1
vy2 = 1

#variable para controlar el bucle

while not game_over: #bucle para ejecutar los fotoramas para el repintado de pantalla

    for eventos in pg.event.get(): #captura los eventos de pygame en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT: #Si no hay evento, entra en True
            game_over = True

    pantalla_principal.fill((52, 152, 219)) #asignar un color a la pantalla
    
    x += vx
    y += vy

    x2 += vx2
    y2 += vy2

    if x >= 780 or x == 0: #para que llegue a los limites, 800 el principio y 0 el borde
        vx *= -1 # -1 ya que si llega al límite, hacer lo contrario
    if y >= 580 or y == 0:
        vy *= -1

    if x2 >= 780 or x2 <= 0:
        vx2 *= -1
    if y2 >= 580 or y2 <= 0:
        vy2 *= -1

                #la surface o pantalla #color RGB   #posición(Posición Ancho, Posición Largo, tamaño del rectangulo Largo, tamaño Alto)
    pg.draw.rect(pantalla_principal, (192, 57, 43), (x, y, 20, 20)) #Método para dibujar un rectángulo // rojo
    pg.draw.rect(pantalla_principal, (255, 255, 0),(x2, y2, 20, 20)) #Método para dibujar un rectangulo // 
    """
    pg.draw.circle(pantalla_principal, bola1.color, (bola1.pos_x, bola1.pos_y), bola1.radio)
    pg.draw.circle(pantalla_principal, bola2.color, (bola2.pos_x, bola2.pos_y), bola2.radio)
    
    """
    pg.display.flip() #adjunta a la pantalla los parámetros

    #contador += 1
    #print(f"pintando el fotograma número:  {contador}")

pg.quit()