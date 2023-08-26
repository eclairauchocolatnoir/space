import pygame  # necessaire pour charger les images et les sons
import time
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ====> CLASSE joueur1 + CLASSE BALLE1                                      """
""" ====> tue l'ennemi qui ne disparait pas                                   """
""" ====> Creation de vie à ajouter                                           """
""" ====> balle qui doit cesser de suivre le vaisseau                         """
""" ====> A les memes caracteristiques que joueur                             """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Joueur(pygame.sprite.Sprite) : # classe pour crÃ©er le vaisseau du joueur
    def __init__(self):
        super().__init__()
        ## Réglages = image + sons + position de depart (ne varie pas)
        self.image=pygame.image.load("vaisseau.png")
        self.rect=self.image.get_rect()
        self.rect.x=400
        self.rect.y=500
        self.position=300
        self.score=0
        self.taille=5

    def deplacer(self,all_sprites):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.rect.x -= 4
        if pressed[pygame.K_RIGHT]:
            self.rect.x += 4
        if pressed[pygame.K_LEFT] and self.rect.x<00  :
            self.rect.x = 0
        if pressed[pygame.K_RIGHT] and self.rect.x>750  :
            self.rect.x = 750

    def tirer(self, all_sprites):
        pressed = pygame.key.get_pressed()

    def marquer(self, all_sprites):
        pass

class Balle(pygame.sprite.Sprite) :
    def __init__(self, player):
        super().__init__()
        ## Réglages = vitesse + image + son (ne varie pas)
        self.image=pygame.image.load("balle.png")
        self.vitesse=5
        self.rect=self.image.get_rect()
        self.balleson = pygame.mixer.Sound('Laser.wav')
        self.ExplosionSon = pygame.mixer.Sound('Explosion.wav')
        ## Réglages = y + x (varie selon les positions du joueur)
        self.rect.y=400
        self.rect.x=500
        self.score=0
        self.etat="chargee"
        self.taille =10


    def deplacer(self,all_sprites,player):
        pressed = pygame.key.get_pressed()
        if self.etat=="chargee":
            if pressed[pygame.K_LEFT]:
                self.rect.x -= 4
            if pressed[pygame.K_RIGHT]:
                self.rect.x += 4
            if pressed[pygame.K_LEFT] and self.rect.x<0  :
                self.rect.x = 0
            if pressed[pygame.K_RIGHT] and self.rect.x>750  :
                self.rect.x = 750
            if pressed[pygame.K_DOWN]:
                self.etat="tiree"
        if self.etat=="tiree":
            self.rect.y-=self.vitesse
            if self.rect.y==0:
                self.rect.y=500
                self.rect.x=player.rect.x
                self.etat="chargee"

    def bouger(self,all_sprites):
        pass

    def toucher(self, ennemi):
        if (ennemi.rect.x < self.rect.x + self.taille and ennemi.rect.x >self.rect.x - self.taille and
                    ennemi.rect.y < self.rect.y + self.taille and ennemi.rect.y > self.rect.y - self.taille):
            self.score+=2
            print("Player 1 :" ,self.score)

        """
        if self.rect.y==ennemi.rect.y and self.rect.x==ennemi.rect.x:
            self.score+=2
            print("Player 1 :" ,self.score)"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ====> CLASSE joueur2 + CLASSE BALLE2                             """
""" ====> l'ennemi mais le tue pas                                   """
""" ====> Creation de vie à ajouter                                  """
""" ====> ballle qui doit cesser de suivre le vaisseau               """
""" ====> A les memes caracteristiques que joueur                    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Joueur2(pygame.sprite.Sprite) : # classe pour crÃ©er le vaisseau du joueur
    def __init__(self):
        super().__init__()
        ## Réglages = image + sons + position de depart (ne varie pas)
        self.image=pygame.image.load("vaisseau2.png")
        self.rect=self.image.get_rect()
        self.rect.x=450
        self.rect.y=500
        self.position=300
        self.score2=0
        self.vie2=5
        self.taille=10
        """self.health=50
        self.max_health=self.health
        self.attack=15"""

    def deplacer(self,all_sprites):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]:
            self.rect.x -= 4
        if pressed[pygame.K_d]:
            self.rect.x += 4
        if pressed[pygame.K_q] and self.rect.x<00  :
            self.rect.x = 0
        if pressed[pygame.K_d] and self.rect.x>750  :
            self.rect.x = 750

    def tirer(self, all_sprites):
        pressed = pygame.key.get_pressed()

    def marquer(self,amount):
        pass

class Balle2(pygame.sprite.Sprite) :
    def __init__(self, player2):
        super().__init__()
        ## Réglages = vitesse + image + son (ne varie pas)
        self.image=pygame.image.load("balle2.png")
        self.vitesse=5
        self.rect=self.image.get_rect()
        self.balleson = pygame.mixer.Sound('Laser.wav')
        self.ExplosionSon = pygame.mixer.Sound('Explosion.wav')
        ## Réglages = y + x (varie selon les positions du joueur)
        self.rect.x=450
        self.rect.y=500
        self.score2=0
        self.taille =5
        self.etat="chargee"


    def deplacer(self,all_sprites,player2):
        pressed = pygame.key.get_pressed()
        if self.etat=="chargee":
            if pressed[pygame.K_q]:
                self.rect.x -= 4
            if pressed[pygame.K_d]:
                self.rect.x += 4
            if pressed[pygame.K_q] and self.rect.x<0  :
                self.rect.x = 0
            if pressed[pygame.K_d] and self.rect.x>750  :
                self.rect.x = 750
            if pressed[pygame.K_s]:
                self.etat="tiree"
        if self.etat=="tiree":
            self.rect.y-=self.vitesse
            if self.rect.y==0:
                self.rect.y=500
                self.rect.x=player2.rect.x
                self.etat="chargee"

    def bouger(self,all_sprites):
        pass

    def toucher(self, ennemi):
        """if self.rect.y == ennemi.rect.y and self.rect.x == ennemi.rect.x:
            self.score2+=2
            print("Player 2 :" ,self.score2)"""
        if (ennemi.rect.x < self.rect.x + self.taille and ennemi.rect.x >self.rect.x - self.taille and
                    ennemi.rect.y < self.rect.y + self.taille and ennemi.rect.y > self.rect.y - self.taille):
            self.score2+=2
            print("Player 2 :" ,self.score2)








""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" ====> CLASSE ENNEMI                                              """
""" ====> Créé un second ennemi                                      """
""" ====> Créé disparaitre ennemi                                    """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Ennemi(pygame.sprite.Sprite) :
    def __init__(self, player):
        super().__init__()
        ## Réglages = vitesse + image + son (ne varie pas)
        self.image=pygame.image.load("invader2.png")
        self.image2=pygame.image.load("invader1.png")
        self.vitesse=2
        self.rect=self.image.get_rect()
        self.balleson = pygame.mixer.Sound('Laser.wav')
        self.ExplosionSon = pygame.mixer.Sound('Explosion.wav')
        self.score=0
        ## Réglages = y + x (varie selon les positions du joueur)
        self.rect.y=0
        self.rect.x=12
        ## BASES
        self.depart=0
        self.hauteur=0
        self.type=0

    def avancer(self):
        self.rect.y += self.vitesse
        if (self.rect.y > 700):
            #self.ExplosionSon.play()
            self.rect.y = -1 * self.rect.y
            self.rect.x = random.randint(0,600)
        if (self.rect.x > 800):
            self.rect.x = -1 * self.rect.x
        if (self.rect.y <= 0):
            self.rect.y = 0
        if (self.rect.x <=0):
            self.rect.x = 0

    def disparaitre(self,player):
        self.image=pygame.image.load("invader2.png")

#######################################################################################

class Vie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ## Réglages = image + sons + position de depart (ne varie pas)
        self.image=pygame.image.load("vie.png")
        self.rect=self.image.get_rect()
        self.mort = pygame.mixer.Sound('You are dead sound effect.wav')
        self.ExplosionSon = pygame.mixer.Sound('You are dead sound effect.wav')
        self.rect.x=0
        self.rect.y=0
        self.coup=25
        self.vie=3
        self.taille=10
        self.mort=0

    def deplacementbarre(self,ennemi,player):
        if (ennemi.rect.x < player.rect.x + self.taille and ennemi.rect.x >player.rect.x - player.taille
                and ennemi.rect.y < player.rect.y + player.taille and ennemi.rect.y > player.rect.y - player.taille):
            self.rect.x-=60
            self.vie-=1
            print("1 : nbr de vie restante :",self.vie)
        if self.vie==1:
            self.ExplosionSon.play()
            player.image=pygame.image.load("fantome.png")

class Vie2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ## Réglages = image + sons + position de depart (ne varie pas)
        self.image=pygame.image.load("vie.png")
        self.rect=self.image.get_rect()
        self.mort = pygame.mixer.Sound('You are dead sound effect.wav')
        self.ExplosionSon = pygame.mixer.Sound('You are dead sound effect.wav')
        self.rect.x=700
        self.rect.y=0
        self.vie=3
        self.taille=10
        self.mort=0

    def deplacementbarre(self,ennemi,player2):
        if (ennemi.rect.x < player2.rect.x + self.taille and ennemi.rect.x >player2.rect.x - player2.taille
                and ennemi.rect.y < player2.rect.y + player2.taille and ennemi.rect.y > player2.rect.y - player2.taille):
            self.rect.x+=6
        if self.rect.x>=800:
            self.ExplosionSon.play()
            player2.image=pygame.image.load("fantome.png")

################################################################################





