class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Return a string containing the cat's name and a message."""
        return f"{self.name} says Meow!"
