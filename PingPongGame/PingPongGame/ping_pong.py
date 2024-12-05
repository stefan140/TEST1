from pygame import *
from time import sleep

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
score1 = 0
score2 = 0
racket1 = Player('C:/Users/user/Desktop/PingPongGame/PingPongGame/racket.png', 30, 200, 4, 50, 150)
racket2 = Player('C:/Users/user/Desktop/PingPongGame/PingPongGame/racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('C:/Users/user/Desktop/PingPongGame/PingPongGame/tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("Player 2 won!", True, (180, 0, 0))
lose2 = font1.render("Player 1 won!", True, (180, 0, 0))
font2 = font.Font(None, 24)
score = font2.render(f"{score1} - {score2}", True, (180, 0, 0))
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        score = font2.render(f"{score1} - {score2}", True, (180, 0, 0))

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0 :
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (230, 200))
            score2 += 1
            score = font2.render(f"{score1} - {score2}", True, (180, 0, 0))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (230, 200))
            score1 += 1
            score = font2.render(f"{score1} - {score2}", True, (180, 0, 0))
            game_over = True
        
        window.blit(score, (280, 100))
        racket1.reset()
        racket2.reset()
        ball.reset()
    else:
        score = font2.render(f"{score1} - {score2}", True, (180, 0, 0))
        window.blit(score, (280, 100))
        sleep(3)
        racket1.rect.x = 30
        racket1.rect.y = 200
        racket2.rect.x = 520
        racket2.rect.y = 200
        ball.rect.x = 280
        ball.rect.y = 240

        window.fill(back)
        racket1.reset()
        racket2.reset()
        ball.reset()

        finish = False

    display.update()
    clock.tick(FPS)