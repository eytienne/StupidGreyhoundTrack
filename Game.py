import pygame
import time
from pygame.locals import *
from ImageEntity import ImageEntity
from BackgroundEntity import BackgroundEntity
from DogEntity import DogEntity
from threading import Timer
from threading import Thread
import threading
import random


class Game():

    entities = []
    launched = False
    finished = False
    clock = pygame.time.Clock()
    listeners = {}
    key_for_line = [K_SPACE, K_RETURN, K_a]

    @staticmethod
    def launch():
        Game.launched = True
        Game.remove_event_listener(KEYDOWN, Game.get_dog_disqualified)
        Game.add_event_listener(KEYDOWN, Game.get_dog_forward)
        currentWindow = pygame.display.get_surface()
        pygame.mixer.Sound("audio/mp5.wav").play()
        pygame.time.wait(300)
        Game.entities.append(ImageEntity(
            "pictures/submachine-gun.png", 10, 10, width=max(100, 0.1*currentWindow.get_width())))
        pygame.mixer_music.load("audio/off_limits.wav")
        pygame.mixer_music.play(-1)

    @staticmethod
    def finish(winner):
        Game.finished = True
        Game.remove_event_listener(KEYDOWN, Game.get_dog_forward)
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
        Game.end()

    @staticmethod
    def end():
        pygame.quit()
        exit()

    @staticmethod
    def get_dogs(key: callable = lambda e: e.run_line):
        return sorted([ent for ent in Game.entities if type(ent) == DogEntity], key=key)

    @staticmethod
    def redraw():
        for entity in Game.entities:
            entity.draw()
            pass
        pygame.display.update()

    @staticmethod
    def resize(event):
        pygame.display.set_mode(event.size, flags=RESIZABLE)
        Game.redraw()

    @staticmethod
    def add_event_listener(event_type, listener: callable):
        if not event_type in Game.listeners:
            Game.listeners[event_type] = []
        Game.listeners[event_type].append(listener)

    @staticmethod
    def remove_event_listener(event_type, listener: callable):
        if event_type in Game.listeners:
            Game.listeners[event_type].remove(listener)

    def get_dog_forward(event):
        run_line = Game.key_for_line.index(event.key)
        if run_line != ValueError:
            fellowDog = Game.get_dogs()[run_line]
            fellowDog.go_forward()
            if fellowDog.progress >= 1:
                Game.redraw()
                Game.finish(fellowDog)

    def get_dog_disqualified(event):
        run_line = Game.key_for_line.index(event.key)
        if run_line != ValueError:
            Game.get_dogs()[run_line].disqualify()

    @staticmethod
    def run():
        # init
        pygame.base.init()
        pygame.display.set_caption("Dog race")
        pygame.display.set_mode(flags=RESIZABLE)
        Game.entities.append(BackgroundEntity("pictures/running_track.png"))
        DogEntity.init_runway(0.33, 0.1, 0.01, 0.70)
        for i in range(0, len(Game.key_for_line)):
            Game.entities.append(
                DogEntity("pictures/dog" + str(1 if i % 2 == 0 else 2) + ".png", i))
        # end init

        Game.add_event_listener(QUIT, Game.end)
        Game.add_event_listener(VIDEORESIZE, Game.resize)

        def user_quit_listener(event):
            if event.mod & KMOD_CTRL and event.key == K_q:
                Game.end()
        Game.add_event_listener(KEYDOWN, user_quit_listener)

        Game.add_event_listener(KEYDOWN, Game.get_dog_disqualified)

        Timer(random.random()*3, Game.launch).start()
        while True:
            for event in pygame.event.get():
                if event.type in Game.listeners:
                    for listener in Game.listeners[event.type]:
                        listener(event)

            if not Game.finished:
                Game.redraw()

            Game.clock.tick(30)


Game.run()
