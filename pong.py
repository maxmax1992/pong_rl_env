from ball import Ball
from paddle import Paddle

class Pong():
    def __init__(self):
        self.ball = Ball()
        self.paddle_left = Paddle(True, init_y=200)
        self.paddle_right = Paddle(False, init_y=200)


    def on_event(self, event):
        self.paddle_left.on_event(event)

    def draw(self, surface):
        self.paddle_left.draw(surface)
        self.paddle_right.draw(surface)
        self.ball.draw(surface)

    def update(self, timedelta):
        self.paddle_left.update(timedelta)
        self.paddle_right.update(timedelta)
        self.ball.update(timedelta, self.paddle_left, self.paddle_right)

