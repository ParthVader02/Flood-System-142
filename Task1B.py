from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
#define variables
p=(52.2053, 0.1218)
stations = build_station_list()
#generate sorted list of stations and distance
x = stations_by_distance(stations, p)
#slice lists into closest and farthest, picking out names, towns and distances from the list
print([(stat_dist[0].name, stat_dist[0].town, stat_dist[1]) for stat_dist in x[:10]],[(stat_dist[0].name, stat_dist[0].town, stat_dist[1]) for stat_dist in x[-10:]])
