from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    #Build list of stations
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)
    inconsistent.sort()
    print(inconsistent)
if __name__ == "__main__":
    run()