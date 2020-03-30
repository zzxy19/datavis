from datetime import datetime

class Location:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

class DataPoint:
  def __init__(self, lat, lon, heat):
    self.lat = lat
    self.lon = lon
    self.heat = heat

class WorldSnapshot:
  def __init__(self, dataPoints):
    self.dataPoints = dataPoints

  def getDataPoints(self):
    return self.dataPoints

class TimeSeriesWorldSnapshots:
  def __init__(self, timeSeriesSnapshots):
    self.timeSeriesSnapshots = timeSeriesSnapshots

class TimeSeriesWorldSnapshotsBuilder:
  def __init__(self):
    self.timeSeriesSnapshots = {}

  def addSnapshot(self, dt, snapshot):
    self.timeSeriesSnapshots[dt] = snapshot
    return self

  def build(self):
    return TimeSeriesWorldSnapshots(self.timeSeriesSnapshots)
