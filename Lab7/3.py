import pygame


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Moving Ball")

ball_color = (255, 0, 0)
ball_radius = 25
ball_position = [400, 400]

def draw_ball():
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_position[1] -= 20
        if ball_position[1] < ball_radius:
            ball_position[1] = ball_radius
    if keys[pygame.K_DOWN]:
        ball_position[1] += 20
        if ball_position[1] > 800 - ball_radius:
            ball_position[1] = 800 - ball_radius
    if keys[pygame.K_LEFT]:
        ball_position[0] -= 20
        if ball_position[0] < ball_radius:
            ball_position[0] = ball_radius
    if keys[pygame.K_RIGHT]:
        ball_position[0] += 20
        if ball_position[0] > 800 - ball_radius:
            ball_position[0] = 800 - ball_radius


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    handle_keys()
    screen.fill((255, 255, 255))
    draw_ball()
    pygame.display.flip()
    clock.tick(24)

pygame.quit()