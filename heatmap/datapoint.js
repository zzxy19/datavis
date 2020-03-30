export class DataPoint {
  constructor(lat, lon, heat) {
    this.lat = lat;
    this.lon = lon;
    this.heat = heat;
  }
}

export class TimeSeriesDataPoint {
  constructor(date, dataPoint) {
    this.dataPoint = dataPoint;
    this.date = date;
  }
}

export class TimeSeriesData {
  constructor(timeSeriesDataPoints) {
    this.timeSeriesDataPoints = timeSeriesDataPoints;
  }
}

function timeSeriesDataCompareFunction(tsData1, tsData2) {
  return tsData1.date.getTime() - tsData2.date.getTime();
}

export class TimeSeriesDataBuilder {
  constructor() {
    this.unsortedTSDataPoints = [];
  }

  addDataPoint(date, dataPoint) {
    return addTimeSeriesDataPoint(new TimeSeriesDataPoint(date, dataPoint));
  }

  addTSDataPoint(timeSeriesDataPoint) {
    this.unsortedTSDataPoints.push(timeSeriesDataPoint);
    return this;
  }

  getData() {
    this.unsortedTSDataPoints.sort(timeSeriesDataCompareFunction)
    return new TimeSeriesData(this.unsortedTSDataPoints)
  }
}