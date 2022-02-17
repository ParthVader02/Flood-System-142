from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    "Outputs descending order list of (station object, water level) for which water level is above a given tol value"
    return sorted_by_key([(station, station.relative_water_level()) for station in stations if station.relative_water_level() != None and station.relative_water_level()>tol],1)[::-1]

def stations_highest_rel_level(stations,N):
    "Outputs descending order list of (station object, water level), for the N stations with the highest water level"
    return sorted_by_key([(station, station.relative_water_level()) for station in stations if station.relative_water_level() != None],1)[::-1][:N]   
