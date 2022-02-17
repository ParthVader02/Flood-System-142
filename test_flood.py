from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
def test_stations_level_over_threshold():
    overs = stations_level_over_threshold(stations, -1)
    assert overs != None
    assert isinstance(overs, list)
    