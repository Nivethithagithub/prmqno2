class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def validate_triangle(self):
        a, b, c = self.sides

        
        if a + b > c and a + c > b and b + c > a:
            return "Valid Triangle"
        else:
            return "Invalid Triangle"


class Rectangle:
    def __init__(self, sides):
        self.sides = sides

    def validate_rectangle(self):
        a, b, c, d = self.sides

        
        if a == c and b == d:
            return "Valid Rectangle"
        else:
            return "Invalid Rectangle"



triangle_sides = list(map(int, input().split()))
rectangle_sides = list(map(int, input().split()))


triangle = Triangle(triangle_sides)
rectangle = Rectangle(rectangle_sides)


triangle_result = triangle.validate_triangle()
print(triangle_result)


rectangle_result = rectangle.validate_rectangle()
print(rectangle_result)
