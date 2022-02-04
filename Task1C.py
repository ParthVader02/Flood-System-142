from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
#define variables
x= build_station_list()
centre=(52.2053, 0.1218)
r=10
#extraxt names and sort alphabetically
print(sorted([station.name for station in stations_within_radius(x, centre, r)]))