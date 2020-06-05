from player import Player


# cree une secondes  classe qui va reperésenter notre jeux
class Game:
    def __init__(self):
        # generer notre joueur quand la partie est crée
        self.player = Player()
        self.pressed = {}
