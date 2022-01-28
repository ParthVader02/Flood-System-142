# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa

#Task D
def rivers_with_station(stations):
    return {station.river for station in stations if station.name is not None}

def stations_by_river(stations):
    return {station.river: (station.station_id, station.measure_id, station.coord, station.typical_range, station.town) for station in stations}