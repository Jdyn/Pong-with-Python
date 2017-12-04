import pygame as pg
from settings import *
from random import *

vec = pg.math.Vector2


class Paddle1(pg.sprite.Sprite):

    def __init__(self, game):
        self.groups = game.all_sprites, game.paddles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(0 + 5, HEIGHT / 2)
        self.speed = vec(0, 0)

    def movement(self):
        self.speed = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.speed.y = -PLAYER_SPEED
        if keys[pg.K_s]:
            self.speed.y = PLAYER_SPEED

    def update(self):
        self.movement()

        self.rect.x = self.pos.x
        self.pos.y += self.speed.y
        self.rect.y = self.pos.y

        if self.rect.top > HEIGHT:
            self.pos.y = 0
        if self.rect.bottom < 0:
            self.pos.y = HEIGHT


class Paddle2(pg.sprite.Sprite):

    def __init__(self, game):
        self.groups = game.all_sprites, game.paddles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH - PADDLE_WIDTH - 5, HEIGHT / 2)
        self.speed = vec(0, 0)

    def input(self):
        self.speed = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.speed.y = -PLAYER_SPEED
        if keys[pg.K_DOWN]:
            self.speed.y = PLAYER_SPEED

    def update(self):
        self.input()

        self.rect.x = self.pos.x
        self.pos.y += self.speed.y
        self.rect.y = self.pos.y

        if self.rect.top > HEIGHT:
            self.pos.y = 0
        if self.rect.bottom < 0:
            self.pos.y = HEIGHT


class Ball(pg.sprite.Sprite):

    def __init__(self, game):
        self.groups = game.all_sprites, game.balls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((BALL_WIDTH, BALL_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH / 2, 0)

        self.vel = vec(BALL_SPEED, BALL_SPEED)

    def update(self):
        self.pos += self.vel
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.vel.y = -self.vel.y

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.rand = randint(1, 2)
            self.pos = (WIDTH / 2, 0)

            if self.rand == 1:
                self.vel.x = -self.vel.x
            if self.rand == 2:
                self.vel.x = self.vel.x

        self.hits = pg.sprite.spritecollide(self, self.game.paddles, False)

        if self.hits:
                print("hit")
                self.vel.x = -self.vel.x

