from floodsystem.analysis import polyfit
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    #Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    #iterating over top 5 stations
    for i in range(5):
        #gets the dates and levels for the ith station up to the 5th one
        dates, levels = fetch_measure_levels(stations_highest_rel_level(stations,5)[i][0].measure_id, dt=datetime.timedelta(days=2))
        #plot the graph of levels agaisnt date, with polynomial fit, for each station
        plot_water_level_with_fit(stations_highest_rel_level(stations,5)[i][0],dates , levels, 4) 

if __name__ == "__main__":
    run()