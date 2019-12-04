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

    @staticmethod
    def __init__():
        pygame.base.init()
        pygame.display.set_caption("Dog race")
        pygame.display.set_mode(flags=RESIZABLE)
        Game.entities = []
        Game.entities.append(BackgroundEntity("pictures/running_track.png"))
        DogEntity.init_runway(0.3, 0.1, 0.01, 0.70)
        Game.entities.append(DogEntity("pictures/dog1.png", 0))
        Game.entities.append(DogEntity("pictures/dog2.png", 1))
        Game.launched = False
        Game.finished = False

    @staticmethod
    def get_dogs():
        return [ent for ent in Game.entities if type(ent) == DogEntity]

    @staticmethod
    def launch():
        Game.launched = True
        Game.entities.append(ImageEntity("pictures/dog1.png"))

    @staticmethod
    def finish(winner):
        Game.finished = True

        pygame.mixer.music.stop()

        text = pygame.font.Font("freesansbold.ttf", 115).render(
            "The winner is " + str(winner) + "!", True, (0, 255, 0), (0, 0, 128))
        text_rect = text.get_rect()
        text_rect.center = tuple(
            [dim/2 for dim in pygame.display.get_surface().get_size()])

        pygame.display.get_surface().blit(text, text_rect)
        pygame.display.update()

        time.sleep(1)
        Game.end()

    @staticmethod
    def end():
        pygame.quit()
        exit()

    @staticmethod
    def redraw():
        for entity in Game.entities:
            entity.draw()
            pass
        pygame.display.update()
    
    @staticmethod
    def run():
        Timer(random.random()*3, Game.launch).start()
        Thread(None, Game.music).start()
        while True:
            fellowDogs = Game.get_dogs()
            for event in pygame.event.get():
                if event.type == QUIT:
                    Game.end()
                if event.type == VIDEORESIZE:
                    pygame.display.set_mode(event.size, flags=RESIZABLE)
                    Game.redraw()
                if event.type == KEYDOWN and event.mod & KMOD_CTRL and event.key == K_q:
                    Game.end()
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if Game.launched and not fellowDogs[0].is_disqualified():
                        fellowDogs[0].go_forward()
                    else:
                        fellowDogs[0].disqualify()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if Game.launched and not fellowDogs[1].is_disqualified():
                        fellowDogs[1].go_forward()
                    else:
                        fellowDogs[1].disqualify()

            Game.redraw()
            for dog in fellowDogs:
                if dog.progress >= 1:
                    Game.finish(dog)

    @staticmethod
    def music():
        pygame.mixer.music.load("music/ff7_victory.mp3")
        pygame.mixer.music.play(-1)

Game.__init__()
Thread(None, Game.run).start()