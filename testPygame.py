import pygame
from screeninfo import get_monitors

pygame.init()


def ddd(args):
    print(args)
    exit()


pygame.mixer.music.load("sounds/vista.mp3")
pygame.mixer.music.play()


first_monitor = get_monitors()[0]

# size = width, height = first_monitor.width - \
#     first_monitor.width_mm, first_monitor.height - first_monitor.height_mm
size = width, height = pygame.display.list_modes()[0]
print(first_monitor, size)

[print(method_name) for method_name in dir(pygame.display)
 if callable(getattr(pygame.display, method_name))]

screen = pygame.display.set_mode(
    size, flags=pygame.RESIZABLE)
back = pygame.image.load("pictures/dog1.png")
backRect = back.get_rect()

for y in range(0, height, backRect.height):
    for x in range(0, width, backRect.width):
        screen.blit(back, (x, y))
count = 0


while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYDOWN and event.mod & pygame.KMOD_CTRL > 0 \
                and event.key == pygame.K_q:
            break
        if event.type == pygame.MOUSEMOTION:
            print(event)
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, flags=pygame.RESIZABLE, Surface=screen)
            print("resize ! ", event)

    print(count, end=' ')
    print([method_name for method_name in dir(pygame.display.get_wm_info()['display'])
           if callable(getattr(pygame.display.get_wm_info()['display'], method_name))]
          )
    pygame.display.update()
    pygame.time.wait(500)
    count += 1

[print(method_name) for method_name in dir(pygame.display)
 if callable(getattr(pygame.display, method_name))]
