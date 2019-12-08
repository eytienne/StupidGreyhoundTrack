from tkinter import *

import pygame
from pygame.locals import *

from ImageEntity import ImageEntity
from BackgroundEntity import BackgroundEntity
from DogEntity import DogEntity

from threading import Timer
from threading import Thread
import random


class Game():

    WINDOW_TITLE = 'Stupid Greyhound Track'

    def __init__(self):
        self.entities = []
        self.launched = False
        self.finished = False
        self.clock = pygame.time.Clock()
        self.listeners = {}
        self.key_for_line = [K_SPACE, K_RETURN, K_m, K_u, K_z]
        pygame.base.init()
        pygame.display.set_caption(Game.WINDOW_TITLE)
        pygame.display.set_mode(flags=RESIZABLE)
        self.entities.append(BackgroundEntity("pictures/running_track.png"))
        DogEntity.init_runway(0.25, 0.09, 0.01, 0.70)
        for i in range(0, len(self.key_for_line)):
            self.entities.append(
                DogEntity("pictures/dog" + str(1 if i % 2 == 0 else 2) + ".png", i))

    def launch(self):
        self.launched = True
        self.remove_event_listener(KEYDOWN, self.get_dog_disqualified)
        self.add_event_listener(KEYDOWN, self.get_dog_forward)
        currentWindow = pygame.display.get_surface()
        pygame.mixer.Sound("audio/mp5.wav").play()
        pygame.time.wait(300)
        self.entities.append(ImageEntity(
            "pictures/submachine-gun.png", 10, 10, width=max(100, 0.1*currentWindow.get_width())))
        pygame.mixer_music.load("audio/off_limits.wav")
        pygame.mixer_music.play(-1)

    def finish(self, winner):
        self.finished = True
        self.remove_event_listener(KEYDOWN, self.get_dog_forward)
        text = pygame.font.Font("freesansbold.ttf", 115).render(
            "The winner is " + str(winner) + "!", True, (0, 255, 0), (0, 0, 128))
        text_rect = text.get_rect()
        text_rect.center = tuple(
            [dim/2 for dim in pygame.display.get_surface().get_size()])

        pygame.display.get_surface().blit(text, text_rect)
        pygame.display.update()

        pygame.mixer_music.fadeout(1)
        pygame.mixer_music.load("audio/ff7_victory.wav")
        pygame.mixer_music.play()
        while pygame.mixer_music.get_busy():
            pass
        self.end()

    def end(self):
        pygame.quit()
        exit()

    def get_dogs(self, key: callable = lambda e: e.run_line):
        return sorted([ent for ent in self.entities if type(ent) == DogEntity], key=key)

    def redraw(self):
        for entity in self.entities:
            entity.draw()
            pass
        pygame.display.update()

    def resize(self, event):
        pygame.display.set_mode(event.size, flags=RESIZABLE)
        self.redraw()

    def add_event_listener(self, event_type, listener: callable):
        if not event_type in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def remove_event_listener(self, event_type, listener: callable):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)

    def get_dog_forward(self, event):
        try:
            run_line = self.key_for_line.index(event.key)
            fellowDog = self.get_dogs()[run_line]
            if fellowDog.is_disqualified():
                return
            fellowDog.go_forward()
            if fellowDog.progress >= 1:
                self.redraw()
                self.finish(fellowDog)
        except ValueError:
            pass

    def get_dog_disqualified(self, event):
        try:
            run_line = self.key_for_line.index(event.key)
            fellowDog = self.get_dogs()[run_line]
            fellowDog.disqualify()
        except ValueError:
            pass

    def run(self):
        self.add_event_listener(QUIT, self.end)
        self.add_event_listener(VIDEORESIZE, self.resize)

        def user_quit_listener(event):
            if event.mod & KMOD_CTRL and event.key == K_q:
                self.end()
        self.add_event_listener(KEYDOWN, user_quit_listener)

        self.add_event_listener(KEYDOWN, self.get_dog_disqualified)

        Timer(random.random()*3, self.launch).start()
        while True:
            for event in pygame.event.get():
                if event.type in self.listeners:
                    for listener in self.listeners[event.type]:
                        if listener.__code__.co_argcount > (1 if hasattr(listener, '__self__') else 0):
                            listener(event)
                        else:
                            listener()

            if not self.finished:
                self.redraw()

            self.clock.tick(30)

    pass
