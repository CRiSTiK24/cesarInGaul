import pandas as pd
def loadDatabase():
    cityData = pd.read_csv("CSV/Hanson2016_Cities_OxREP.csv", encoding = "ISO-8859-1")
    #cityData = cityData[cityData['Start Date'] < -58]  #We want the cities that existed pre 58 b.C
    #There are only 4 cities pre-roman conquest in the database, so I'll need to get a little ahistorical
    filteredCityData = cityData.filter(['Ancient Toponym','Province','Longitude (X)','Latitude (Y)'])
    gallia = ["Gallia Aquitania","Gallia Belgica","Gallia Lugdunensis","Gallia Narbonensis"]
    gallicCityData = filteredCityData[filteredCityData['Province'].isin(gallia)]
    return gallicCityData

print(loadDatabase())