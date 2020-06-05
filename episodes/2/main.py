import pygame
from game import Game

pygame.init()

# Génerer la fenetre du jeux
pygame.display.set_caption("Commet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arrière plan de notre jeux
background = pygame.image.load('assets/bg.jpg')

# charger le jeux
game = Game()

# Le jeux
running = True

# Boucle tant que cette condition est vrai
while running:

    # Appliquer la fenetre du jeux
    screen.blit(background, (0, 0))

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # verifier si le joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_lef()


    # metre a jour l'ecrean
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de feneter
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux !")
            # detecter si un joueur lache une touche de clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False