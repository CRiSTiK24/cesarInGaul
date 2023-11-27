# from: https://stackoverflow.com/questions/47106276/converting-pixels-to-latlng-coordinates-from-google-static-image
import math

w = 1280
h = 1280
zoom = 6
centerLat = 46.672997
centerLng = 1.77489

parallelMultiplier = math.cos(centerLat * math.pi / 180)
degreesPerPixelX = 360 / math.pow(2, zoom + 8)
degreesPerPixelY = 360 / math.pow(2, zoom + 8) * parallelMultiplier


def getPointXY(lat, lng):
    y = (centerLat - lat)/degreesPerPixelY + h/2
    x = (centerLng - lng)/degreesPerPixelX + w/2
    return (x, y)


def getPointLatLng(x, y):

    lat = centerLat - degreesPerPixelY * (y - h / 2)
    lng = centerLng + degreesPerPixelX * (x - w / 2)

    return (lat, lng)

