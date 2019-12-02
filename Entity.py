import pygame

class Entity():

    def to_draw(self):
        raise NotImplementedError("to_draw method !")

    def draw(self, x=0, y=0):
        pygame.display.get_surface().blit(self.to_draw(), (x, y))

    pass
