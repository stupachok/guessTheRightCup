import ______
import random

pygame.init()


BLACK = _______
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen_width = 800
screen_height = 600
screen = pygame.display.____((screen_width, screen_height))
pygame.display.set_caption("_____")

cup_img = pygame.image.load("___")
class Cup:
    def __________(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.has_ball = False

    def draw(self):
        screen._____(self.image, self.rect)

    def check_for_ball(self):
        return self.has_ball

cups = []
cup_width = 100
cup_height = 150
margin = 130
for i in range(3):
    x = margin + i * (cup_width + margin)
    y = screen_height - cup_height - margin
    cup = ____(x, y, cup_img.copy())
    cups.append(cup)

ball_cup_index = _____.randint(0, len(cups) - 1)
cups[________].has_ball = True

running = True

while _____:
    for e in pygame.event.get():
        if e.type == pygame._______:
            running = False

    screen._____(WHITE)

    for cup in ______:
        cup.draw()

    pygame._____.flip()

pygame.quit()
