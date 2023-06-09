import pygame

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
fall_speed = 2
jump_speed = 100

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Dino Game")
WIN.fill(black)
clock=pygame.time.Clock()
info_obj = pygame.display.Info()
#x, y = info_obj.current_w / 2, info_obj.current_h / 2
x, y = 400, 500
size = 30

def update():
    #global y
    #if (y + fall_speed < info_obj.current_h - 30):
        #y += fall_speed
    pygame.draw.rect(WIN, red, pygame.Rect(x, y, size, size))

def boundry():
        pygame.draw.line(WIN, white, [0, 300 + jump_speed], [info_obj.current_w, 300 + jump_speed], 5)
        pygame.draw.line(WIN, white, [0, 500 + size], [info_obj.current_w, 500 + size], 5)

def main():
    run = True
    global y
    global x
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and y == 500:
                if event.key == pygame.K_SPACE :
                    y -= jump_speed
            elif event.type == pygame.KEYDOWN and x != 500:
                if event.key == pygame.K_SPACE :
                    y += jump_speed
        WIN.fill(black)
        boundry()
        update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()