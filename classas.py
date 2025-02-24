import pygame, sys, random
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((1700, 900))
clock = pygame.time.Clock()
cloud_image_unscaled = pygame.image.load('cloud.png').convert_alpha()
hooman_image = pygame.image.load('hooman.png').convert_alpha()
hooman_image.set_colorkey((255,255,255))
hooman_umbrella = pygame.image.load('hooman_umbrella.png').convert_alpha()
cloud_image = pygame.transform.scale(cloud_image_unscaled, (cloud_image_unscaled.get_width()*0.5, cloud_image_unscaled.get_height()*0.5))

class Rain:
    def __init__(self):
        self.x = random.randint(0, 1700)
        self.y = -5


    def draw(self):
        pygame.draw.circle(screen, (250, 250, 250), (self.x, self.y), 2, 0)


    def move(self):
        self.y += random.randint(1, 2)


class Cloud:
    def __init__(self):
        self.x = random.randint(0, 1700-cloud_image.get_width())
        self.y = random.randint(0, 100)

    def draw(self):
        screen.blit(cloud_image, (self.x, self.y))

    def move(self):
        self.x += 0.5

pretty_cloud = Cloud()
rain = []

xpos = 200

while True:
    clock.tick(500)
    pressed_key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((150, 150,150))
    rain.append(Rain())
    for R in rain:
        R.draw()
        R.move()

    if pressed_key[pygame.K_RIGHT] and xpos <= 1700 - hooman_image.get_width():
        xpos += 0.3
    if pressed_key[pygame.K_LEFT] and xpos >= 0:
        xpos -= 0.3
    # if pressed_key[pygame.K_UP]:
    #     ypos -= 0.3
    # if pressed_key[pygame.K_DOWN]:
    #     ypos += 0.3

    #screen.blit(cloud_image, (200, 200))
    screen.blit(hooman_image, (xpos, screen.get_height() - hooman_image.get_height()))
    pretty_cloud.draw()
    pretty_cloud.move()




    # rain.append(Rain())
    # if pressed_key[pygame.K_RIGHT]:
    #     xpos += 0.3
    # if pressed_key[pygame.K_LEFT]:
    #     xpos -= 0.3
    # if pressed_key[pygame.K_UP]:
    #     ypos -= 0.3
    # if pressed_key[pygame.K_DOWN]:
    #     ypos += 0.3


    pygame.display.flip()