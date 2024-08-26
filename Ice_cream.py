import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
bob = turtle.Turtle()
for b in range(24):
    for i in range(5):
        alex.speed(100000000000000000000000000000000000000^10000000)
        bob.speed(100000000000000000000000000000000000000^10000000)
        alex.forward(50)
        alex.right(72)
        alex.forward(50)
        alex.left(144)
        alex.write(str(i))
        bob.back(50)
        bob.left(72)
        bob.back(50)
        bob.right(144)
        bob.write(str(i))
    alex.forward(10)
    bob.back(10)

wn.mainloop()