import pygame
from utils.player.player import Player
from utils.monster.monster import Monster


# cree une secondes  classe qui va reperésenter notre jeux
class Game:
    def __init__(self):
        # Définir si notre jeux a commencer ou non
        self.is_playing = False
        # generer notre joueur quand la partie est crée
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # definir un group de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remetre le jeux a neuf, retirer les monstres, remettre le joueur a 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.healt = self.player.max_healt
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_healt_bar(screen)

        # récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # appliquer lensemble des images du groupe projectiles
        self.player.all_projectiles.draw(screen)

        # recuperer les montres du jeux
        for monster in self.all_monsters:
            monster.forward()
            monster.update_healt_bar(screen)

        # appliquer l'ensemble des images du groupe de montres
        self.all_monsters.draw(screen)

        # verifier si le joueur veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_lef()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))