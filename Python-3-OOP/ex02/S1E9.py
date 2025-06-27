from abc import ABC, abstractmethod


class Character(ABC):
    """This class represents a character in the game."""
    def __init__(self, name, is_alive=True):
        """Instantiates a character with a name and an alive status."""
        self._name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """The character has been slain"""
        self.is_alive = False
        print(f"{self._name} has been slain.")


class Stark(Character):
    """This class represents a Stark character."""

    def die(self):
        """The character has been killed"""
        return super().die()
