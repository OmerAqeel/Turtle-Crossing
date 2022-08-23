import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManage = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)

in_the_game = True
while in_the_game:
    time.sleep(0.1)
    screen.update()
    carManage.generate_cars()
    carManage.move_cars()

#Detecting the collision between the cars and the turtle
    for c in carManage.all_cars:
        if player.distance(c) <20:
            print("Squish !!")
            in_the_game = False

