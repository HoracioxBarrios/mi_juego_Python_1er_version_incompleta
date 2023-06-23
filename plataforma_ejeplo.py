import pygame, sys
from pygame.locals import *
pygame.init()
#https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu
#https://freesound.org
#https://kenney.nl/assets/platformer-art-deluxe
WHITE = (255, 255, 255)

tile_size = 200
cols = 20
margin = 100
screen_width = 1000
screen_heigth = 1000

screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("Plataforma")

#Cargar imagenes

bg_img = pygame.image.load("location\game_background_1.png")
sun_img = pygame.image.load("sprites\StoneBlock.png")

def draw_grid():
    #Dibuja una cuadricula en la pantalla
    
	for c in range(21):
		#vertical lines
		pygame.draw.line(screen, WHITE, (c * tile_size, 0), (c * tile_size, screen_heigth - margin))
		#horizontal lines
		pygame.draw.line(screen, WHITE, (0, c * tile_size), (screen_width, c * tile_size))

class World:
    def __init__(self, data : list[list]) -> None:
        self.tile_list = []
        bloque_img = pygame.image.load("sprites/block.png")
        agua_img = pygame.image.load("sprites/agua.png")
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(bloque_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                if tile == 2:
                    img = pygame.transform.scale(agua_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                col_count += 1
            row_count += 1
            
            
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], (tile[1])) # aca esta la screen , y la tupla de coordenadas ya que tile tiene esos valores.

world_data = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 2, 2, 2, 1]
]
    


#instaciar mundo

world = World(world_data)



while True:
    
    
    
    
    screen.blit(bg_img,(0, 0))# fondo
    screen.blit(sun_img, (100, 100)) #sol
    
    
    draw_grid()
    world.draw()
    # print(world.tile_list)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    pygame.display.update()
    
    
