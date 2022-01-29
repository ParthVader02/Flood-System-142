# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
from collections import defaultdict
#Task D
def rivers_with_station(stations):
    return {station.river for station in stations if station.station_id and station.name and station.measure_id !=None}

def stations_by_river(stations):
    station_list = [(station.river, station.name) for station in stations]
    by_river = defaultdict(list)
    for river, name in station_list:
        by_river[river].append(name)
    return by_river
