"""
ImageViewer

Description: Let's User View images for use in other projects. This
module will be duplicated for later use in other projects.
"""
# Libraries
import pygame
pygame.init()

# Draws Painting to Screen
def draw_painting(screen, paint):
    
    for i in range(len(paint)):
        pygame.draw.circle(screen, paint[i][0], paint[i][1], paint[i][2])

# Loads Previously Saved Drawing
def Load_Saved_Painting(screen, file):
    
    with open(file, 'r') as f:
        painting = eval('[' + ''.join(f.readlines()) + ']') 
        draw_painting(screen, painting)
