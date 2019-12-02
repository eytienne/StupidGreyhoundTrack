import pygame
import time
from pygame.locals import *
from ImageEntity import ImageEntity
from DogEntity import DogEntity


class Game():

    def __init__(self):
        pygame.base.init()
        pygame.display.set_caption("Dog race")
        pygame.display.set_mode(flags=RESIZABLE)
        pygame.display.resize_event(VIDEORESIZE)
        print([e for e in pygame.event.get() if e.type == VIDEORESIZE])
        exit()
        self.entities = []
        self.entities.append(ImageEntity("pictures/running_track.png"))
        DogEntity.init_runway(0.5, 0.1, 0.01, 0.72)
        self.entities.append(DogEntity("pictures/dog1.png", 0))
        self.entities.append(DogEntity("pictures/dog2.png", 1))

    def get_dogs(self):
        return [ent for ent in self.entities if type(ent) == DogEntity]

    def finish(self, winner):
        text = pygame.font.Font("freesansbold.ttf", 115).render(
            "The winner is " + str(winner) + "!", True, (0, 255, 0), (0, 0, 128))
        text_rect = text.get_rect()
        text_rect.center = (0, 0)  # tuple(
        # [dim for dim in pygame.display.get_surface().get_size()])

        pygame.display.get_surface().blit(text, text_rect)
        pygame.display.update()

        time.sleep(1)
        self.end()

    def end(self):
        pygame.quit()
        exit()

    def redraw(self):
        for entity in self.entities:
            entity.draw()
            pass
        pygame.display.update()

    def run(self):
        while True:
            fellowDogs = self.get_dogs()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.end()
                if event.type == VIDEORESIZE:
                    self.redraw()
                if event.type == KEYDOWN and event.mod & KMOD_CTRL and event.key == K_q:
                    self.end()
                if event.type == KEYDOWN and event.key == K_SPACE:
                    fellowDogs[0].go_forward()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    fellowDogs[1].go_forward()

            self.redraw()
            for dog in fellowDogs:
                if dog.progress >= 1:
                    self.finish(dog)


Game().run()
