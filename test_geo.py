from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number, stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    #builds list of stations
    stations= build_station_list()
    #checks that Cambridge is the closest station to a point in Cambridge
    assert stations_by_distance(stations, (52.2053, 0.1218))[0].town == "Cambridge" 


def test_rivers_with_station():
    #Build stations database
    stations = build_station_list()
    #Get list of rivers with at least 1 station
    river_names =list(rivers_with_station(stations))
    #check that there are no duplicates
    for i in range(len(river_names)):
        assert river_names[i] != river_names[i-1]
    

def test_stations_by_river():
    stations = build_station_list()
    objects=[station.name for station in stations]
    #get list of stations by river check they agree with the real data
    rivers = list(stations_by_river(stations).values())
    assert rivers.sort()== objects.sort()

def test_rivers_by_station_number():
    stations = build_station_list()
    N=9
    #get numbers of stations in top 9 
    by_number = [x[1] for x in rivers_by_station_number(stations, N)]
    #check that it is ordered in descending order
    for i in range(1,len(by_number)):
        assert by_number[i] <= by_number[i-1]