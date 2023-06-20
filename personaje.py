import pygame
from utilidades import *

class Personaje:
    def __init__(self, x, y, speed_caminar, speed_correr, gravedad, salta_y) -> None:
        self.caminar_r = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 6, 8,False)
        self.caminar_l = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0 , 6, 8,True)
        self.quieto_r = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 0, 2, True)
        self.quieto_l = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 0, 2, False)
        self.saltar_r = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 6, 7, False)
        self.saltar_l = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 6, 7, True)
        self.frame = 0
        self.vidas = 3
        self.puntuacion = 0
        self.mover_x = x
        self.mover_y = y
        self.jugador_quieto_derecha = True
        self.jugador_quieto_izquierda = False
        self.jugador_corriendo_derecha = False
        self.jugador_corriendo_izquierda = False
        self.salta_y = salta_y
        self.speed_caminar = speed_caminar
        self.speed_correr = speed_correr
        self.gravedad = gravedad
        self.en_aire = False
        
        self.animacion = self.quieto_r
        self.imagen = self.animacion[self.frame]
        self.rectangulo = self.imagen.get_rect()
    def update_personaje(self):
        
        if(self.frame < len(self.animacion) -1):
            self.frame += 1
        else:
            self.frame = 0
            self.mover_y = 0
            self.en_aire = False
            
        self.rectangulo.x += self.mover_x
        self.rectangulo.y += self.mover_y
        #controla si el personaje esta en el aire o llego al piso   
        if self.rectangulo.y < 650:
            self.en_aire = True
            self.rectangulo.y += self.gravedad
            if(self.jugador_quieto_derecha):
                self.animacion = self.saltar_r
            elif(self.jugador_quieto_izquierda):
                self.animacion = self.saltar_l
        else:
            self.en_aire = False
            if(self.jugador_corriendo_derecha):
                self.animacion = self.caminar_r
            elif(self.jugador_corriendo_izquierda):
                self.animacion = self.caminar_l
            elif(self.jugador_quieto_derecha):
                self.animacion = self.quieto_r
            else:
                self.animacion = self.quieto_l
            print('llego a cero')

            
    def control(self, accion):
        #Caminar R
        if accion == "caminar_r" and self.en_aire == False:
            self.mover_x = self.speed_caminar
            self.animacion = self.caminar_r
            self.frame = 0
            self.setFlagsDarseVuelta(True)
        #Caminar L
        elif accion == "caminar_l" and self.en_aire == False:
            self.mover_x = -self.speed_caminar
            self.animacion = self.caminar_l
            self.frame = 0
            self.setFlagsDarseVuelta(False)
        
        #Quieto
        elif accion == "quieto":
            self.jugador_corriendo_izquierda = False
            self.jugador_corriendo_derecha = False
            self.mover_x = 0
            self.mover_y = 0
            if(self.jugador_quieto_derecha):
                self.animacion = self.quieto_r
            else:
                self.animacion = self.quieto_l
            self.frame = 0
            
        #Saltar
        elif accion == "saltar" and self.en_aire == False:
            if(self.jugador_quieto_derecha):
                self.animacion = self.saltar_r
            else:
                self.animacion = self.saltar_l
            self.mover_y = self.salta_y
            self.frame = 0
            self.en_aire = True
        
    #funcion para controlar el lado al que corre y mira
    def setFlagsDarseVuelta(self, flag):
        self.jugador_corriendo_derecha = flag
        self.jugador_quieto_derecha = self.jugador_corriendo_derecha

        self.jugador_corriendo_izquierda = not self.jugador_corriendo_derecha
        self.jugador_quieto_izquierda = self.jugador_corriendo_izquierda

    def draw_personaje(self, screen):
        self.imagen = self.animacion[self.frame]
        # self.rectangulo = self.imagen.get_rect()
        screen.blit(self.imagen, self.rectangulo)


