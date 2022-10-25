class Rectangle:
    def __init__(self, length=4, width=4):
        if(length > 0 and length <= 100):
            self.__length = length
        else:
            raise ValueError("the length of the rectangle cannot exceed 100 cm")
        if(width > 0 and width <= 100):
            self.__width = width
        else:
            raise ValueError("the width of the rectangle cannot exceed 100 cm")

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def area(self):
        return self.__length * self.__width


print("enter the length of the rectangle:")
l = int(input())
print("enter the width of the rectangle:")
w = int(input())
rctngl = Rectangle(l, w)
print("enter 1 to calculate the perimeter of the rectangle and 2 to calculate the area:")
if(int(input()) == 1):
    print(rctngl.perimeter())
else:
    print(rctngl.area())