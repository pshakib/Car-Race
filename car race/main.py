
import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 300, 550
roadwidth = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Race!")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (60, 220, 0)
GRAY = (88,89,91)

FPS = 60
VEL = 5
CAR_WIDTH, CAR_HEIGHT = 160, 190
lane = pygame.Rect(WIDTH/2, 0, 5, HEIGHT)


YCAR = pygame.image.load(os.path.join('Assets', 'ycar.png'))
yellowcar = pygame.transform.scale(YCAR, (CAR_WIDTH, CAR_HEIGHT))
WCAR = pygame.image.load(os.path.join('Assets', 'wcar.png'))
whitecar = pygame.transform.scale(WCAR, (CAR_WIDTH, CAR_HEIGHT))

def draw(yellow, white):
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, lane)
    screen.blit(yellowcar, (yellow.x, yellow.y))
    screen.blit(whitecar, (white.x, white.y))
    pygame.display.update()


def main():
    yellow = pygame.Rect(100, 350, CAR_WIDTH, CAR_HEIGHT)
    white = pygame.Rect(2, 30, CAR_WIDTH, CAR_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        white.y += 10
        if white.y > HEIGHT:
            white.y = -200
            if random.randint(0,1) == 0:
                white.x = 2
            else:
                white.x = 150

            
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and yellow.x > 0:
            yellow.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and yellow.x < 170:
            yellow.x += VEL      
        
        draw(yellow, white)

    pygame.quit()

if __name__ == "__main__":
    main()


