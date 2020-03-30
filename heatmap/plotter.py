from gmplot import gmplot
from datapoint import *

class Plotter:
  def __init__(self, location=None, zoom=None):
    apikey = self._load_api_key()
    if location is None:
      location = Location(0, 0)
    if zoom is None:
      zoom = 2
    self.gmap = gmplot.GoogleMapPlotter(location.lat, location.lon, zoom, apikey=apikey)

  def heatmap(self, snapshot, outputFile):
    lat_list, lon_list = self._process_snapshot(snapshot)
    self.gmap.heatmap(lat_list, lon_list)
    self.gmap.draw(outputFile)

  def _process_snapshot(self, snapshot):
    dataPoints = snapshot.getDataPoints()
    lat_list = []
    lon_list = []
    for dp in dataPoints:
      lat_list += [dp.lat] * dp.heat
      lon_list += [dp.lon] * dp.heat
    return lat_list, lon_list

  def _load_api_key(self):
    with open('apikey.txt', 'r') as apikeyFile:
      apikey = apikeyFile.read().strip()
    return apikey

def test():
  dpList = [DataPoint(30.9756,112.2707,10000),DataPoint(27.6104,111.7088,1000)]
  snapshot = WorldSnapshot(dpList)
  plotter = Plotter()
  plotter.heatmap(snapshot, "test.html")

test()