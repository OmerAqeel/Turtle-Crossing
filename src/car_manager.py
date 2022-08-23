from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []

    def generate_cars(self):
        random_dice = random.randint(1, 5)
        if random_dice == 1:                    # Just to make sure that only few number of cars are being produced (this will make it easier for the turtle to cross the road)
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=1.5)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)




