"""
ImageEditor

Description: Tool that lets you Create and Edit SVG Vector Images
"""
# Libraries
from Colors import *
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
    
    # Saving Lists
    color_rect = [red, white, orange, yellow, green, blue, indigo, violet]
    rgb_list = [RED, CLOUDY_WHITE, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
    save_buttons = [Load_Button, Save_Button, Clear_Button]
    
    return brush_list, color_rect, rgb_list, save_buttons

# Draws Saved Image
def draw_painting(paint):
    
    for i in range(len(paint)):
        pygame.draw.circle(screen, paint[i][0], paint[i][1], paint[i][2])

# Clears Canvas (Mostly Working)
def Clear_Screen():
    painting = []
    screen.fill(WHITE)

# Loads Previously Saved Drawing
def Load_Saved_Painting():
    
    with open('SaveData.txt', 'r') as f:
        painting = eval('[' + ''.join(f.readlines()) + ']') 
        draw_painting(painting)

# Saves Artwork into TXT File
def Save_Painting(painting):
    
    with open('SaveData.txt', 'w') as f:
        for index in painting:
            f.write(''.join(str(index) + ','))

run = True
while run:
    timer.tick(fps)
    screen.fill(WHITE)
    
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)
        
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))
    
    draw_painting(painting)
    
    brushes, colors, rgb, saveLoad = draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Toolbar Buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgb[i]
            
            # Load Button
            for i in range(len(saveLoad)):
                if saveLoad[i].collidepoint(event.pos):
                    
                    if i == 0:
                        Load = True
                        
                    if i == 1:
                        Load = False
                        Save_Painting(painting)
                    
                    if i == 2:
                        Load = False
                        Clear_Screen()
    if Load:
        Load_Saved_Painting()
        
    pygame.display.flip()
    
sys.exit()
