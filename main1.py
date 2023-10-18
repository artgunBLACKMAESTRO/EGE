import pygame

pygame.init()

window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Peter the Piglet")

# загружаем изображение
background_image = pygame.image.load("EGE-1024x899.jpg")

# подгоняем масштаб под размер окна
background_image = pygame.transform.scale(background_image, window_size)

# накладываем изображение на поверхность
screen.blit(background_image, (0, 0))

screen.fill((200,0,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()