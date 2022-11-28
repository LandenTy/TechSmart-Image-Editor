"""
Engine

Description: Base Tools for Image Editor
"""
# Libraries
from Colors import *

#PyGame
import pygame, sys
pygame.init()

# Window Variables
fps = 10
timer = pygame.time.Clock()
WIDTH, HEIGHT = 1000, 600

Load = False

# Painting Variables
active_size = 20
active_color = RED
painting = []

screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Images
Load_Image = pygame.image.load("ArrowIconDown.png")
Load_Image = pygame.transform.scale(Load_Image, (40, 40))

Save_Image = pygame.image.load("ArrowIconUp.png")
Save_Image = pygame.transform.scale(Save_Image, (40, 40))

Clear_Image = pygame.image.load("ArrowIconReset.png")
Clear_Image = pygame.transform.scale(Clear_Image, (40, 40))

# Draws Toolbar
def draw_menu():
    pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, WIDTH, 70))
    pygame.draw.line(screen, BLACK, (0, 70), (WIDTH, 70), 3)
    
    # Brush Sizes
    xl_brush = pygame.Rect(10, 10, 50, 50)
    pygame.draw.rect(screen, BLACK, xl_brush)
    pygame.draw.circle(screen, WHITE, (35, 35), 20)
    
    l_brush = pygame.Rect(70, 10, 50, 50)
    pygame.draw.rect(screen, BLACK, l_brush)
    pygame.draw.circle(screen, WHITE, (95, 35), 15)
    
    m_brush = pygame.Rect(130, 10, 50, 50)
    pygame.draw.rect(screen, BLACK, m_brush)
    pygame.draw.circle(screen, WHITE, (155, 35), 10)
    
    s_brush = pygame.Rect(190, 10, 50, 50)
    pygame.draw.rect(screen, BLACK, s_brush)
    pygame.draw.circle(screen, WHITE, (215, 35), 5)
    
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    
    # Color Pallette
    red = pygame.Rect(WIDTH - 35, 10, 25, 25)
    white = pygame.Rect(WIDTH - 35, 37, 25, 25)
    orange = pygame.Rect(WIDTH - 62, 10, 25, 25)
    yellow = pygame.Rect(WIDTH - 62, 37, 25, 25)
    green = pygame.Rect(WIDTH - 89, 10, 25, 25)
    blue = pygame.Rect(WIDTH - 89, 37, 25, 25)
    indigo = pygame.Rect(WIDTH - 116, 10, 25, 25)
    violet = pygame.Rect(WIDTH - 116, 37, 25, 25)
    
    pygame.draw.rect(screen, RED, red)
    pygame.draw.rect(screen, CLOUDY_WHITE, white)
    pygame.draw.rect(screen, ORANGE, orange)
    pygame.draw.rect(screen, YELLOW, yellow)
    pygame.draw.rect(screen, GREEN, green)
    pygame.draw.rect(screen, BLUE, blue)
    pygame.draw.rect(screen, INDIGO, indigo)
    pygame.draw.rect(screen, VIOLET, violet)
    
    # Load Button
    Load_Button = pygame.Rect(WIDTH - 350, 15, 40, 40)
    pygame.draw.rect(screen, WHITE, Load_Button)
    screen.blit(Load_Image, (WIDTH-350,15))
    
    # Save Button
    Save_Button = pygame.Rect(WIDTH - 305, 15, 40, 40)
    pygame.draw.rect(screen, WHITE, Save_Button)
    screen.blit(Save_Image, (WIDTH-305,15))
    
    # Clear Button
    Clear_Button = pygame.Rect(WIDTH - 260, 15, 40, 40)
    pygame.draw.rect(screen, WHITE, Clear_Button)
    screen.blit(Clear_Image, (WIDTH-260,15))
    
    # Input Field
    inputBox = pygame.Rect(int((WIDTH/2) - 225), 10, 250, 50)
    pygame.draw.rect(screen, (120, 120, 120), inputBox)
    pygame.draw.rect(screen, (90,90,90) , inputBox, 3)
    
    # Saving Lists
    color_rect = [red, white, orange, yellow, green, blue, indigo, violet]
    rgb_list = [RED, CLOUDY_WHITE, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
    save_buttons = [Load_Button, Save_Button, Clear_Button]
    
    return brush_list, color_rect, rgb_list, save_buttons, inputBox

# Draws Saved Image
def draw_painting(paint):
    
    for i in range(len(paint)):
        pygame.draw.circle(screen, paint[i][0], paint[i][1], paint[i][2])

# Clears Canvas (Mostly Working)
def Clear_Screen():
    painting = []
    screen.fill(WHITE)

# Loads Previously Saved Drawing
def Load_Saved_Painting(file):
    
    with open(file, 'r') as f:
        painting = eval('[' + ''.join(f.readlines()) + ']') 
        draw_painting(painting)

# Saves Artwork into TXT File
def Save_Painting(painting):
    
    with open('SaveData.txt', 'w') as f:
        for index in painting:
            f.write(''.join(str(index) + ','))
