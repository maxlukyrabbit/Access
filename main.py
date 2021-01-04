import pygame

size_input = input().split(' ')
j = 0
if len(size_input) == 2:
    if __name__ == '__main__':
        a = int(size_input[0]), int(size_input[1])
        size_input = int(size_input[0]), int(size_input[0])
        pygame.init()
        size = size_input
        screen = pygame.display.set_mode(size)
        b = []
        for k in range(a[1]):
            b.append(int("0"))
        if a[1] % 2 != 0:
            b[0] = a[0] / a[1]
            for i in range(a[1]):
                for j in range(a[1]):
                    if i % 2 == 0:
                        color = pygame.Color(250, 250, 250)
                        pygame.draw.rect(screen, color, (b[0], b[1], a[0] / a[1], a[0] / a[1]), 0)
                        b[0] += a[0] / a[1] * 2
                        if j == a[1] - 1:
                            b[0] = 0

                    if i % 2 != 0:
                        color = pygame.Color(250, 250, 250)
                        pygame.draw.rect(screen, color, (b[0], b[1], a[0] / a[1], a[0] / a[1]), 0)
                        b[0] += a[0] / a[1] * 2
                        if j == a[1] - 1:
                            b[0] = a[0] / a[1]
                b[1] += a[0] / a[1]
        if a[1] % 2 == 0:
            for i in range(a[1]):
                for j in range(a[1]):
                    if i % 2 == 0:
                        color = pygame.Color(250, 250, 250)
                        pygame.draw.rect(screen, color, (b[0], b[1], a[0] / a[1], a[0] / a[1]), 0)
                        b[0] += a[0] / a[1] * 2
                        if j == a[1] - 1:
                            b[0] = a[0] / a[1]

                    if i % 2 != 0:
                        color = pygame.Color(250, 250, 250)
                        pygame.draw.rect(screen, color, (b[0], b[1], a[0] / a[1], a[0] / a[1]), 0)
                        b[0] += a[0] / a[1] * 2
                        if j == a[1] - 1:
                            b[0] = 0
                b[1] += a[0] / a[1]

        print(b)
        pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()