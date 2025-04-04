import pygame, sys, random, time
pygame.init()

FPS = pygame.time.Clock() #Make game slow
fps = 10
FPS.tick(fps)


White = (255, 255, 255)
LightSteelBlue = (176, 196, 222)
Red = (255, 0, 0)
Green = (0, 255, 0) #Colors

height = 500
width = 500
window = (width, height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Lab9 Snake") #Window settings
step = 20

direction = 'RIGHT'

End = False 
append = False 

background=pygame.transform.scale(pygame.image.load('WEEK9/img/background.png'),(600,600)) 
food=pygame.transform.scale(pygame.image.load("WEEK9/img/food.png"),(20,20)) 
font=pygame.font.SysFont('Times New Roman', 24)
score=0  
head_x = head_y=240
body=[(head_x, head_y),(head_x, head_y),(head_x, head_y)] #body as array

step=20 
move_x,move_y=20,0 #first speed
direction =  'RIGHT' #first direction
t = 0



def rand():
    return(random.randint(2,22)*20) #random food spawn

food_x=rand()
food_y=rand()

while True:
    FPS.tick(fps)
    pressed = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type==pygame.QUIT or pressed[pygame.K_SPACE]:
            pygame.quit()
            sys.exit() 


        if pressed[pygame.K_DOWN]: 
            if direction!='UP': 
                direction= 'DOWN' 
                move_x= 0 
                move_y= step 

        if pressed[pygame.K_UP]: 
            if direction!='DOWN':
                direction = 'UP'
                move_x = 0
                move_y = -step

        if pressed[pygame.K_LEFT]:
            if direction!='RIGHT':
                direction = 'LEFT'
                move_x = -step
                move_y = 0

        if pressed[pygame.K_RIGHT]: 
            if direction!='LEFT':
                direction = 'RIGHT'
                move_x = step
                move_y = 0    #Head movement directions

        
    if not End:    
        body.append([head_x,head_y]) 
        body.pop(0) 
        if append:
            body.append([head_x,head_y])  #body increase
            score+= random.randint(1,5)
            append=False
        head_x+=move_x 
        head_y+=move_y
        t +=1 



        if head_x<0 or head_x>480 or head_y<0 or head_y>480: #inside the borders
            End=True 

        if t>50: #change food location after some amount of movements
            food_x=rand()
            food_y=rand()
            t = 0            
        
        while head_x==food_x and head_y==food_y:
            food_x=rand()
            food_y=rand()
            t = 0
            append=True
        screen.blit(background,(0, 0)) 
        screen.blit(food,(food_x,food_y))
        pygame.draw.rect(screen,(0, 100, 0),(head_x,head_y,20,20))

        for block in body:
        

            while block[0]==food_x and block[1]==food_y:    
                food_x=rand()
                food_y=rand()
                fps = fps + 1
                FPS.tick(fps)

                
            if head_x==block[0] and head_y==block[1]: 
                End=True 
                break 
            pygame.draw.rect(screen,(0,200,0),(block[0],block[1],20,20)) 
            screen.blit(font.render("Score: {}".format(score),True,(255,0,0)), (10,10))
            screen.blit(font.render("Level: {}".format(len(body)-3),True,(255,0,0)), (10,40)) 
    else: 
        screen.fill((255,255,255)) 
        screen.blit(font.render("GAME OVER",True,(255,0,0)),(175,200))  #Game Over
    pygame.display.update() 