import pygame
from projectile import Projectile

# cree une premiere class qui va représenter le joueur

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.healt = 100
        self.max_healt = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        # cree une nouvelle instance de la class projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en colision avec une entité monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_lef(self):
        self.rect.x -= self.velocity
