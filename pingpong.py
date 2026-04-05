from pygame import *
'''Необходимые классы'''

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, pos_x, pos_y, speed, wight, hight):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (wight, hight))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed


#игровая сцена:
back = (200, 255, 255) #цвет фона (background)
win_width = 1000
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
#создания мяча и ракетки 
ball = GameSprite('1_1735.png', 400, 400, 4, 100, 100)
racket_l = Player('table-tennis-racket-and-ball-clipart-design-illustration-free-png.png', 10, 200, 4, 25, 150) # 130 - Ш 150 - В
racket_r = Player('table-tennis-racket-and-ball-clipart-design-illustration-free-png.png', 965, 200, 4, 25, 150)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
setting = font.render('press 1 to exit', True, (0, 0, 0))

speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket_l.update_l()
        racket_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 100 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
        
        if ball.rect.x < 0:
            window.blit(lose1, (win_width//2, win_height//2))
            finish = True
            
        if ball.rect.x > win_width:
            window.blit(lose2, (win_width//2, win_height//2))
            finish = True
            

    if finish:
        window.blit(setting, (win_width//2, win_height//2 + 50,))
        keys = key.get_pressed()
        if keys[K_1]:
            game = False


    ball.reset()
    racket_l.reset()
    racket_r.reset()

    display.update()
    clock.tick(FPS)
