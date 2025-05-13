import pygame

run = True
width = 1400
height = 500
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame by Aditya", True, (255, 0, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
                or event.type == pygame.MOUSEBUTTONUP \
                or event.type == pygame.KEYUP:
            run = False
