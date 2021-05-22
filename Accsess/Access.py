import pygame

if __name__ == '__main__':
    pygame.init()
    size = 700, 400
    screen = pygame.display.set_mode(size)
    color = pygame.Color(0, 0, 0)
    pygame.draw.circle(screen, (139, 0, 0), (100, 200), 75)
    pygame.draw.circle(screen, (139, 0, 0), (100, 112), 50)
    pygame.draw.circle(screen, (0, 100, 0), (100, 200), 62)
    pygame.draw.circle(screen, (0, 100, 0), (100, 117), 37)
    pygame.draw.circle(screen, (25, 25, 112), (100, 200), 55)
    pygame.draw.circle(screen, (25, 25, 112), (100, 122), 30)

    pygame.draw.circle(screen, (139, 0, 0), (250, 25), 15)
    pygame.draw.circle(screen, (0, 100, 0), (250, 125), 15)
    pygame.draw.circle(screen, (25, 25, 112), (250, 225), 15)

    font = pygame.font.Font(None, 25)
    text = font.render("Навык программирования на языке Python", True, (139, 0, 0))
    text_x = 275
    text_y = 20
    screen.blit(text, (text_x, text_y))

    font = pygame.font.Font(None, 25)
    text = font.render("Навык общаться с разными слоями общества", True, (0, 100, 0))
    text_x = 275
    text_y = 120
    screen.blit(text, (text_x, text_y))

    font = pygame.font.Font(None, 25)
    text = font.render("Навык свободно выступать на публике", True, (25, 25, 112))
    text_x = 275
    text_y = 220
    screen.blit(text, (text_x, text_y))

    pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
