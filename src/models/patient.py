from dataclasses import dataclass
from typing import Optional

@dataclass
class Patient:
    id:str
    name:str
    age:int
    weight: Optional[float] = None
    height: Optional[float] = None