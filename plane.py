import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Самолеты")

# Загрузка изображений
background_image = pygame.image.load('sky.png').convert()
red_plane_image = pygame.image.load('red_plane.png').convert_alpha()
green_plane_image = pygame.image.load('green_plane.png').convert_alpha()


class Plane:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

    # Отрисовка самолёта
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    # Обновление положения по нажатию клавиш
    def update_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= 2
        elif keys[pygame.K_DOWN]:
            self.y += 2

        if keys[pygame.K_LEFT]:
            self.x -= 2
        elif keys[pygame.K_RIGHT]:
            self.x += 2

    # Обновление позиции мыши
    def update_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Выравниваем центр самолёта с центром курсора
        self.x = mouse_x - self.width // 2
        self.y = mouse_y - self.height // 2


red_plane = Plane(WIDTH // 4, HEIGHT // 2, red_plane_image)
green_plane = Plane(WIDTH * 3 // 4, HEIGHT // 2, green_plane_image)

# Скрываем стандартный курсор мыши
pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Прорисовываем фон неба
    screen.blit(background_image, (0, 0))

    # Управление красным самолётом через клавиши
    red_plane.update_keyboard()

    # Зелёный самолёт двигается за мышью
    green_plane.update_mouse()

    # Рисуем самолёты
    red_plane.draw()
    green_plane.draw()

    # Переворот экрана
    pygame.display.flip()

pygame.quit()
