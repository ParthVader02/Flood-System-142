from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
p=(52.2053, 0.1218)
stations = build_station_list()


x = stations_by_distance(stations, p)

print([(stat_dist[0].name, stat_dist[0].town, stat_dist[1]) for stat_dist in x[:10]],[(stat_dist[0].name, stat_dist[0].town, stat_dist[1]) for stat_dist in x[-10:]])
#y = (station)  x[:10]
#z= x[-10:]

#print (y)
#print(z)