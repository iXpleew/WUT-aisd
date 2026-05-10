from dataclasses import dataclass

@dataclass
class Destination:
    destination: str
    lenght: float
    morning_time: int
    noon_time: int
    evening_time: int

    def night_time(self) -> float:
        return 75/100 * self.noon_time