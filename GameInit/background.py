from Mappa.constants import options
import gmplot
import Secrets.GoogleAPI as Maps

def gmplotInit():
    gmap = gmplot.GoogleMapPlotter(options.get("lat"), options.get("lng"), options.get("zoom"), apikey=Maps.googleAPIKey)
    return gmap