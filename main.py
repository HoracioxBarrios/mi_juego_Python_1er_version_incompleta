import pygame, sys
from clase_boton import Button
from configuracion import *
from level_1 import *
from pyvidplayer import Video

pygame.init()


SCREEN = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menu")

background_main = pygame.image.load("assets\Backgroung_guku_chico.jpg")
background_main_rescalado = pygame.transform.scale(background_main,(ANCHO,ALTO))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        level_1()
        #---------------------
                
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(20).render("Estas en la pantalla de Opciones", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(ANCHO/2, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(ANCHO/2, 460), 
                            text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.mixer.music.load('sounds\intro_dbz.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    while True:
        SCREEN.blit(background_main_rescalado,(0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("Dragon Ball Sprite", True, "#E74C3C")
        MENU_RECT = MENU_TEXT.get_rect(center=(ANCHO /2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(ANCHO /2, 200), 
                            text_input="PLAY", font=get_font(20), base_color="#2874A6", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(ANCHO /2, 350), 
                            text_input="OPTIONS", font=get_font(20), base_color="#2874A6", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(ANCHO /2, 500), 
                            text_input="QUIT", font=get_font(20), base_color="#2874A6", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def intro():
    
    vid = Video("assets/video_corto.mp4")
    vid.set_size((ANCHO, ALTO))
    
    while True:
        #donde corre el video
        
        if vid.active == True: # si es true cirre ek video
            vid.draw(SCREEN, (0, 0)) 
        else:
            vid.close()
            main_menu()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                #llamada a main menu ()
                main_menu()



intro()