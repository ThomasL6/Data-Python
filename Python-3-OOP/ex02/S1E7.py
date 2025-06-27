from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_baratheon(cls, name, is_alive=True):
        return cls(name, is_alive)

    def die(self):
        """The character has been killed"""
        self.is_alive = False
        print(f"{self._name} has been slain.")

    def first_name(self):
        """Returns the first name of the character."""
        return self._name


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hair}')"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, name, is_alive=True):
        return cls(name, is_alive)

    def die(self):
        """The character has been killed"""
        self.is_alive = False
        print(f"{self._name} has been slain.")

    def first_name(self):
        """Returns the first name of the character."""
        return self._name
