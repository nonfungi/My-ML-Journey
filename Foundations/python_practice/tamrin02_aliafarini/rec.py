class rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def area (self):
        return (self.width* self.height)
    
    def perimeter(self):
        return (2*(self.width + self.height))
    
    def __str__ (self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
rec1 = rectangle(10,8)
print (rec1)

rec2 = rectangle(3,4)
print (rectangle.area(rec2))