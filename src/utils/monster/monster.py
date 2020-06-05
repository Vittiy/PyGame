import pygame
import random


# Crée une classe qui va gérer la notion de monstre sur notren jeux
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.healt = 100
        self.max_healt = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # Infliger les degats
        self.healt -= amount

        # Verifier si sont nouveau nombre de point de vie est inferieur ou égale a 0
        if self.healt <= 0:
            # Réapparaitre comme un nouveau monstres
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.healt = self.max_healt

    def update_healt_bar(self, surface):
        # déssiner notre bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_healt, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.healt, 5])

    def forward(self):
        # le deplacement ne ce fait uniquement si il n'y a pas de collision avec un group de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des degats (au joueur)
            self.game.player.damage(self.attack)
