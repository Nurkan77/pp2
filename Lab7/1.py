import pygame
import time

pygame.init()

screen_size = (829, 836)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()
mickey = pygame.image.load("/Users/kurbanbek10/Downloads/mickeyclock.jpeg")
minute_hand = pygame.image.load("/Users/kurbanbek10/Downloads/mickeyclock.jpeg")
second_hand = pygame.image.load("/Users/kurbanbek10/Downloads/mickeyclock.jpeg")

minute_hand_pos = (screen_size[0] // 2, screen_size[1] // 2)
second_hand_pos = (screen_size[0] // 2, screen_size[1] // 2)

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = (minutes / 60) * 360
    second_angle = (seconds / 60) * 360

    minute_hand_rotated = pygame.transform.rotate(minute_hand, 90 - minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand, 90 - second_angle)

    minute_hand_pos = (screen_size[0] // 2 - minute_hand_rotated.get_width() // 2,
                       screen_size[1] // 2 - minute_hand_rotated.get_height() // 2)
    second_hand_pos = (screen_size[0] // 2 - second_hand_rotated.get_width() // 2,
                       screen_size[1] // 2 - second_hand_rotated.get_height() // 2)

    screen.fill('white')

    screen.blit(mickey, (0, 0))
    screen.blit(minute_hand_rotated, minute_hand_pos)
    screen.blit(second_hand_rotated, second_hand_pos)

    pygame.display.flip()
    pygame.time.delay(1000)