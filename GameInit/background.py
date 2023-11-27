import pygame

gaul_image = pygame.image.load('gaulFullQuality.jpg')
screen_width, screen_height = 760, 760


# gaul_image = pygame.image.load('staticmap.png')
# screen_width, screen_height = 1280, 1280  # Adjust the window size as needed
def init():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Roman Cities Map')

    convertedImg = pygame.Surface.convert(gaul_image)
    convertedImg = pygame.transform.scale(convertedImg, (screen_width, screen_height))


    return convertedImg, screen


def getDimensons():
    return screen_width, screen_height
