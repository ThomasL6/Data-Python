from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a character that is both Baratheon and Lannister."""
    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def get_eyes(self):
        """Returns the eye color of the character."""
        return self.eyes

    def set_eyes(self, color):
        """Sets the eye color of the character."""
        self.eyes = color

    def get_hairs(self):
        """Returns the hair color of the character."""
        return self.hairs

    def set_hairs(self, color):
        """Sets the hair color of the character."""
        self.hairs = color
