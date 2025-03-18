import pygame
import os

pygame.init()

playlist = []

music_folder = r"C:\Users\Nurasyl\OneDrive\Рабочий стол\2 semester\PP2\lab7\assets\musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Musics")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join(
    "lab7", "assets", "images", "background.png"))

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

playb = pygame.image.load(os.path.join("lab7", "assets", "images", "play.png"))
pausb = pygame.image.load(os.path.join(
    "lab7", "assets", "images", "pause.png"))
nextb = pygame.image.load(os.path.join("lab7", "assets", "images", "next.png"))
prevb = pygame.image.load(os.path.join("lab7", "assets", "images", "back.png"))

index = 0

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(0)
aplay = True

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))

    screen.blit(background, (0, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))
    playb = pygame.transform.scale(playb, (50, 50))
    pausb = pygame.transform.scale(pausb, (50, 50))
    if aplay:
        screen.blit(pausb, (370, 590))
    else:
        screen.blit(playb, (370, 590))
    nextb = pygame.transform.scale(nextb, (50, 50))
    screen.blit(nextb, (460, 590))
    prevb = pygame.transform.scale(prevb, (50, 50))
    screen.blit(prevb, (273, 590))

    clock.tick(60)
    pygame.display.update()
