from dataclasses import dataclass

@dataclass
class Destination:
    destination: str
    length: float
    morning_time: float
    noon_time: float
    evening_time: float

    def night_time(self) -> float:
        return 75/100 * self.noon_time