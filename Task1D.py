from floodsystem.geo import rivers_with_station 
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    #Build list of stations
    stations = build_station_list()

    #Print number of rivers with at least 1 monitoring station
    rivers = list(rivers_with_station(stations))
    print(len(rivers), "stations")

    #Print first 10 of these rivers in alphabetical order
    rivers.sort()
    print(rivers[0:10])

    #Print names of stations located on the rivers
    by_river = stations_by_river(stations)
    river_aire = by_river['River Aire']
    river_cam = by_river['River Cam']
    river_thames = by_river['River Thames']
    river_aire.sort()
    river_cam.sort()
    river_thames.sort ()
    print('River Aire:', river_aire)
    print('River Cam:', river_cam)
    print('River Thames:',river_thames)
    

if __name__ == "__main__":
    run()