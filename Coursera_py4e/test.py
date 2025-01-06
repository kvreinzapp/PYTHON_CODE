from abc import ABC, abstractmethod
from typing import List


class Fighter(ABC):
    """Abstract base class for all fighter types."""

    def __init__(self, strength: int):
        self.strength = strength

    @abstractmethod
    def get_special_bonus(self) -> int:
        """Return any special bonus the fighter type provides."""
        pass

    def get_total_strength(self) -> int:
        """Calculate total strength including special bonus."""
        return self.strength + self.get_special_bonus()


class Swordsman(Fighter):
    """A fighter specializing in sword combat."""

    def get_special_bonus(self) -> int:
        return 2  # Swordsmen get +2 strength bonus


class Archer(Fighter):
    """A fighter specializing in ranged combat."""

    def get_special_bonus(self) -> int:
        return 1  # Archers get +1 strength bonus


class Knight(Fighter):
    """A heavily armored fighter on horseback."""

    def get_special_bonus(self) -> int:
        return 3  # Knights get +3 strength bonus


class Army:
    """A collection of fighters that can work together."""

    def __init__(self, fighters: List[Fighter]):
        self.fighters = fighters

    def get_total_strength(self) -> int:
        """Calculate the total strength of the army including all bonuses."""
        return sum(fighter.get_total_strength() for fighter in self.fighters)

    def add_fighter(self, fighter: Fighter) -> None:
        """Add a new fighter to the army."""
        self.fighters.append(fighter)

    def get_fighter_count(self) -> int:
        """Return the total number of fighters in the army."""
        return len(self.fighters)


# Example usage
def main():
    # Create some fighters
    knight = Knight(strength=10)
    archer = Archer(strength=7)
    swordsman = Swordsman(strength=8)

    # Create an army with these fighters
    army = Army([knight, archer, swordsman])

    # Print individual fighter strengths (including bonuses)
    print(f"Knight strength: {knight.get_total_strength()}")  # 13 (10 + 3)
    print(f"Archer strength: {archer.get_total_strength()}")  # 8 (7 + 1)
    print(
        f"Swordsman strength: {swordsman.get_total_strength()}")  # 10 (8 + 2)

    # Print total army strength
    print(f"Total army strength: {army.get_total_strength()}")  # 31

    # Add another fighter
    army.add_fighter(Swordsman(strength=9))
    print(f"New army strength: {army.get_total_strength()}")  # 42
    print(f"Total fighters: {army.get_fighter_count()}")  # 4


if __name__ == "__main__":
    main()
