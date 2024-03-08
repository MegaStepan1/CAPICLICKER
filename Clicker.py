import pygame
import sys
import time

# Инициализация Pygame
pygame.init()

# Установка цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Капибара кликер")

# Загрузка изображений капибары
capibara_images = [
    pygame.image.load("capibara1.png"),
    pygame.image.load("capibara2.png"),
    pygame.image.load("capibara3.png"),
    pygame.image.load("capibara4.png"),
    pygame.image.load("capibara5.png"),
    pygame.image.load("capibara6.png"),
    pygame.image.load("capibara7.png")
]

# Переменные игры
counter = 0
level = 1

# Основной цикл игры
while level < 7:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            counter += 1
            if counter % 1000 == 0:
                level += 1

                # Отображение капибары
    screen.blit(capibara_images[level - 1], (WIDTH // 2 - capibara_images[level - 1].get_width() // 2,
                                             HEIGHT // 2 - capibara_images[level - 1].get_height() // 2))

    # Отображение счетчика
    font = pygame.font.Font(None, 36)
    text = font.render(f"Клики: {counter}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
