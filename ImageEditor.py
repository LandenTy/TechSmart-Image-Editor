"""
ImageEditor

Description: Tool that lets you Create and Edit Vector Images for later use
in other projects.
"""
# Libraries
from Engine import *

# Editor
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
    
    brushes, colors, rgb, saveLoad, iBox = draw_menu()
    
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
                        
            # Project Name Field
            if iBox.collidepoint(event.pos):
                print("TEXTBOX!")
                
    if Load:
        Load_Saved_Painting('SaveData.txt')
        
    pygame.display.flip()
    
sys.exit()
