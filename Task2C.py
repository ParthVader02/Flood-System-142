from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
#sets variables/values
stations = build_station_list()
update_water_levels(stations)
N=10
#cycles through the output list, printing the names and rel_levels
print(*[(station[0].name, station[1]) for station in stations_highest_rel_level(stations,N)], sep = "\n")