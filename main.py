import geopandas as gpd
import pygame
import loadCSV
import GameInit.factionInit as factions
import Calculations.pixelLatitudeLongitudeConvertors as pixelCalculations
from ObjectClasses.city import City

# Load your filtered DataFrame with Roman cities using loadCSV module
filteredCityData = loadCSV.loadDatabase()

arrayFactions = factions.init()

# Create a list of City objects
cities = [City(row['Ancient Toponym'], row['Longitude (X)'], row['Latitude (Y)'], 50, arrayFactions.get("RO")) for index, row in filteredCityData.iterrows()]

# Set up Pygame
pygame.init()
screen_width, screen_height = 1280, 1280  # Adjust the window size as needed
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Roman Cities Map')

gaul_image = pygame.image.load('staticmap.png')

# Pygame main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(gaul_image, (0, 0))

    # Draw cities as points on the screen
    for city in cities:
        pygame.draw.circle(screen, city.faction.color, (pixelCalculations.getPointXY(city.latitude, city.longitude)), 5)

        font = pygame.font.Font(None, 12)
        text = font.render(city.name, True, (0, 0, 0))
        screen.blit(text, (pixelCalculations.getPointXY(city.latitude, city.longitude)))



    pygame.display.flip()

# Quit Pygame
pygame.quit()