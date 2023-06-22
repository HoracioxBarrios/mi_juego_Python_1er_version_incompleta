import pygame
from utilidades import *
from piso import *
import time

class Personaje:
    def __init__(self, x, y, speed_caminar, speed_correr, gravedad, potencia_salto) -> None:
        self.caminar_r = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 6, 8,False)
        self.caminar_l = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0 , 6, 8,True)
        self.quieto_r = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 0, 2, True)
        self.quieto_l = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 0, 2, False)
        self.saltar_r = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 6, 7, False)
        self.saltar_l = get_surface_form_sprite_sheet("sprites\goku2.png", 9, 6, 0, 6, 7, True)
        self.frame = 0
        self.vidas = 3
        self.puntuacion = 0

        self.velocidad_x = speed_caminar

        self.desplazamiento_y = 0
        self.limite_velocidad_caida = 15
        self.potencia_salto = potencia_salto
        self.gravedad = gravedad
        

        self.jugador_quieto_derecha = True
        self.jugador_quieto_izquierda = False
        self.jugador_corriendo_derecha = False
        self.jugador_corriendo_izquierda = False
        self.speed_caminar = speed_caminar
        self.speed_correr = speed_correr
        ##############################
        self.times = [20,2,2]
        self.en_aire = True
        self.index = 0
        self.cont = self.times[self.index] 
        self.lenTimes = len(self.times)    
        #Creacion inicial del rectangulo con superficie
        self.animacion = self.quieto_r
        self.imagen = self.animacion[self.frame]
        self.rectangulo_principal = self.imagen.get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.colisiones_rectangulo_princial: dict[pygame.Rect] = obtener_rectangulos_colision(self.rectangulo_principal)
        print(self.colisiones_rectangulo_princial)
        
    def update_personaje(self, pisos: list[Piso]):
        for piso in pisos:
            if not self.en_aire and self.colisiones_rectangulo_princial["lado_abajo"].colliderect(piso.colisiones_rectangulo_princial["lado_arriba"]):
                self.rectangulo_principal.x += self.velocidad_x
                for lado in self.colisiones_rectangulo_princial:
                        self.colisiones_rectangulo_princial[lado].x += self.velocidad_x
            else:
                self.en_aire = True
        self.aplicar_gravedad(pisos)
            
    def control(self, accion):
        #Caminar R
        if accion == "caminar_r" and self.en_aire == False:
            self.velocidad_x = self.speed_caminar
            self.animacion = self.caminar_r
            self.frame = 0
            self.setFlagsDarseVuelta(True)
        #Caminar L
        elif accion == "caminar_l" and self.en_aire == False:
            self.velocidad_x = -self.speed_caminar
            self.animacion = self.caminar_l
            self.frame = 0
            self.setFlagsDarseVuelta(False)
        
        #Quieto
        elif accion == "quieto":
            self.jugador_corriendo_izquierda = False
            self.jugador_corriendo_derecha = False
            self.velocidad_x = 0
            self.desplazamiento_y = 0
            if(self.jugador_quieto_derecha):
                self.animacion = self.quieto_r
            else:
                self.animacion = self.quieto_l
            self.frame = 0
            
        #Saltar
        elif accion == "saltar" and self.en_aire == False:
            self.en_aire = True
            if(self.jugador_quieto_derecha):
                self.animacion = self.saltar_r
            else:
                self.animacion = self.saltar_l

            self.desplazamiento_y = self.potencia_salto
            self.frame = 0
            
        
    def controlar_animacion_en_aire(self):
        if(self.jugador_quieto_derecha):
            self.animacion = self.saltar_r
        elif(self.jugador_quieto_izquierda):
            self.animacion = self.saltar_l
    def controlar_animacion_an_piso(self):
        if(self.jugador_corriendo_derecha):
            self.animacion = self.caminar_r
        elif(self.jugador_corriendo_izquierda):
            self.animacion = self.caminar_l
        elif(self.jugador_quieto_derecha):
            self.animacion = self.quieto_r
        else:
            self.animacion = self.quieto_l

    #funcion para controlar el lado al que corre y mira
    def setFlagsDarseVuelta(self, flag):

        self.jugador_corriendo_derecha = flag
        self.jugador_quieto_derecha = self.jugador_corriendo_derecha

        self.jugador_corriendo_izquierda = not self.jugador_corriendo_derecha
        self.jugador_quieto_izquierda = self.jugador_corriendo_izquierda

    def draw_personaje(self, screen, pisos:list[Piso]):
        
        self.animacion_controller()
        screen.blit(self.imagen, self.rectangulo_principal)
        for piso in pisos:
            screen.blit(piso.imagen, piso.rectangulo_principal)
   
    def animacion_controller(self):
        if(self.cont == 0):
            if(self.frame < len(self.animacion) -1):
                self.frame += 1
                self.imagen = self.animacion[self.frame]
                if(self.index < self.lenTimes -1):
                    self.index += 1
                    self.cont = self.times[self.index]
                else:
                    self.index = 0 
            else:
                self.frame = 0
        else:
            print(self.cont)
            print(self.index)
            self.cont -= 1
    def aplicar_gravedad(self, pisos: list[Piso]):
        if self.en_aire:
            self.rectangulo_principal.y += self.desplazamiento_y
            for lado in self.colisiones_rectangulo_princial:
                self.colisiones_rectangulo_princial[lado].y += self.desplazamiento_y


            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
            self.chaquear_colision_pisos(pisos)

    def chaquear_colision_pisos(self, list_pisos: list[Piso]):
        for piso in list_pisos:
            if self.colisiones_rectangulo_princial["lado_abajo"].colliderect(piso.colisiones_rectangulo_princial["lado_arriba"]):
                self.desplazamiento_y = 0
                self.en_aire = False
                self.rectangulo_principal.bottom = piso.rectangulo_principal.top


