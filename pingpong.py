from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 80)
win1 = font1.render('RAKET 1 WIN!', True, (255, 255, 255))
win2 = font1.render('RAKET 2 WIN!', True, (255, 255, 255))



# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

# класс спрайта-врага   
class Ball(GameSprite):
    pass
    # движение врага
    #def update(self):
   #     self.rect.y += self.speed
    #    if self.rect.x - raket_1 or raket_2 == 20:
   #         pass
#
 
# создаем спрайты
raket_1 = Player('table-tennis-racket-and-ball-clipart-design-illustration-free-png.png', 50, 250, 75, 75, 10)
raket_2 = Player('table-tennis-racket-and-ball-clipart-design-illustration-free-png.png', 450, 250, 75, 75, 10)
ball = Ball('1_1735.png', 250, 250, 40, 40, 7)

display.set_caption("Ping Pong")
window = display.set_mode((500, 500))
background = transform.scale((500, 500))
window.fill((0,0,0))
 
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        
 
  # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

        # производим движения спрайтов
        raket_1.update()
        raket_2.update()
        ball.update()

        # обновляем их в новом местоположении при каждой итерации цикла
        raket_1.reset()
        raket_2.reset()
        ball.reset()
 
        # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        if ball.rect.x == 20:
            window.blit(win2, (200, 200))
        if ball.rect.x == 480:
            window.blit(win1, (200, 200))

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(60)

    #1111111111
    
