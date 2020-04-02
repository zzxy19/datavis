from gmplot import gmplot
from datapoint import *
import math

BASE = 10

class Plotter:
  def __init__(self, location=None, zoom=None):
    apikey = self._load_api_key()
    if location is None:
      location = Location(20, 0)
    if zoom is None:
      zoom = 2
    self.gmap = gmplot.GoogleMapPlotter(location.lat, location.lon, zoom, apikey=apikey)

  def _get_intensity(self, value):
    return math.pow(value, 0.8)
    #return math.sqrt(value)

  def heatmap(self, snapshot, outputFile):
    lat_list, lon_list, weight_list = self._process_snapshot(snapshot)
    self.gmap.heatmap(lat_list, lon_list, weight_list, radius=8, maxIntensity=self._get_intensity(100000))
    self.gmap.draw(outputFile)

  def _process_snapshot(self, snapshot):
    dataPoints = snapshot.getDataPoints()
    lat_list = []
    lon_list = []
    weights = []
    for dp in dataPoints:
      lat_list.append(dp.lat)
      lon_list.append(dp.lon)
      weights.append(self._get_intensity(dp.heat))
    return lat_list, lon_list, weights

  def _load_api_key(self):
    with open('apikey.txt', 'r') as apikeyFile:
      apikey = apikeyFile.read().strip()
    return apikey

def test():
  dpList = [DataPoint(30.9756,112.2707,10000),DataPoint(27.6104,111.7088,100),DataPoint(27.6104,114.7088,1000),DataPoint(27.6104,109.7088,100000)]
  snapshot = WorldSnapshot(dpList)
  plotter = Plotter()
  plotter.heatmap(snapshot, "test.html")

test()