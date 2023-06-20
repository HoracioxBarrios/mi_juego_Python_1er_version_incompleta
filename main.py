import pygame
import sys
from constantes import *
from personaje import *

pygame.init()



screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Db Z")
relog = pygame.time.Clock()

fondo = pygame.image.load("location\game_background_1.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
musica = pygame.mixer.music.load('sounds\intro_dbz.mp3')
jugador = Personaje(0, 0, 5, 8, 5, -15)

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
while(True):

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                jugador.control("caminar_r")
            if evento.key == pygame.K_LEFT :
                jugador.control("caminar_l")
            if evento.key == pygame.K_SPACE:
                jugador.control("saltar_r")
            if evento.key == pygame.K_SPACE:
                jugador.control("saltar_l")
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                jugador.control("quieto_r")
            if evento.key == pygame.K_LEFT:
                jugador.control("quieto_l")
              

    jugador.update_personaje()
    jugador.draw_personaje(screen)


    pygame.display.flip()     
    screen.blit(fondo, fondo.get_rect())



    delta_ms = relog.tick(FPS)

