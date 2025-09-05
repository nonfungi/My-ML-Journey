"""
Problem:
- Create a base class Shape with an area() method.
- Implement Rectangle and Circle subclasses that override area().
- Create and test a list of mixed shapes.
"""

from math import pi

# Abstract base class for all shapes.
class Shape:
    # Forces subclasses to implement this method.
    def area(self):
        raise NotImplementedError("Subclasses must implement their own area() method")

# A specific shape that inherits from Shape.
class Rectangle(Shape):
    # Initializes rectangle with width and height.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Overrides the parent method with the correct formula.
    def area(self):
        return self.width * self.height

    # String representation of the rectangle.
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Another specific shape that inherits from Shape.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius**2)

    def __str__(self):
        return f"Circle(radius={self.radius})"

# --- Test Script ---
# Create a list of different shape objects.
shapes = [Rectangle(4, 5), Circle(2), Rectangle(2, 3)]

print("--- Calculating Areas ---")
# Loop through the list and print the area for each shape.
for item in shapes:
    # This demonstrates polymorphism.
    print(f"{item} -> Area: {item.area():.2f}")