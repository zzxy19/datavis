from typing import List
import datetime.datetime

class DataPoint:
  def __init__(self, lat: float, lon: float, heat: float):
    self.lat = lat
    self.lon = lon
    self.heat = heat

class WorldSnapshot:
  def __init__(self, dataPoints: List[DataPoint]):
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
