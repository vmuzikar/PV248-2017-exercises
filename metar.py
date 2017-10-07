#!/usr/bin/env python3

import requests
import xml.etree.ElementTree as etree
from datetime import datetime


class Metar:
    urlTemplate = "https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars" \
                  "&requestType=retrieve&format=xml&stationString={station}&hoursBeforeNow=24"

    def __init__(self, station, index):
        self.index = index
        self._url = Metar.urlTemplate.format(station=station)
        self._metarXml = None  # IDE is not happy without this; not sure why
        self.loadData()

    def loadData(self):
        response = requests.get(self._url)
        if response.ok is False:
            raise IOError("Unable to load data from server")
        try:
            self._metarXml = etree.fromstring(response.content).findall("./data/METAR")[self.index]
        except KeyError:
            raise IOError("No data found for given station")

    def __getElementTextByName(self, name):
        return self._metarXml.find("./"+name).text

    @property
    def temperature(self):
        return float(self.__getElementTextByName("temp_c"))

    @property
    def time(self):
        return datetime.strptime(self.__getElementTextByName("observation_time"), "%Y-%m-%dT%H:%M:%SZ")

    @property
    def station(self):
        return self.__getElementTextByName("station_id")


def main():
    metar = Metar("LKTB", 0)
    print("{} {}: {}°C".format(metar.station, metar.time, metar.temperature))


if __name__ == "__main__":
    main()
