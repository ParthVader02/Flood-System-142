# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa

#Task D.1
def rivers_with_station(stations):
    return {station.river for station in stations if station.name is not None}

