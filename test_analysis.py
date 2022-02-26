import datetime
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.dates

stations = build_station_list()
update_water_levels(stations)
def test_polyfit():
    for i in range(5):
        #gets the dates and levels for the ith station up to the 5th one
        dates, levels = fetch_measure_levels(stations_highest_rel_level(stations,5)[i][0].measure_id, dt=datetime.timedelta(days=2))
        x = matplotlib.dates.date2num(dates)
        if dates:
            poly, d0 = polyfit(dates, levels, 4)
            assert d0 == x[0]
            assert max(poly) <= max(levels)
            