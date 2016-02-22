from collections import defaultdict
from gen_utils import *
from trip import Trip
from uberatc.config.strings import *
from uberatc.config.settings import *

import csv
import logging


class DataModel:
    """Class for reading and managing raw data"""
    def __init__(self, train_file):
        self.train_file = train_file
        self.logger = logging.getLogger(LOGGER)
        self.data = None


    def read_train_data(self, to_read_count=-1):
        self.data = []
        """Reads data file"""
        read_count = 0
        with open(self.train_file,'r') as train_f:
            reader = csv.DictReader(train_f)
            for row in reader:
                trip = Trip(row)
                read_count += 1
                self.data.append(trip)
                if to_read_count > 0 and read_count >= to_read_count:
                    break
            #endfor
        #endwith



