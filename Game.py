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
    def get_dogs():
        return sorted([ent for ent in Game.entities if type(ent) == DogEntity], key=lambda e: e.run_line)

    @staticmethod
    def launch():
        Game.launched = True
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
    def redraw():
        for entity in Game.entities:
            entity.draw()
            pass
        pygame.display.update()

    @staticmethod
    def run():
        # init
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
        Game.clock = pygame.time.Clock()
        # end init

        Timer(random.random()*3, Game.launch).start()
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
                    if Game.launched and not Game.finished and not fellowDogs[0].is_disqualified():
                        fellowDogs[0].go_forward()
                    else:
                        fellowDogs[0].disqualify()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if Game.launched and not Game.finished and not fellowDogs[1].is_disqualified():
                        fellowDogs[1].go_forward()
                    else:
                        fellowDogs[1].disqualify()
                        
            if not Game.finished:
                Game.redraw()

            for dog in fellowDogs:
                if dog.progress >= 1 and not Game.finished:
                    Game.finish(dog)

            Game.clock.tick(30)


Game.run()
