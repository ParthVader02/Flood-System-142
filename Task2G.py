import datetime
from floodsystem.plot import plot_water_level_with_fit
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    #Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    #initalise flood risk categories
    severe = []
    high = []
    moderate = []
    low = []    
    #goes through all stations
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        if not levels:
            pass
        else:
            #finds gradient
            rate = np.gradient(levels)
            #sum gradient to get what the general increase is 
            grad_sum = sum(rate)

            if grad_sum < 0.01:
                low.append((station.town, grad_sum))
            elif grad_sum >=0.01 and grad_sum < 0.1:
                moderate.append((station.town, grad_sum))
            elif grad_sum >= 0.1 and grad_sum < 0.7:
                high.append((station.town, grad_sum))
            elif grad_sum >= 0.7:
                severe.append((station.town, grad_sum))    
    severe.sort()        
    print(severe[0:4])

if __name__ == "__main__":
    run()