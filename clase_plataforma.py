import pygame
from utilidades import *

class Plataforma:
    def __init__(self, path, x, y):
        self.lista_plataforma_superficie = get_surface_form_sprite_sheet(path, 1,1,0,0,1, False)
        self.pos_init_x = x
        self.pos_init_y = y
        self.frame = 0

        self.lista_animacion = self.lista_piso_superficie
        self.imagen_superficie = self.lista_animacion[self.frame]
        self.rectangulo_principal = self.imagen_superficie.get_rect()
        self.rectangulo_principal.x = x
        self.rectangulo_principal.y = y
        self.dicc_rectangulo_y_sub_rectangulos_col = obtener_rectangulos_colision(self.rectangulo_principal)