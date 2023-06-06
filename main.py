import pygame

pygame.init()
WIDTH, HEIGHT = 900, 500
x, y = 435, 235
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
WIN.fill(black)


def main():
    run = True
    global y
    global x
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and y - 25 > 0:
                    y -= 25
            #y += 10

            WIN.fill(black)
            pygame.draw.rect(WIN, red, pygame.Rect(x, y, 30, 30))
            pygame.display.update()
    pygame.quit()


main()