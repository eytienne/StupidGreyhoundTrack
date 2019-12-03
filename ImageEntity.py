from Entity import Entity
import pygame

class ImageEntity(Entity):

    def __init__(self, url):
        super().__init__()
        self.image = pygame.image.load(url)

    def to_draw(self):
        return self.image

    pass
