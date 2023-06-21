import pygame
import asyncio
def get_surface_form_sprite_sheet(path, columnas, filas, cortar_en_fila : int, cortar_columna_desde = 0, cortar_columna_hasta = 0, flip= False):
    lista = []
    superficie_imagen = pygame.image.load(path)

    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)
    
    for columna in range(cortar_columna_desde, cortar_columna_hasta):
        for fila in range(filas):
            x = fotograma_ancho * columna
            y = fotograma_alto * cortar_en_fila
            superficie_fotograma =  superficie_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
            # superficie_fotograma = pygame.transform.scale(superficie_fotograma, (fotograma_ancho * 3, fotograma_alto * 3))
            if flip:
                superficie_fotograma = pygame.transform.flip(superficie_fotograma, True, False)
            lista.append(superficie_fotograma)
    
    return lista

def obtener_rectangulos_colision(rectangulo_principal: pygame.Rect):
    dicc_rectangulos_lados= {}
    dicc_rectangulos_lados["lado_abajo"]: dict[pygame.Rect] = pygame.Rect(rectangulo_principal.left, rectangulo_principal.bottom -10, rectangulo_principal.width, 10)
    dicc_rectangulos_lados["lado_derecha"]: dict[pygame.Rect] = pygame.Rect(rectangulo_principal.right -2, rectangulo_principal.top,  2, rectangulo_principal.height)
    dicc_rectangulos_lados["lado_izquierda"]: dict[pygame.Rect] = pygame.Rect(rectangulo_principal.left, rectangulo_principal.top, 2, rectangulo_principal.height)
    dicc_rectangulos_lados["lado_arriba"]: dict[pygame.Rect] = pygame.Rect(rectangulo_principal.left, rectangulo_principal.top, rectangulo_principal.width, 10)
    return dicc_rectangulos_lados

def obtener_ractangulo_principal(superficies, frame):
    animaciones = []
    animaciones = superficies
    imagen = animaciones[frame]
    rectangulo_principal = imagen.get_rect()
    return rectangulo_principal 

async def animationControler(times: list[int], frame: int):
    for time in times:
        asyncio.sleep(time)