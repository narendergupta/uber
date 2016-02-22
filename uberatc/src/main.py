from datamodel import DataModel
from experimenter import Experimenter
from haversine import haversine
from uberatc.config.strings import *
from uberatc.config.settings import *

import argparse
import logging
import statistics as stats
import time


def main(args):
    dm = DataModel(args.train_file)
    dm.read_train_data()
    exp = Experimenter(dm)
    distances = [x.get_distance() for x in dm.data]
    print(max(distances))
    print(min(distances))
    print(stats.mean(distances))
    t1 = time.time()
    t2 = time.time()
    timeused = t2 - t1
    logging.getLogger(LOGGER).info('Time used in experiment (hour:min:sec): %d:%d:%d' % \
            (timeused/3600, timeused/60, timeused%60))
    return exp


if __name__ == '__main__':
    logging.basicConfig(level=LOG_LEVEL)
    logger = logging.getLogger(LOGGER)
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_file", default=DEFAULT_TRAIN_PATH, required=False)
    parser.add_argument("--test_file", default=DEFAULT_TEST_PATH, required=False)
    args = parser.parse_args()
    exp = main(args)

