import pygame
from pygame.draw import rect

class Paddle():
    def __init__(self, is_left=True, init_y=199):
        self.move_multiplier = None
        self.speed = 5
        self.height = 40
        self.width = 5
        self.left = 20 if is_left else 640 - 20 - self.width
        self.y = init_y - self.width/2
        self.rect = pygame.Rect((self.left, self.y), (self.width, self.height))
        print(self.rect.y, self.y)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

    def update(self, dt):
        if self.move_multiplier:

            offset = self.move_multiplier * self.speed*dt*0.1
            if self.rect.bottom + offset < 400 and self.rect.top + offset >= 0:
                self.rect.move_ip(0, self.move_multiplier * self.speed*dt*0.1)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_multiplier = -1
            elif event.key == pygame.K_DOWN:
                self.move_multiplier = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.move_multiplier = None
            elif event.key == pygame.K_DOWN:
                self.move_multiplier = None
