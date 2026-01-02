from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Parameter:
    w_cost : float = 1.0
    w_obj1 : float = 1.0
    w_obj2 : float = 1.0
    timelimit : float = 60.0
    gap : float = 0.01

    def __post_init__(self):
        pass
