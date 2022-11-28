"""
Demo

Description: Basic demo scenario to show an example of
how you could use the tool in a project space.
"""
# Libraries
import Image_Viewer as iv
import pygame, sys
pygame.init()

# Variables
run = True

# Draws Screen
screen = pygame.display.set_mode([1000, 600])

# Game Loop
while run:
    
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    iv.Load_Saved_Painting(screen, 'Testing.txt')
    pygame.display.flip()
    
sys.exit()
