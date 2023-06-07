import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
fall_speed = 2
jump_speed = 100

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Flappy Bird")
WIN.fill(black)
clock=pygame.time.Clock()
info_obj = pygame.display.Info()
x, y = info_obj.current_h / 2 , info_obj.current_w / 2

def update():
    global y
    if (y + fall_speed < info_obj.current_h - 30):
        y += fall_speed
    pygame.draw.rect(WIN, red, pygame.Rect(x, y, 30, 30))
def main():
    run = True
    global y
    global x
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and y - jump_speed > 0:
                    y -= jump_speed
            

        WIN.fill(black)
        update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()