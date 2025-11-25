from pygame import *

window = display.set_mode((900, 800))
display.set_caption('Ping-Pong')

game = True
timer = time.Clock()

class GameSprite(sprite.Sprite):
    def init(self, filename, x, y, width=30, height=200):
        super.__init__()
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
while game:
    window.fill((200, 130, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    timer.tick(80)