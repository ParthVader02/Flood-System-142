import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

# initialise station list
stations = build_station_list()
update_water_levels(stations)

# iterate over top 5 stationss
for i in range(5):
    # sets date/level lists for i-th highest station
    dates, levels = fetch_measure_levels(stations_highest_rel_level(stations,5)[i][0].measure_id, dt=datetime.timedelta(days=10))
    # plots time series for that i-th station 
    plot_water_levels(stations_highest_rel_level(stations,5)[i][0],dates , levels)