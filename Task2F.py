from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    #Build list of stations
    stations = build_station_list()
    top_5 = stations_highest_rel_level(stations, 5)
    dates = []
    levels = []
    for station in top_5:
        dates, levels= fetch_measure_levels(station.measure_id, 2)
        return plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    run()