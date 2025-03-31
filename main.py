from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def resert(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_height = 500
win_width = 700

player = GameSprite('hero.png', 5, win_height - 80, 4)
monster = GameSprite('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)



window = display.set_mode((win_width, win_height))
display.set_caption('лабіринт')
backround = transform.scale(
    image.load('background.jpg'),
    (win_width, win_height)
)

clock = time.Clock()
FPS = 90



game = True
while game:
    window.blit(backround, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False







    clock.tick(FPS)

    display.update()