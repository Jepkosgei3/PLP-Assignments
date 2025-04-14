class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Base move method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def speak(self):
        """Base speak method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")


class Bird(Animal):
    def move(self):
        """Birds fly through the air"""
        return f"{self.name} the bird is flying! 🕊️"
    
    def speak(self):
        """Bird's sound"""
        return f"{self.name} says: Tweet tweet! 🎵"


class Fish(Animal):
    def move(self):
        """Fish swim in water"""
        return f"{self.name} the fish is swimming! 🐠"
    
    def speak(self):
        """Fish don't make sounds (usually)"""
        return f"{self.name} bubbles quietly... 💭"


class Snake(Animal):
    def move(self):
        """Snakes slither on the ground"""
        return f"{self.name} the snake is slithering! 🐍"
    
    def speak(self):
        """Snake's sound"""
        return f"{self.name} hisses: Sssss... 🎶"


class Horse(Animal):
    def move(self):
        """Horses gallop"""
        return f"{self.name} the horse is galloping! 🐎"
    
    def speak(self):
        """Horse's sound"""
        return f"{self.name} neighs: Neighhh! 🎤"


# Demonstration of polymorphism
if __name__ == "__main__":
    animals = [
        Bird("Sky"),
        Fish("Bubbles"),
        Snake("Viper"),
        Horse("Thunder")
    ]
    
    print("=== Animal Movement Demonstration ===")
    for animal in animals:
        print(animal.move())
    
    print("\n=== Animal Sounds ===")
    for animal in animals:
        print(animal.speak())
