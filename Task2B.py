from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
#sets variables/values
stations = build_station_list()
update_water_levels(stations)
tol = 0.8
stations_over =stations_level_over_threshold(stations, tol)
#cycles through the output list, printing the names and rel_levels
print(*[(station[0].name, station[1]) for station in stations_over], sep = "\n")
