import numpy as np
import pygame
from Box2D import (b2CircleShape, b2FixtureDef, b2LoopShape, b2PolygonShape,
                   b2RevoluteJointDef, b2_pi)
import inspect

class Ball():
    def __init__(self):
        self.max_h = 400
        self.max_w = 640

        self.speed = 30
        max_deg = np.random.randint(45)
        self.curr_angle = np.random.randint(2*max_deg) - max_deg
        if np.random.random() > 0.5:
            self.curr_angle += 180
        self.radius = 5
        self.curr_angle = np.deg2rad(self.curr_angle)

        self.x = self.max_w / 2
        self.y = self.max_h / 2
        self.speed_x = np.cos(self.curr_angle)*self.speed
        self.speed_y = np.sin(self.curr_angle)*self.speed

        self.rect = pygame.Rect((self.x - self.radius, self.y - self.radius), 
                (self.radius, self.radius))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def update(self, td, paddle_1, paddle_2):

        if self.rect.colliderect(paddle_1.rect):
            self.speed_x *= -1
        elif self.rect.colliderect(paddle_2.rect):
            self.speed_x *= -1
        else:
            self.speed_x *= 1

        self.y += td*self.speed_y*0.01
        self.x += td*self.speed_x*0.01

        if self.y >= self.max_h:
            remainder = self.y - self.max_h
            self.y = self.max_h - remainder
            self.speed_y *= -1
        elif self.y < 0:
            self.y = -self.y
            self.speed_y *= -1

        if self.x >= self.max_w:
            remainder = self.x - self.max_w
            self.x = self.max_w - remainder
            self.speed_x *= -1
        elif self.x < 0:
            self.x = -self.x
            self.speed_x *= -1

        self.rect.center = (self.x, self.y)
