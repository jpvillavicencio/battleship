from enum import Enum

class Status(Enum):
    EMPTY = 1
    SHIP = 2
    MISSED = 3
    HIT = 4

class Orientation(Enum):
    VERTICAL = 1
    HORIZONTAL = 2
