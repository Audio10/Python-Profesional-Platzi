"""dataclasses are a feature from python 3.7"""
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Position:
  lat: float = field(default=0.0, metadata={'unit': 'degrees'})
  lon: float = field(default=0.0, metadata={'unit': 'degrees'})


@dataclass(frozen=True)
class Town(Position):
  name: str = None


@dataclass(frozen=True)
class Capital(Town):
  pass


@dataclass
class Country:
  code: str
  towns: List[Town] = field(default_factory=list)

  def get_capital(self):
    try:
      return list(filter(lambda x: isinstance(x, Capital), self.towns)).__getitem__(0)
    except IndexError:
      return None


if __name__ == '__main__':
  paris = Capital(2.3522219, 48.856614, 'Paris')
  san_francisco = Town(37.6216, -122.3929, 'San Francisco')
  washington = Capital(47.751076, -120.740135, 'Washington')
  united_states = Country('US', [san_francisco, washington])
  print(united_states.get_capital())
