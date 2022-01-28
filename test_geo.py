from floodsystem.geo import rivers_with_station
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list


def test_rivers_with_station():
    stations = build_station_list()
    river_names = rivers_with_station(stations)
    print(len(river_names))
    print(river_names)
test_rivers_with_station()