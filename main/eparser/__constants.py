""" This module only for common constants """
from collections import namedtuple
from enum import Enum

Channel = namedtuple("Channel", ["service", "package", "service_type",
                                 "ssid", "freq", "rate", "pol", "fec",
                                 "system", "pos", "data_id", "fav_id"])


class Type(Enum):
    """ Types of DVB transponders """
    Satellite = "s"
    Terestrial = "t"
    Cable = "c"


class Polarization(Enum):
    H = 0
    V = 1
    L = 2
    R = 3


class PlsMode(Enum):
    Root = 0
    Gold = 1
    Combo = 2


# Symbol rate
FEC = {0: "None", 1: "Auto", 2: "1/2",
       3: "2/3", 4: "3/4", 5: "5/6",
       6: "7/8", 7: "3/5", 8: "4/5",
       9: "8/9", 10: "9/10"}

SYSTEM = {0: "DVB-S", 1: "DVB-S2"}

MODULATION = {0: "Auto", 1: "QPSK", 2: "8PSK", 3: "16APSK", 5: "32APSK"}

SERVICE_TYPE = {-2: "Unknown", 1: "TV", 2: "Radio", 3: "Data",
                10: "Radio", 12: "Data", 22: "TV", 25: "TV",
                136: "Data", 139: "Data"}