import pygame
import os

# Инициализация Pygame
pygame.init()

# Параметры окна
screen_width, screen_height = 500, 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Музыкальный Плеер")

# Папка с музыкой
MUSIC_FOLDER = "/Users/kurbanbek10/Documents/pp2/Kurbanbek/muz/"

# Получаем список аудиофайлов (фильтруем только .mp3 и .wav)
music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(('.mp3', '.wav'))]

# Проверяем, есть ли музыка
if not music_files:
    print("❌ Ошибка: В папке нет аудиофайлов!")
    pygame.quit()
    quit()

# Выводим список доступных треков
print("🎵 Найденные файлы:")
for i, file in enumerate(music_files):
    print(f"{i + 1}. {file}")

# Загружаем первый трек
current_music = 0
track_path = os.path.join(MUSIC_FOLDER, music_files[current_music])
pygame.mixer.music.load(track_path)

# Шрифт для кнопок
font = pygame.font.SysFont(None, 36)

# Клавиши управления
key_play = pygame.K_SPACE  # Воспроизведение / Пауза
key_stop = pygame.K_ESCAPE  # Остановить
key_next = pygame.K_RIGHT  # Следующий трек
key_prev = pygame.K_LEFT  # Предыдущий трек

# Подписи к клавишам
labels = {
    key_play: "Play/Pause (SPACE)",
    key_stop: "Stop (ESC)",
    key_next: "Next (→)",
    key_prev: "Previous (←)",
}

# Координаты кнопок на экране
label_pos = {
    key_play: (50, screen_height - 50),
    key_stop: (150, screen_height - 50),
    key_next: (250, screen_height - 50),
    key_prev: (350, screen_height - 50),
}

# Отображение кнопок на экране
for key in label_pos:
    label_surface = font.render(labels[key], True, (255, 255, 255))
    label_rect = label_surface.get_rect(center=label_pos[key])
    screen.blit(label_surface, label_rect)

# Запускаем музыку
pygame.mixer.music.play()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == key_play:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == key_stop:
                pygame.mixer.music.stop()

            elif event.key == key_next:
                current_music = (current_music + 1) % len(music_files)
                track_path = os.path.join(MUSIC_FOLDER, music_files[current_music])
                pygame.mixer.music.load(track_path)
                pygame.mixer.music.play()
                print(f"▶ Следующий трек: {music_files[current_music]}")

            elif event.key == key_prev:
                current_music = (current_music - 1) % len(music_files)
                track_path = os.path.join(MUSIC_FOLDER, music_files[current_music])
                pygame.mixer.music.load(track_path)
                pygame.mixer.music.play()
                print(f"◀ Предыдущий трек: {music_files[current_music]}")

    pygame.display.update()

# Завершаем Pygame
pygame.quit()