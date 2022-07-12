from enum import Enum, auto

QUAIL_VALID_INFOS: dict[str, bool] = {
    "Name": True,
    "Flyable-version": True,
    "Description": True,
    "Timeout": False,
    "No-Wrap": False,
    "Dependencies": False,
}
""" 
A dictionary of valid infos. The keys are the names of the infos, and the values are booleans. 

True means the info is required, False means it is optional. 
"""


class QuailTestState(Enum):
    New = auto()
    Infos = auto()
    Start = auto()
    Body = auto()
    None_ = auto()
    End = auto()
