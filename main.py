import pygame
import random
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("guess the right cup")

cup_img = pygame.image.load("cup.png")
class Cup:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.has_ball = False

    def draw(self):
        screen.blit(self.image, self.rect)

    def check_for_ball(self):
        return self.has_ball

cups = []
cup_width = 100
cup_height = 150
margin = 130
amount_of_cups = 3

for i in range(amount_of_cups):
    x = margin + i * (cup_width + margin)
    y = screen_height - cup_height - margin
    cup = Cup(x, y, cup_img.copy())
    cups.append(cup)

ball_cup_index = random.randint(0, len(cups) - 1)
cups[ball_cup_index].has_ball = True


running = True



while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame._____:
             mouse_x, mouse_y = pygame.mouse.get_pos()
             for cup in ____:
                 if cup.rect.collidepoint(mouse_x, mouse_y):
                     if ____.check_for_ball():
                         cup.image = pygame.image._____("cup_and_ball.png")
                     else:
                         cup.image = pygame.____.load("cup_and_nothing.png")
   


    screen.fill(WHITE)



    for cup in cups:
        cup.draw()

    
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
