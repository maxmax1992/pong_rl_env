import pygame
from pygame.locals import *
from pong import Pong 
from pygame.time import Clock
import time
import numpy as np

HEADLESS = False
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.clock = Clock()
        self.clock.tick()
        self.headless = HEADLESS
        self.pong_logic = Pong()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        self.pong_logic.on_event(event)

    def on_loop(self):
        passed = self.clock.tick(60) 
        self.pong_logic.update(passed)

    def on_render(self):
        self.pong_logic.draw(self._display_surf)

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self._display_surf.fill((0, 0, 0))
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.update()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
