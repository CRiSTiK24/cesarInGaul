import pygame
from Mappa.constants import options

gaul_image = pygame.image.load('satstaticmap.png')

screen_width, screen_height = options.get("width"), options.get("height")

def init():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Roman Cities Map')

    convertedImg = pygame.Surface.convert(gaul_image)
    convertedImg = pygame.transform.scale(convertedImg, (screen_width, screen_height))

    return convertedImg, screen


def getDimensons():
    return screen_width, screen_height
