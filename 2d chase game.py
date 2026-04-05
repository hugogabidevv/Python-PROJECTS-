import pygame
import sys

pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D chase game")

clock = pygame.time.Clock()

# fonts
title_font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 30)

# player
player_x = 400
player_y = 300
player_speed = 200
player_dir = "right"

# enemy
enemy_x = 200
enemy_y = 200
enemy_speed = 120

# sword
sword_size = 20

# Menu
state = "menu"

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # menu
    if state == "menu":
        screen.fill((0, 0, 0))

        title = title_font.render("MY GAME", True, (255, 255, 255))
        screen.blit(title, (300, 200))

        text = small_font.render("Press ENTER to start", True, (200, 200, 200))
        screen.blit(text, (260, 300))

        if keys[pygame.K_RETURN]:
            state = "playing"

    # GAME
    elif state == "playing":

        # player movement
        if keys[pygame.K_w]:
            player_y -= player_speed * dt
            player_dir = "up"
        if keys[pygame.K_s]:
            player_y += player_speed * dt
            player_dir = "down"
        if keys[pygame.K_a]:
            player_x -= player_speed * dt
            player_dir = "left"
        if keys[pygame.K_d]:
            player_x += player_speed * dt
            player_dir = "right"

        # inside screen
        player_x = max(0, min(750, player_x))
        player_y = max(0, min(550, player_y))

        # enemy follows player
        if enemy_x < player_x:
            enemy_x += enemy_speed * dt
        if enemy_x > player_x:
            enemy_x -= enemy_speed * dt

        if enemy_y < player_y:
            enemy_y += enemy_speed * dt
        if enemy_y > player_y:
            enemy_y -= enemy_speed * dt

        enemy_x = max(0, min(750, enemy_x))
        enemy_y = max(0, min(550, enemy_y))

        # enemy direction
        if abs(player_x - enemy_x) > abs(player_y - enemy_y):
            enemy_dir = "right" if player_x > enemy_x else "left"
        else:
            enemy_dir = "down" if player_y > enemy_y else "up"

        # hitboxes
        player_rect = pygame.Rect(player_x, player_y, 50, 50)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)

        # player sword
        if player_dir == "right":
            player_sword = pygame.Rect(player_x + 40, player_y + 25, sword_size, 5)
        elif player_dir == "left":
            player_sword = pygame.Rect(player_x - sword_size, player_y + 25, sword_size, 5)
        elif player_dir == "up":
            player_sword = pygame.Rect(player_x + 20, player_y - sword_size, 5, sword_size)
        else:
            player_sword = pygame.Rect(player_x + 20, player_y + 40, 5, sword_size)

        # enemy sword
        if enemy_dir == "right":
            enemy_sword = pygame.Rect(enemy_x + 40, enemy_y + 25, sword_size, 5)
        elif enemy_dir == "left":
            enemy_sword = pygame.Rect(enemy_x - sword_size, enemy_y + 25, sword_size, 5)
        elif enemy_dir == "up":
            enemy_sword = pygame.Rect(enemy_x + 20, enemy_y - sword_size, 5, sword_size)
        else:
            enemy_sword = pygame.Rect(enemy_x + 20, enemy_y + 40, 5, sword_size)

        # collisions
        if player_rect.colliderect(enemy_rect) or enemy_sword.colliderect(player_rect):
            state = "dead"

        # draw
        screen.fill((34, 139, 34))

        # player
        pygame.draw.circle(screen, (255, 220, 180), (int(player_x + 25), int(player_y + 10)), 10)
        pygame.draw.rect(screen, (0, 0, 200), (int(player_x + 10), int(player_y + 20), 30, 30))
        pygame.draw.rect(screen, (180, 180, 180), (int(player_x + 40), int(player_y + 25), 10, 5))
        pygame.draw.rect(screen, (200, 200, 200), player_sword)

        # enemy
        pygame.draw.circle(screen, (100, 255, 100), (int(enemy_x + 25), int(enemy_y + 10)), 10)
        pygame.draw.rect(screen, (0, 150, 0), (int(enemy_x + 10), int(enemy_y + 20), 30, 30))
        pygame.draw.rect(screen, (255, 0, 0), (int(enemy_x), int(enemy_y + 25), 10, 5))
        pygame.draw.rect(screen, (255, 0, 0), enemy_sword)

    # death
    elif state == "dead":
        screen.fill((0, 0, 0))

        text = title_font.render("YOU DIED", True, (255, 0, 0))
        screen.blit(text, (250, 250))

        text2 = small_font.render("Press R to restart", True, (255, 255, 255))
        screen.blit(text2, (260, 320))

        if keys[pygame.K_r]:
            player_x = 400
            player_y = 300
            enemy_x = 200
            enemy_y = 200
            state = "menu"

    pygame.display.update()

pygame.quit()
sys.exit()