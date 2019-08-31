#__author__ = Mohammad Abdin

# Define a class named Shape and its subclasses Square and Circle.
# Each shape will have a method of area and a method of perimeter
# (default value of both is 0).

class Shape:
    shape_area = 0
    shape_perimeter = 0

#################################
class Square(Shape):


    def __init__(self,length):
        self.shape_area = length*length
        self.shape_perimeter = length*2

    def area(self):
        return self.shape_area

    def perimeter(self):
        return self.shape_perimeter

#################################
class Circle(Shape):

    def __init__(self, radius):
        self.shape_area = radius**2 * 3.14
        self.shape_perimeter = 2 * radius * 3.14

    def area(self):
        return self.shape_area

    def perimeter(self):
        return self.shape_perimeter


square = Square(3)
print("square's perimeter is : {}".format(square.perimeter()))
print("square's area is : {}\n".format(square.area()))

circle  = Circle(3)
print("circle's perimeter is : {}".format(circle.perimeter()))
print("circle's area is : {}".format(circle.area()))


