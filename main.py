import pygame
import loadCSV
import GameInit.faction as Factions
import GameInit.background as Background
import Calculations.pixelLatitudeLongitudeConvertors as pixelCalculations
from ObjectClasses.city import City

# Load your filtered DataFrame with Roman cities using loadCSV module
filteredCityData = loadCSV.loadDatabase()

arrayFactions = Factions.init()

# Create a list of City objects
cities = [City(row['Ancient Toponym'], row['Longitude (X)'], row['Latitude (Y)'], 50, arrayFactions.get("RO")) for index, row in filteredCityData.iterrows()]

# Set up Pygame
pygame.init()
gaul_image, screen = Background.init()

# Pygame main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(gaul_image, (0, 0))

    # Draw cities as points on the screen
    #for city in cities:
    #    pygame.draw.circle(screen, city.faction.color, (pixelCalculations.getPointXY(city.latitude, city.longitude)), 5)

    #    font = pygame.font.Font(None, 12)
    #    text = font.render(city.name, True, (0, 0, 0))
    #    screen.blit(text, (pixelCalculations.getPointXY(city.latitude, city.longitude)))



    pygame.display.flip()

# Quit Pygame
pygame.quit()