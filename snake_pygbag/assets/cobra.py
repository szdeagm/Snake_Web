from pygame import *
from pygame.locals import *
from pygame import font, image
import random 

class Cobra():
    def __init__(self):
        self.rayquaza = image.load("rayquaza.png")
        self.rayquaza = transform.scale(self.rayquaza, (100, 100))
        self.rayquaza_direita = image.load("rayquaza_direita.png")
        self.rayquaza_direita = transform.scale(self.rayquaza_direita, (150, 130))
        self.rayquaza_cima = image.load("rayquaza_cima.png")
        self.rayquaza_cima = transform.scale(self.rayquaza_cima, (125, 125))
        self.rayquaza_esquerda = image.load("rayquaza_esquerda.png")
        self.rayquaza_esquerda = transform.scale(self.rayquaza_esquerda, (150, 130))
        self.rayquaza_parado = image.load("rayquaza_parado.png")
        self.rayquaza_parado = transform.scale(self.rayquaza_parado, (125, 125))
        self.cobra = [[200, 200], [240, 200]]
        self.skin = Surface((25,25))
        self.skin.fill((0, 0, 0))
        self.direction = "Right"
        self.change_to = self.direction
        self.cobra_direction = [240, 200]

class Fruta():
    def __init__(self):
        self.frutafoto = image.load("fruta.png")
        self.frutafoto = transform.scale(self.frutafoto, (40,40))
        x = random.randint(4,54)*10
        y = random.randint(4,54)*10
        self.fruta = [x, y] 
        self.fskin = Surface((25,25))
        self.fskin.fill((0,0,0))
        self.fruta_spaw = True

    def reposicionar(self):
        x = random.randint(4,54)*10
        y = random.randint(4,54)*10
        self.fruta = [x, y] 