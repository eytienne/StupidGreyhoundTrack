from ImageEntity import ImageEntity
import pygame


class DogEntity(ImageEntity):

    @staticmethod
    def init_runway(run_start_y, runway_height, run_start_x, run_length):
        DogEntity.run_start_y = run_start_y
        DogEntity.runway_height = runway_height
        DogEntity.run_start_x = run_start_x
        DogEntity.run_length = run_length

    def __init__(self, url, run_line):
        super().__init__(url)
        self.run_line = run_line
        self.progress = 0
        self.disqualified = False

    def get_run_line(self):
        return self.run_line

    def go_forward(self):
        self.progress += 0.1

    def disqualify(self):
        self.disqualified = True

    def is_disqualified(self):
        return self.disqualified

    def to_draw(self):
        return pygame.transform.rotate(super().to_draw(), 180) if self.disqualified else super().to_draw()

    def draw(self):
        width, height = pygame.display.get_surface().get_size()
        newX = width * self.run_start_x + width * self.progress * self.run_length
        newY = height * self.run_start_y + height * self.run_line * \
            self.runway_height+height*self.runway_height/2
        super().draw(newX, newY)

    def __str__(self):
        return "Dog n°"+str(self.run_line)

    pass
