from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def resert(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
win_height = 500
win_width = 700
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
#підключання клавіш з перевіркою чи невиходить за межі екрану
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width-self.rect.width:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height-self.rect.height:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
#
    def update(self):
        #ліва межа
        if self.rect.x <= 270:
            self.direction = 'right'   
        #права межа        
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, wall_collor, x, y, w, h):
        super().__init__()
        self.color = wall_collor
        self.width = w
        self.height = h
        self.image = Surface((self.width, self.height))
        self.image.fill(wall_collor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall_Image(sprite.Sprite):
    def __init__(self, filename, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

walls = []
walls.append(Wall((2, 247, 121), 220, 160, 10, 460 - 160))
walls.append(Wall((2, 247, 121), 140, 300, 10, 370 - 300))
walls.append(Wall((2, 247, 121), 80, 370, 70, 10))
walls.append(Wall((2, 247, 121), 30, 370, 60, 10))
walls.append(Wall((2, 247, 121), 30, 210, 110, 10))
walls.append(Wall((2, 247, 121), 230, 160, 150, 10))
walls.append(Wall((2, 247, 121), 380, 170, 10, 200))
walls.append(Wall((2, 247, 121), 520, 130, 10, 520))
walls.append(Wall((2, 247, 121), 600, 130, 10, 220))
walls.append(Wall((2, 247, 121), 610, 230, 500, 10))
walls.append(Wall((2, 247, 121), 330, 250, 10, 120))
walls.append(Wall((2, 247, 121), 340, 370, 40, 10))
walls.append(Wall((2, 247, 121), 100, 30, 330, 40))
walls.append(Wall_Image('shupdown.png', 270, 70, 20, 20))

x = 340
while x < 3600:
    walls.append(Wall_Image('shupup.png', x, 480, 20, 20))
    x += 10

player = Player('hero.png', 5, win_height - 80, 2)
monster = Enemy('cyborg.png', win_width - 80, 280, 1)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)



window = display.set_mode((win_width, win_height))
display.set_caption('лабіринт')
backround = transform.scale(
    image.load('background.jpg'),
    (win_width, win_height)
)

clock = time.Clock()
FPS = 90
finish = False

mixer.init()
mixer.music.load('jungles.ogg')
#mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

game = True
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(backround, (0, 0))
        player.resert()
        player.update()
        monster.resert()
        monster.update()
        final.resert()
        for wall in walls:
            wall.draw()
        for wall in walls:
            if sprite.collide_rect(player, wall):
                kick.play()
                player.rect.x = 5
                player.rect.y = win_height - 80

        if sprite.collide_rect(player, monster):
            kick.play()
            player.rect.x = 5
            player.rect.y = win_height - 80
        if sprite.collide_rect(player, final):
            money.play()
            finish = True


    clock.tick(FPS)

    display.update()