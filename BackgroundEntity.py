from ImageEntity import ImageEntity
import pygame

class BackgroundEntity(ImageEntity):

    def to_draw(self):
        return pygame.transform.scale(super().to_draw(), pygame.display.get_surface().get_size())

    pass
