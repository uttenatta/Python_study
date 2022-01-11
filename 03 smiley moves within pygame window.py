import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True
pic = pygame.image.load("CrazySmile.bmp")

picx = 0
picy = 0
COLOR = (0,0,0)
timer = pygame.time.Clock()
speedx = 10
speedy = 10

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += speedx
    picy += speedy
    if picx <=0 or picx + pic.get_width() >=800:
        speedx = -speedx
    if picy <=0 or picy + pic.get_height() >=600:
        speedy = -speedy

    screen.fill(COLOR)
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(60)

pygame.quit()