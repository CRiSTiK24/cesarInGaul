import geopandas as gpd
import pygame
import loadCSV
from ObjectClasses.city import City

# Load your filtered DataFrame with Roman cities using loadCSV module
filteredCityData = loadCSV.loadDatabase()

# Create a list of City objects
cities = [City(row['Ancient Toponym'], row['Longitude (X)'], row['Latitude (Y)']) for index, row in filteredCityData.iterrows()]

# Set up Pygame
pygame.init()
screen_width, screen_height = 1000, 1000  # Adjust the window size as needed
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Roman Cities Map')

# Map the City objects to screen coordinates with padding
max_longitude, min_longitude = max(city.longitude for city in cities), min(city.longitude for city in cities)
max_latitude, min_latitude = max(city.latitude for city in cities), min(city.latitude for city in cities)

for city in cities:
    city.screen_x = (city.longitude - min_longitude) / (max_longitude - min_longitude) * (screen_width*0.9)
    city.screen_y = screen_height - ((city.latitude - min_latitude) / (max_latitude - min_latitude) * (screen_height*0.9))

# Pygame main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw cities as points on the screen
    for city in cities:
        pygame.draw.circle(screen, (0, 0, 255), (int(city.screen_x), int(city.screen_y)), 5)

        # Display city names
        font = pygame.font.Font(None, 24)
        text = font.render(city.name, True, (0, 0, 0))
        screen.blit(text, (int(city.screen_x), int(city.screen_y) - 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()