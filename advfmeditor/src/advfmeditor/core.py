from dataclasses import dataclass

@dataclass
class Factors:
    players: int
    fans: int
    management: int
    finances: int
    
    def update(self, other):
        self.players += other.players
        self.fans += other.fans
        self.management += other.management
        self.finances += other.finances

    def any_failed(self) -> bool:
        return any(factor < 1 for factor in [self.players, self.fans , self.management, self.finances])

@dataclass
class Statement:
    text: str
    agree: Factors
    disagree: Factors

class Game:
    def __init__(self, players: int, fans: int, management: int, finances: int):
        self.factors: Factors = Factors(players, fans, management, finances)

    def apply(self, decision: Factors):
        self.factors.update(decision)

    def is_over() -> bool:
        return self.factors.any_failed()