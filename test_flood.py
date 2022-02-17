from numpy import isin
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

stations = build_station_list()

def test_stations_level_over_threshold():
    #calls function, with a high likelihood of a non-empty list
    overs = stations_level_over_threshold(stations, -10)
    #makes sure function actually has output != None 
    assert overs != None
    #checks output is of correct variable type (list)
    assert isinstance(overs, list)

def test_stations_highest_rel_level():
    #calls function over all stations
    highs = stations_highest_rel_level(stations,len(stations))
    #checks output is of correct variable type (list)
    assert isinstance(highs, list)
    #checks that list is correctly ordered (descending)
    for i in range(len(highs)-1):
        assert highs[i][1] >= highs[i+1][1]