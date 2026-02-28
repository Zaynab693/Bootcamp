import math

class Circle:
    # Step 1: Initialize the circle with radius
    def __init__(self, radius):
        self.radius = radius

    # Step 2: Create a property to calculate diameter
    @property
    def diameter(self):
        return self.radius * 2

    # Step 3: Optional setter to create circle from diameter
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    # Step 4: Compute the area
    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    # Step 5: String representation
    def __str__(self):
        return f"Circle with radius: {self.radius:.2f}"

    def __repr__(self):
        return f"Circle({self.radius})"

    # Step 6: Addition of two circles (returns new circle)
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError("Can only add Circle to Circle")

    # Step 7: Comparison: greater than
    def __gt__(self, other):
        return self.radius > other.radius

    # Step 8: Comparison: equal
    def __eq__(self, other):
        return self.radius == other.radius

    # Step 9: Less than for sorting
    def __lt__(self, other):
        return self.radius < other.radius

#----------------------------------------------------------------------------------------------------------------------------------
#Bonus: Visualizing sorted circles with turtle graphics
import turtle
import math

# ===== Circle class (same as before) =====
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius:.2f}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError("Can only add Circle to Circle")

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

# ===== Create circles and sort them =====
c1 = Circle(50)
c2 = Circle(30)
c3 = Circle(70)
c4 = Circle(20)

circles = [c1, c2, c3, c4]
circles.sort()  # sort by radius

# ===== Turtle setup =====
screen = turtle.Screen()
screen.title("Sorted Circles Visualization")
t = turtle.Turtle()
t.speed(1)

# Starting x position
x_pos = -200

# Draw each circle in sorted order
for circle in circles:
    t.penup()
    t.goto(x_pos, 0)  
    t.pendown()
    t.circle(circle.radius) 
    x_pos += circle.radius * 2 + 20  
turtle.done()  
