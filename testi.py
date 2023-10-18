import pygame
pygame.init()
size=(500,500)
colour='red'
screen=pygame.display.set_mode(size)
pygame.display.set_caption('лол')
image=pygame.image.load('EGE-1024x899.jpg')
image=pygame.transform.scale(image,size)
screen.fill(colour)
screen.blit(image,(0,10))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
