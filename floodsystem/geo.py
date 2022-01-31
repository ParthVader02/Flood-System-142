# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from calendar import c
from .utils import sorted_by_key  # noqa
from collections import defaultdict
from collections import Counter
import numpy as np

#Task D
def rivers_with_station(stations):
    # Get river names for rivers with at least 1 station
    return {station.river for station in stations if station.station_id and station.name and station.measure_id !=None}

def stations_by_river(stations):
    #Get list of tuples 
    station_list = [(station.river, station.name) for station in stations]
    #Initialise defaultdict object from collections
    by_river = defaultdict(list)
    #append to defaultdict with each river as key, and names as values
    for river, name in station_list:
        by_river[river].append(name)
    return by_river

#Task 1E
def rivers_by_station_number(stations, N):
    #Call function from Task 1D to get a dict with rivers as keys
    by_river = stations_by_river(stations)
    #initialise list 
    number = list()
    #loop through rivers and get station names
    for river in by_river:
        station_names = list(by_river[river])
        #Get the number of stationf for each river
        n = len(station_names)
        #append to list of tuples
        number.append((river, n))
    #sort by top N in descending order
    top_N = sorted(number, key = lambda x: x[1], reverse = True)[:N]
    return top_N
        