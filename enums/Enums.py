from enum import Enum
from datetime import timedelta

class Periods(Enum):
   seven = timedelta(days = 7)
   month = timedelta(days = 30)
   sixmonths = timedelta(days = 180)
   year = timedelta(days = 360)
   max = timedelta(days = 999)