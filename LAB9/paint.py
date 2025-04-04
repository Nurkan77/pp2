
import pygame, math

screen = pygame.display.set_mode((800,600))

draw_on = False
StartDraw = False
last_pos = (0, 0)
color = (0, 0, 0) #Start color
mode = 'pen'
radius = 10 #pen radius
screen.fill((255, 255, 255)) #screen filling white



def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

#make line not just dots




while True:
    pressed = pygame.key.get_pressed() #pressed button

    if pressed[pygame.K_r]:
        color = (255, 0, 0)
        radius = 10
    elif pressed[pygame.K_b]:
        color = (0, 0, 255)
        radius = 10
    elif pressed[pygame.K_g]:
        color = (0, 255, 0)
        radius = 10
    elif pressed[pygame.K_p]:
        radius = 10
        color = (255, 105, 180)
    elif pressed[pygame.K_y]:
        radius = 10
        color = (255, 255, 0)
    elif pressed[pygame.K_o]:
        radius = 10
        color = (255, 165, 0)
    elif pressed[pygame.K_d]:
        radius = 10
        color = (0, 0, 0)
    elif pressed[pygame.K_v]:
        radius = 10
        color = (255, 0, 255)
    elif pressed[pygame.K_s]:
        radius = 10
        color = (0, 191, 255)  
    elif pressed[pygame.K_SPACE] or pressed[pygame.K_w]: 
        radius = 25
        color = (255, 255, 255) #colors


    if pressed[pygame.K_1]: mode = 'pen'
    if pressed[pygame.K_2]: mode = 'circle' 
    if pressed[pygame.K_3]: mode = 'rect'  #modes of draw
    


    
    for event in pygame.event.get():
 
        if mode == 'rect': #draw rectangle
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                StartDraw = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if StartDraw:
                    pos = event.pos
    
                    width = pos[0] - sp[0]
                    height = pos[1] - sp[1]
    
                    pygame.draw.rect(screen, color , pygame.Rect(sp[0], sp[1], width, height))
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                StartDraw = False


        if mode == 'circle': #draw circle
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                StartDraw = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if StartDraw:
                    pos = event.pos
    
                    radius = math.sqrt((pos[0] - sp[0])**2 + (pos[1] - sp[1])**2)
    
                    pygame.draw.circle(screen, color , (sp[0], sp[1]), radius)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                StartDraw = False



        if event.type == pygame.QUIT: #close the window
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and mode == 'pen':
            pygame.draw.circle(screen, color, event.pos, radius)
            draw_on = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if event.type == pygame.MOUSEMOTION:
            if draw_on :
                pygame.draw.circle(screen, color, event.pos, radius)
                if mode == 'pen':
                    roundline(screen, color, event.pos, last_pos,  radius)

            last_pos = event.pos
    pygame.display.update()

