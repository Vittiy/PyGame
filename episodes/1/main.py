import pygame
pygame.init()

# Génerer la fenetre du jeux
pygame.display.set_caption("Commet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arrière plan de notre jeux

background = pygame.image.load('episodes/1/assets/bg.jpg')


running = True

# Boucle tant que cette condition est vrai

while running:

    # Appliquer l'arrière plan
    screen.blit(background, (0, 0))

    # metre a jour l'ecrean
    pygame.display.flip()

# si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de feneter
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux !")
