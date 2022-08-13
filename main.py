import pygame
from sys import exit

# very important to initialize the pygame module
pygame.init()

# creating a display surface
screen = pygame.display.set_mode((800, 400))
# set window title
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()

# font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface: pygame.Surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface: pygame.Surface = pygame.image.load('graphics/ground.png').convert()

score_surface: pygame.Surface = test_font.render('My game', False, (64, 64, 64))
score_rect: pygame.Rect = score_surface.get_rect(center=(400, 50))

snail_surface: pygame.Surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect: pygame.Rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface: pygame.Surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect: pygame.Rect = player_surface.get_rect(midbottom=(80, 300))

player_gravity: int = 0

while True:
    # draw all our elements
    # update everything

    # check for events
    for event in pygame.event.get():
        # checking of QUIT event
        if event.type == pygame.QUIT:
            # quiting pygame
            pygame.quit()
            # exiting the program
            exit()

        # player jumps if we clicked on it
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

        # player jumps if K_SPACE is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # print('jump')
                player_gravity = -20
        
        if event.type == pygame.KEYUP:
            # print('key up')
            pass

    # block image transfer, display the image surface
    # draw order is important!
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
    # pygame.draw.rect(screen, '#c0e8ec', score_rect)
    screen.blit(score_surface, score_rect)

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    # Player
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surface, player_rect)

    # keyboard input
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # collision check
    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # collision of a point (mouse pos) with rectangle (player)
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        # print('collision')
        if pygame.mouse.get_pressed()[0]:
            print('pressed')

    # updates the created display surface
    pygame.display.update()

    # makes sure that the while loop doesn't run at more than 60 times per second
    clock.tick(60)