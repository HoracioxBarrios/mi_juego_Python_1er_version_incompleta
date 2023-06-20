import pygame
from utilidades import *

class Personaje:
    def __init__(self, x, y, speed_caminar, speed_correr, gravedad, salta_y) -> None:
        self.caminar_r = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 6, False)
        self.caminar_l = get_surface_form_sprite_sheet("sprites\goku.png", 4, 4, 2 , 0, True)
        self.quieto_r = get_surface_form_sprite_sheet("sprites\goku.png", 4, 4, 2, 0, False)
        self.quieto_l = get_surface_form_sprite_sheet("sprites\goku.png", 4, 4, 2, 0, True)
        self.saltar_r = get_surface_form_sprite_sheet("sprites\goku.png", 4, 4, 2, 0, False)
        self.saltar_l = get_surface_form_sprite_sheet("sprites\goku.png", 4, 4, 2, 0, True)
        self.frame = 0
        self.vidas = 3
        self.puntuacion = 0
        self.mover_x = x
        self.mover_y = y
        self.jugador_mirando_derecha = True
        self.jugador_mirando_izquierda = False
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
            self.en_aire = False
            self.mover_y = 0

        self.rectangulo.x += self.mover_x
        self.rectangulo.y += self.mover_y
            
        if self.rectangulo.y < 650:
            self.en_aire = True
            self.rectangulo.y += self.gravedad
            print(self.rectangulo.y)
       
    def control(self, accion):
        if accion == "caminar_r" and self.en_aire == False:
            self.mover_x = self.speed_caminar
            self.animacion = self.caminar_r
            self.frame = 0
            self.jugador_mirando_derecha = True
            self.jugador_mirando_izquierda = False
            print(self.caminar_r)
        elif accion == "caminar_l" and self.en_aire == False:
            self.mover_x = -self.speed_caminar
            self.animacion = self.caminar_l
            self.frame = 0
            self.jugador_mirando_izquierda = True
            self.jugador_mirando_derecha = False
        elif accion == "quieto_r":
            self.mover_x = 0
            self.mover_y = 0
            self.animacion = self.quieto_r
            self.frame = 0
            self.jugador_mirando_derecha = True
            self.jugador_mirando_izquierda = False
            print('derecha', self.jugador_mirando_derecha)
        elif accion == "quieto_l":
            self.mover_x = 0
            self.mover_y = 0
            self.animacion = self.quieto_l
            self.frame = 0
            self.jugador_mirando_izquierda = True
            self.jugador_mirando_derecha = False
            print('izquierda',self.jugador_mirando_izquierda)
        elif accion == "saltar_r" and self.en_aire == False:
            self.mover_y = self.salta_y
            if(self.jugador_mirando_derecha):
                self.animacion = self.saltar_r
            else:
                self.animacion = self.saltar_l
            self.frame = 0
            self.en_aire = True
        elif accion == "saltar_l" and self.en_aire == False:
            self.mover_y = self.salta_y
            self.animacion = self.saltar_l
            self.frame = 0
            self.en_aire = True
        


    def draw_personaje(self, screen):
        self.imagen = self.animacion[self.frame]
        # self.rectangulo = self.imagen.get_rect()
        screen.blit(self.imagen, self.rectangulo)


