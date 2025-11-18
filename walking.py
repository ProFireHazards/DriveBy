# Import the necessary modules
import pygame
import random
import time
# Initialize the game engine
pygame.init()
clockobject = pygame.time.Clock()
# Define some colors
BLUE = (175, 88, 37)
BLACK = (200, 200, 200)
WHITE = (175, 88, 37)
RED = (252, 83, 83)

# Set the screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Create the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# Set the title of the window
pygame.display.set_caption('Driveby')
image = pygame.image.load("player.png")
my_list = ["enemy1.png", "enemy2.png", "enemy3.png", "enemy4.png"]
en = random.choice(my_list)
image2 = pygame.image.load(en)
en = random.choice(my_list)
image3 = pygame.image.load(en)
en = random.choice(my_list)
image4 = pygame.image.load(en)
en = random.choice(my_list)
image5 = pygame.image.load(en)
# Create a player object
player = pygame.Rect(400, 550, 40, 40)

# Create a variable to control the player's speed
player_speed = 3

# Create a list to store the player's bullets
bullets = []

# Create a list to store the enemies
enemies = []


# Create a variable to control the enemies' speed
enemy_speed = 4
cap = enemy_speed
# Create a variable to control the rate at which enemies are spawned
spawn_rate = 30
choui = [f"{image2}", f"{image3}", f"{image4}", f"{image5}"]
# Create a variable to keep track of the game clock
clock = pygame.time.Clock()
death = "n"
# Define the game loop
done = False
score=0
while not done:
    cap=cap-0.0000000000000000000000000000000000001
    epp = random.choice(choui)
    # Get the list of events from the event queue
    events = pygame.event.get()

    # Iterate over the events
    for event in events:
        # Check if the event is the QUIT event
        if event.type == pygame.QUIT:
            # If it is, set done to True to exit the game loop
            done = True

    # Get the current state of the keyboard
    keys = pygame.key.get_pressed()

    # Update the player's position based on the keys pressed
    if keys[ord('a')]:
        player.x -= player_speed
    if keys[ord('d')]:
        player.x += player_speed
    if keys[ord('w')]:
        player.y -= player_speed
    if keys[ord('s')]:
        player.y += player_speed

    # Check if the player is trying to shoot
    if keys[pygame.K_SPACE]:
        # If so, create a new bullet and add it to the list of bullets
        bullets.append(pygame.Rect(player.x+40, player.y, 1, 3))
    # Check if the spawn rate counter has reached zero
    if spawn_rate == 0:
        # If so, reset the counter and spawn a new enemy
        spawn_rate = 30
        enemies.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - 40), 0, 40, 40))

    # Update the spawn rate counter
    spawn_rate -= 2

    # Iterate over the enemies
    for enemy in enemies:
        # Update the enemy's position
        if enemy_speed < cap:
            enemy_speed = enemy_speed+0.0001
        enemy.y += enemy_speed
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)

    # Iterate over the bullets
    for bullet in bullets:
        # Update the bullet's position
        bullet.y -= 6

        # Check if the bullet has hit any enemies
        for enemy in enemies:
            if bullet.colliderect(enemy):
                score=score+1
                cap=cap+30
                # Remove the bullet and the enemy
                bullets.remove(bullet)
                enemies.remove(enemy)

    # Fill the screen with blue
    screen.fill(BLUE)
    screen.fill(BLUE)

# Draw the player on the screen
    pygame.draw.rect(screen, WHITE, player)

# Draw the enemies on the screen
    for enemy in enemies:
        pygame.draw.rect(screen, BLUE, enemy)
        screen.blit(image2, enemy)
        if player.colliderect(enemy):
            death = "y"

# Draw the bullets on the screen
    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, bullet)
        if bullet.y > SCREEN_HEIGHT:
            bullets.remove(bullet)
    font = pygame.font.Font("Retro Gaming.ttf", 22)
    text = font.render("Score: " + str(score), True, (255, 0, 0))
    if "y" in death:
        enemy_speed = 4
        cap = enemy_speed
        image2 = pygame.image.load(en)
        bullets = []
        enemies = []
        text = font.render("Game Over, Score: " + str(score), True, (255, 0, 0))
        screen.blit(text, [500, 500])
        pygame.display.update()
        time.sleep(2)
        bullets = []
        enemies = []
        score = 0
        death = "n"
    screen.blit(text, [10, 10])
    screen.blit(image, player)
    pygame.display.update()
# Update the screen
    pygame.display.flip()

# Limit the game to 60 frames per second
    clock.tick(60)

# Close the game window
pygame.quit()
