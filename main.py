from sprites import *



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pong")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        self.paddles = pg.sprite.Group()

        self.paddle1 = Paddle1(self)
        self.paddle2 = Paddle2(self)
        self.ball  = Ball(self)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.clock.tick(FPS)
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(DARK_GREY)
        pg.draw.line(self.screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 3)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


g = Game()

while g.running:
    g.new()

pg.quit()
