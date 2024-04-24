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

def reset_game():
     global won, ball_cup_index
     for cup in cups:
         cup.has_ball = False
         cup.____ = cup_img.copy()
     ball_cup_index = random.____(0, len(cups) - 1)
     cups[_____].has_ball = True
     won = False

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

font = _____.font.Font(None, 36)
button_text = font.render('Start Over', True, BLACK)
button_rect = _______.get_rect(center=(screen_width // 2, 100))

running = True
won = ______

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:
             mouse_x, mouse_y = pygame.mouse.get_pos()
             for cup in cups:
                 if cup.rect.collidepoint(mouse_x, mouse_y):
                     if cup.check_for_ball():
                         cup.image = pygame.image.load("cup_and_ball.png")
                         won = _____
                     else:
                         cup.image = pygame.image.load("cup_and_nothing.png")
        
        if e.type == pygame.MOUSEBUTTONDOWN and won:
             if button_rect.collidepoint(pygame.mouse.get_pos()):
                 reset_game()


    screen.fill(WHITE)



    for cup in cups:
        cup.draw()

    
    
    if won:
         font = pygame.font.Font(None, 72)
         victory_text = font.render('You won!', True, ____)
         text_rect = victory_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
         screen.______(victory_text, text_rect)
         pygame.draw.rect(screen, WHITE, button_rect)
         ______.blit(button_text, button_rect.topleft)
    

    pygame.display.flip()

pygame.quit()
