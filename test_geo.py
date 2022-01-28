from floodsystem.geo import rivers_with_station 
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def test_rivers_with_station():
    stations = build_station_list()
    river_names =list(rivers_with_station(stations))
    for i in range(len(river_names)):
        assert river_names[i] != river_names[i-1]

def test_stations_by_river():
    stations = build_station_list()
    objects = ((station.station_id, station.measure_id, station.coord, station.typical_range, station.town) for station in stations )
    rivers = stations_by_river(stations)
    assert rivers.values() == objects

