from Entity import Entity
import pygame


class ImageEntity(Entity):

    def __init__(self, url, x=0, y=0, width=None, height=None):
        super().__init__()
        self.image = pygame.image.load(url)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def to_draw(self):
        ratio = self.image.get_width()/self.image.get_height()
        if self.width and self.height:
            scaledWidth = self.width
            scaledHeight = self.height
        elif self.width:
            scaledWidth = self.width
            scaledHeight = round(self.width/ratio)
        elif self.height:
            scaledWidth = round(self.height*ratio)
            scaledHeight = self.height
        else:
            scaledWidth = self.image.get_width()
            scaledHeight = self.image.get_height()
        return pygame.transform.scale(self.image, (int(scaledWidth), int(scaledHeight)))

    def draw(self, x=None, y=None):
        super().draw(x or self.x, y or self.y)

    pass
