from math import *
from fractions import Fraction
import turtle as trtl

print()
print("Graph Parametric Motion!")

while True:
    print()
    shape1 = input("First Shape: ").replace(" ", "").lower()
    if shape1 == "c" or shape1 == "circle":
        r1 = float(input("Radius: ").replace(" ", ""))
        p1 = float(input("Period: ").replace(" ", ""))
        def Shape1Graph(t):
            return r1 * cos(tau / p1 * t), r1 * sin(tau / p1 * t) 
    elif shape1 == "e" or shape1 == "ellipse":
        a1 = float(input("Major Axis: ").replace(" ", ""))
        b1 = float(input("Minor Axis: ").replace(" ", ""))
        d1 = input("Hoizontal or Vertical: ").replace(" ", "").lower()
        p1 = float(input("Period: ").replace(" ", ""))
        if d1 == "h" or d1 == "hor" or d1 == "horizontal":
            def Shape1Graph(t):
                return a1 * cos(tau / p1 * t), b1 * sin(tau / p1 * t)
        elif d1 == "v" or d1 == "ver" or d1 == "vertical":
            def Shape1Graph(t):
                return b1 * cos(tau / p1 * t), a1 * sin(tau / p1 * t)
    elif shape1 == "p" or shape1 == "polar":
        print("Enter values for r = a sin(bθ) + c")
        a1 = float(input("a: ").replace(" ", ""))
        b1 = float(input("b: ").replace(" ", ""))
        p1 = tau
        c1 = float(input("c: ").replace(" ", ""))
        op1 = input("Sine or Cosine: ").replace(" ", "").lower()
        if op1 == "s" or op1 == "sin" or op1 == "sine":
            def Shape1Graph(t):
                r = a1 * sin(b1 * t) + c1
                return r * cos(t), r * sin(t)
        elif op1 == "c" or op1 == "cos" or op1 == "cosine":
            def Shape1Graph(t):
                r = a1 * cos(b1 * t) + c1
                return r * cos(t), r * sin(t)
    else: continue

    print()
    position = "centered"
    shape2 = input("Second Shape: ").replace(" ", "").lower()
    if shape2 == "c" or shape2 == "circle":
        r2 = float(input("Radius: ").replace(" ", ""))
        p2 = float(input("Period: ").replace(" ", ""))
        pos = input("Roll centered, outside, or inside: ")
        if pos == "centered" or pos == "c": position = "centered"
        elif pos == "outside" or pos == "o": position = "outside"
        elif pos == "inside" or pos == "i": position = "inside"
        def Shape2Graph(t):
            return r2 * cos(tau / p2 * t), r2 * sin(tau / p2 * t) 
    elif shape2 == "e" or shape2 == "ellipse":
        a2 = float(input("Major Axis: ").replace(" ", ""))
        b2 = float(input("Minor Axis: ").replace(" ", ""))
        d2 = input("Hoizontal or Vertical: ").replace(" ", "").lower()
        p2 = float(input("Period: ").replace(" ", ""))
        if d2 == "h" or d2 == "hor" or d2 == "horizontal":
            def Shape2Graph(t):
                return a2 * cos(tau / p2 * t), b2 * sin(tau / p2 * t)
        elif d2 == "v" or d2 == "ver" or d2 == "vertical":
            def Shape2Graph(t):
                return b2 * cos(tau / p2 * t), a2 * sin(tau / p2 * t)
    elif shape2 == "p" or shape2 == "polar":
        print("Enter values for r = asin(bθ)+c")
        a2 = float(input("a: ").replace(" ", ""))
        b2 = float(input("b: ").replace(" ", ""))
        p2 = tau
        c2 = float(input("c: ").replace(" ", ""))
        op2 = input("Sine or Cosine: ").replace(" ", "").lower()
        if op2 == "s" or op2 == "sin" or op2 == "sine":
            def Shape2Graph(t):
                r = a2 * sin(b2 * t) + c2
                return r * cos(t), r * sin(t)
        elif op2 == "c" or op2 == "cos" or op2 == "cosine":
            def Shape2Graph(t):
                r = a2 * cos(b2 * t) + c2
                return r * cos(t), r * sin(t)
    else: continue
    break

screen = trtl.Screen()
screen.tracer(0)
trtl.setworldcoordinates(-100, -100, 100, 100)
graphTurtle = trtl.Turtle()
graphTurtle.color("black")
graphTurtle.speed(0)
graphTurtle.penup()
graphTurtle.goto(Shape1Graph(0))
graphTurtle.pendown()
t = 0
while t < p1:
    graphTurtle.goto(Shape1Graph(t))
    t += 0.01
graphTurtle.color("red")
shapeTurtle = trtl.Turtle()
shapeTurtle.color("blue")
shapeTurtle.speed(0)
shapeTurtle.hideturtle()

def ShapeCenter(t):
    if position == "centered":
        return Shape1Graph(t)
    elif position == "outside":
        angle = atan2(Shape1Graph(i))
        return tuple(map(sum, zip(Shape1Graph(t), (r2 * cos(angle), r2 * sin(angle)))))
    elif position == "inside":
        angle = atan2(Shape1Graph(i))
        return tuple(map(sum, zip(Shape1Graph(t), (-r2 * cos(angle), -r2 * sin(angle)))))

def Graph(t, i):
    return tuple(map(sum, zip(ShapeCenter(t), Shape2Graph(i))))

t = 0
graphTurtle.penup()
graphTurtle.goto(Graph(0, 0))
graphTurtle.pendown()
while t < lcm(Fraction(p1).numerator, Fraction(p2).numerator) / gcd(Fraction(p1).denominator, Fraction(p2).denominator):
    shapeTurtle.clear()
    shapeTurtle.penup()
    shapeTurtle.goto(ShapeCenter(t))
    shapeTurtle.pendown()
    shapeTurtle.dot(5)
    shapeTurtle.goto(Graph(t, t))
    shapeTurtle.penup()
    shapeTurtle.goto(Graph(t, 0))
    shapeTurtle.pendown()
    i = 0
    while i < p2:
        shapeTurtle.goto(Graph(t, i))
        i += 0.01
    graphTurtle.goto(Graph(t, t))
    screen.update()
    t += 0.01
screen.mainloop()