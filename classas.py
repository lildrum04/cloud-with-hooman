import pygame, sys, random, time

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((1700, 900))
clock = pygame.time.Clock()

cloud_image_unscaled = pygame.image.load('cloud.png').convert_alpha()
hooman_image = pygame.image.load('hooman.png').convert_alpha()
hooman_image.set_colorkey((255, 255, 255))
hooman_umbrella = pygame.image.load('hooman_umbrella.png').convert_alpha()
cloud_image = pygame.transform.scale(cloud_image_unscaled,
                                     (cloud_image_unscaled.get_width() * 0.5, cloud_image_unscaled.get_height() * 0.5))
umbrella_height = hooman_image.get_height()
umbrella_width = hooman_umbrella.get_width()
resized_umbrella = pygame.transform.scale(hooman_umbrella,(umbrella_width, umbrella_height))


print(time.time())

class Rain:
    def __init__(self, cloud_x, cloud_y, cloud_width):
        self.x = random.randint(int(cloud_x + cloud_width * 0.20), int(cloud_x + cloud_width * 0.85))  # Reduced width
        self.y = int(cloud_y + 180)  # Starts below the cloud

    def draw(self):
        pygame.draw.circle(screen, (250, 250, 250), (self.x, self.y), 2, 0)

    def move(self):
        self.y += random.randint(1, 2)

    def check_collision(self, human):
        return pygame.Rect(human.x, human.y, hooman_image.get_width(), hooman_image.get_height()).collidepoint(self.x, self.y)


class Cloud:
    def __init__(self):
        self.x = random.randint(0, 1700 - cloud_image.get_width())
        self.y = random.randint(0, 100)

    def draw(self):
        screen.blit(cloud_image, (self.x, self.y))

    def move(self):
        self.x += 0.5


class James:
    def __init__(self):
        self.x = 200
        self.y = screen.get_height() - hooman_image.get_height()
        self.umbrella_open = False

    def draw(self):
        screen.blit(hooman_image, (self.x, self.y))  # Draw the human

        if self.umbrella_open:


            # Draw the resized umbrella at the same position as the human (no offset)
            screen.blit(resized_umbrella, (self.x, self.y))


character_height = screen.get_height() - hooman_image.get_height()
pretty_cloud = Cloud()
rain = []
jamie = James()

xpos = 200

while True:
    clock.tick(500)
    pressed_key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: and event.key == pygame.K_SPACE:



    screen.fill((150, 150, 150))
    rain.append(Rain(pretty_cloud.x, pretty_cloud.y, cloud_image.get_width()))

    for R in rain:
        R.draw()
        R.move()


        if R.check_collision(jamie):

            jamie.umbrella_open = True
        else:
            jamie.umbrella_open = False
        if R.y > screen.get_height():

            rain.remove(R)


    if all(not R.check_collision(jamie) for R in rain):
        jamie.umbrella_open = False


    if pressed_key[pygame.K_RIGHT] and xpos <= 1700 - hooman_image.get_width():
        xpos += 2  # Move right
    if pressed_key[pygame.K_LEFT] and xpos >= 0:
        xpos -= 2  # Move left

    # Update the human's x-position
    jamie.x = xpos

    # Draw everything on the screen
    pretty_cloud.draw()
    pretty_cloud.move()
    jamie.draw()

    pygame.display.flip()
