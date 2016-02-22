from datetime import datetime
from haversine import haversine
from uberatc.config.strings import *


class Trip:
    """Class representing a trip"""
    def __init__(self, info):
        self.begin_time = self.parse_time(info[BEGIN_TIME])
        self.from_lat = float(info[FROM_LAT])
        self.from_lng = float(info[FROM_LNG])
        self.to_lat = float(info[TO_LAT])
        self.to_lng = float(info[TO_LNG])
        self.user_id = info[USER_ID]

    def get_distance(self):
        try:
            return self.distance
        except AttributeError:
            self.distance = haversine(
                    (self.from_lat, self.from_lng),
                    (self.to_lat, self.to_lng))
            return self.distance

    def parse_time(self, timestr):
        return datetime.strptime(timestr, '%Y-%m-%d_%H:%M:%S')

