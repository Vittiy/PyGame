import pygame
import math
from game import Game
pygame.init()

# Génerer la fenetre du jeux
pygame.display.set_caption("Commet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arrière plan de notre jeux
background = pygame.image.load('assets/bg.jpg')
# Je re dimensionne l'image car mon ecran n'est pas assez grand mais vous pouvez le supprimer si ce n'est pas le cas pour vous !
background = pygame.transform.scale(background, (1080, 720))

# importer  charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeux
game = Game()

# Le jeux
running = True

# Boucle tant que cette condition est vrai
while running:

    # Appliquer la fenetre du jeux
    screen.blit(background, (0, 0))

    # Verifier si notre jeux a commencer ou non
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(screen)
    # Vérifier si notre jeux n'a pas commencer
    else:
        # Ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

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
            # detecter si la touche espace est enclanchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verification pour s'avoir si la souris est en collision avec le boutton jouer
            if play_button_rect.collidepoint(event.pos):
                # metre le mode de jeux en "lancé"
                game.start()