import math
import pygame
import random
white = (255, 255, 255)
black = (0, 0, 0)
block_w = 30
block_h = 15
class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([block_w, block_h])

        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class bouncing_ball(pygame.sprite.Sprite):
    x = random.randint(100.0,400.0)
    y = 250.0
    #start point of the bouncing block
    direction = random.randint(140.0,221.0)
    #random angle of the start direction

    
    speed = 15.0

    width = 9
    height = 9
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([self.width, self.height])
 
        self.image.fill(white)
 
        self.rect = self.image.get_rect()

        self.screen_w = pygame.display.get_surface().get_width()
        self.screen_h = pygame.display.get_surface().get_height()

    def bounce(self,difference):
        #define the herizontally bouncing property
        self.direction = 180 - self.direction
        #get the angle in
        self.direction = self.direction % 360
        self.direction = self.direction - difference

    def update(self):
        direction_radians = math.radians(self.direction)
 
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        self.rect.x = self.x
        self.rect.y = self.y
        #move the ball

        #detect the top screen
        if self.y <=0:
            self.bounce(0)
            self.y = 1
        #detect the left side of the screen
        if self.x<=0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
        #detect the right side of the screen
        if self.x > self.screen_w - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screen_w - self.width - 1

        #the bottom of the screen(lose)
        if self.y > 801:
            return True
        else:
            return False

#create the bottom bar to block the bouncing ball
class bottom_bar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.w = 80
        self.h = 8
        self.image = pygame.Surface([self.w, self.h])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.screen_w = pygame.display.get_surface().get_width()
        self.screen_h = pygame.display.get_surface().get_height()
        #genenation point of the bar
        self.rect.x = 0
        self.rect.y = self.screen_h-self.h - 5 

    def update(self):
        """
        #use the key press to control the bar
        events = pygame.event.get()
        for event in events:
           if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    self.rect.x-=1
                if event.key ==pygame.K_RIGHT:
                    self.rect.x+=1
        """
        position = pygame.mouse.get_pos()
        self.rect.x = position[0]
        #use the mouse to control the bar
        if self.rect.x > self.screen_w - self.w:
            self.rect.x = self.screen_w - self.w

pygame.init()
 
# Create an 1200x800 sized screen
screen = pygame.display.set_mode([1200, 800])
 
font = pygame.font.Font(None, 36)
 
background = pygame.Surface(screen.get_size())
 
# Create sprite lists
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
 

player = bottom_bar()
allsprites.add(player)
 

ball = bouncing_ball()
allsprites.add(ball)
balls.add(ball)
 

top = 50

blockcount = 34
 
for row in range(8):
    for column in range(0, blockcount):
        block = Block(white, column * (block_w + 5) + 5, top)
        blocks.add(block)
        allsprites.add(block)

    top += block_h + 10
 

clock = pygame.time.Clock()
 
#game over?
game_over = False
 

exit_program = False

while not exit_program:

    clock.tick(30)
    screen.fill(black)
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

    if not game_over:

        player.update()
        game_over = ball.update()
 

    if game_over:
        text = font.render("Game Over", True, white)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300
        screen.blit(text, textpos)
 
    if pygame.sprite.spritecollide(player, balls, False):

        difference = (player.rect.x + player.w/2) - (ball.rect.x+ball.width/2)
 
        ball.rect.y = screen.get_height() - player.rect.h - ball.rect.height - 1
        ball.bounce(difference)
 
    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
 
    if len(deadblocks) > 0:
        ball.bounce(0)
 
        if len(blocks) == 0:
            game_over = True
 
    allsprites.draw(screen)
 
    pygame.display.flip()
 
pygame.quit()
