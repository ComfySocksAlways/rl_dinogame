import pygame
import random

#initialize the pygame library
pygame.init()
#set game window size
screen = pygame.display.set_mode((800,400))
#set title
pygame.display.set_caption("Dino Game")
#create clock to control how fast game runs
clock=pygame.time.Clock()
#set font for score
font = pygame.font.SysFont(None,36)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#dino
dino = pygame.Rect(50,300,40,40)

gravity = 0 #control how dino moves up and falls down
is_jumping = False #prevents from jumping when already in air

#Cactus
cactus = pygame.Rect(800,310,20,40)

score = 0

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        gravity = -10
        is_jumping = True
    
    gravity += 0.5
    dino.y += gravity
    if dino.y >= 300:
        dino.y = 300
        is_jumping = False
    
    cactus.x -= 5
    if cactus.x < -20:
        cactus_delay = random.randint(5,200)
        cactus.x = 800 + cactus_delay
        score += 1

    if dino.colliderect(cactus):
        print("GAME OVER!")
        running = False

    pygame.draw.rect(screen,BLACK,dino)
    pygame.draw.rect(screen, (34, 177, 76), cactus)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(120)

pygame.quit()