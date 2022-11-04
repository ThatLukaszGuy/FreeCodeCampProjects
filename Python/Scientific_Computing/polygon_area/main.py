import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
      return f"Rectangle(width={self.width}, height={self.height})"
  
    def set_width(self, width):
        self.width = width
        return self.width
      
    def set_height(self, height):
        self.height = height
        return self.height
      
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return "Too big for picture."
        else:
          picture = f""
          for i in range(0, self.height):
              picture += (self.width * '*') + '\n'
          return picture
          
    def get_amount_inside(self, other_shape):
        area = self.get_area()
        other_area = other_shape.height * other_shape.width
        return math.floor(area / other_area)

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __repr__(self):
      return f"Square(side={self.width})"
      
    def set_side(self, side):
        self.width = side
        self.height = side   

    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)
        
        
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))