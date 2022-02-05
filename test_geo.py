from tokenize import Floatnumber
from typing import List
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number, stations_by_distance, stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
stations = build_station_list()

def test_stations_by_distance():
    #checks that Cambridge is the closest station to a point in Cambridge
    assert stations_by_distance(stations, (52.2053, 0.1218))[0][0].town == "Cambridge" 
    #checks all stations appear in sorted list
    for i in range(len(stations)):
        assert stations[i].name in [station[0].name for station in stations_by_distance(stations, (1,1))]

def test_stations_within_radius():
    #calls function
    x= stations_within_radius(stations, (52.2053, 0.1218),10)
    #checks all list entries are MonitoringStation variables
    for i in range(len(x)):
        assert type(x[i]) == MonitoringStation

def test_rivers_with_station():
    #Get list of rivers with at least 1 station
    river_names =list(rivers_with_station(stations))
    #check that there are no duplicates
    for i in range(len(river_names)):
        assert river_names[i] != river_names[i-1]
    

def test_stations_by_river():
    objects=[station.name for station in stations]
    #get list of stations by river check they agree with the real data
    rivers = list(stations_by_river(stations).values())
    assert rivers.sort()== objects.sort()

def test_rivers_by_station_number():
    N=9
    #get numbers of stations in top 9 
    by_number = [x[1] for x in rivers_by_station_number(stations, N)]
    #check that it is ordered in descending order
    for i in range(1,len(by_number)):
        assert by_number[i] <= by_number[i-1]