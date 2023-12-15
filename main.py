import pygame
import loadCSV
import GameInit.faction as Factions
import GameInit.background as Background
from ObjectClasses.city import City
import AuxFiles.colorConverter as ColorConverter

# Load your filtered DataFrame with Roman cities using loadCSV module
filteredCityData = loadCSV.loadDatabase()

arrayFactions = Factions.init()

# Create a list of City objects
cities = [City(row['Ancient Toponym'], row['Longitude (X)'], row['Latitude (Y)'], 50, arrayFactions.get("N")) for
          index, row in filteredCityData.iterrows()]

gmap = Background.gmplotInit()

# Set up Pygame
pygame.init()
gaul_image = pygame.image.load('cig.jpg')
screen = pygame.display.set_mode((600, 600))

for city in cities:
    gmap.marker(lat=city.latitude, lng=city.longitude, color=ColorConverter.rgb_to_hex(city.faction.color),
                title=city.name)

gmap.draw("map.html")

# Pygame main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(gaul_image, (0, 0))

    # Draw cities as points on the screen
    pygame.display.flip()


# Quit Pygame
pygame.quit()
