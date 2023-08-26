# Setup Python ----------------------------------------------- #
import pygame
import space
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('space invaders')

fond = pygame.image.load('space invaders.png')
j1 = pygame.image.load('1joueur.png')
j2 = pygame.image.load('2joueur.png')
screen = pygame.display.set_mode((800,600),0,32)
click = False
font = pygame.font.SysFont(None, 20)

def menu():
    click=False
    while True:
        screen.blit(fond,(0,0))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(270, 80, 260, 100)
        button_2 = pygame.Rect(270, 250, 260, 100)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (29,135,35), button_1)
        pygame.draw.rect(screen, (29,135,35), button_2)
        screen.blit(j1,(250, 60))
        screen.blit(j2,(250, 230))
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game():
    player=space.Joueur()
    player2=space.Joueur2()
    balle=space.Balle(player)
    balle2=space.Balle2(player2)
    ennemi=space.Ennemi(player)
    vie=space.Vie()
    vie2=space.Vie2()
    all_sprites = pygame.sprite.Group(player,player2,balle,balle2,ennemi,vie,vie2)
    yfond=0
    score=0
    score2=0
    service = 0
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Space Invaders")
    fond = pygame.image.load('background.png')

    while running :
        yfond+=1
        if yfond<619:
            screen.blit(fond,(-109,yfond))
            screen.blit(fond,(-109,yfond-619))
        else:
            yfond=0
            screen.blit(fond,(-109,yfond))
        screen.blit(player.image, player.rect)

        screen.blit(balle.image, balle.rect)

        screen.blit(ennemi.image, ennemi.rect)

        screen.blit(vie.image, vie.rect)
        clock.tick(200)


        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement

        # gestion du clavier
            if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                    player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                    player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_SPACE : # espace pour tirer
                    player.tirer(all_sprites)
                    #tir.etat = "tiree"

        ### Actualisation de la scene ###
        # Gestions des collisions
        """for ennemi in listeEnnemis:
            if tir.toucher(ennemi):
                ennemi.disparaitre()
                player.marquer()
        print(f"Score = {player.score} points")
        # placement des objets
        # le joueur
        #player.deplacer()
        #screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
        # la balle
        #tir.bouger()
        #screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
        # les ennemis
        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur])"""
        pygame.display.update()

        player.tirer(all_sprites)
        player.deplacer(all_sprites)
        balle.deplacer(all_sprites,player)
        balle.toucher(ennemi)
        ennemi.avancer()
        ennemi.disparaitre(player)
        vie.deplacementbarre(ennemi,player)

def options():
    player=space.Joueur()
    player2=space.Joueur2()
    balle=space.Balle(player)
    balle2=space.Balle2(player2)
    ennemi=space.Ennemi(player)
    vie=space.Vie()
    vie2=space.Vie2()
    all_sprites = pygame.sprite.Group(player,player2,balle,balle2,ennemi,vie,vie2)
    yfond=0
    score=0
    score2=0
    service = 0
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Space Invaders")
    fond = pygame.image.load('background.png')
    while running :
        yfond+=1
        if yfond<619:
            screen.blit(fond,(-109,yfond))
            screen.blit(fond,(-109,yfond-619))
        else:
            yfond=0
            screen.blit(fond,(-109,yfond))
        screen.blit(player.image, player.rect)
        screen.blit(player2.image, player2.rect)

        screen.blit(balle.image, balle.rect)
        screen.blit(balle2.image, balle2.rect)

        screen.blit(ennemi.image, ennemi.rect)

        screen.blit(vie.image, vie.rect)
        screen.blit(vie2.image, vie2.rect)
        clock.tick(200)


        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement

        # gestion du clavier
            if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
                if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                    player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                    player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
                if event.key == pygame.K_SPACE : # espace pour tirer
                    player.tirer(all_sprites)
                    #tir.etat = "tiree"

        ### Actualisation de la scene ###
        # Gestions des collisions
        """for ennemi in listeEnnemis:
            if tir.toucher(ennemi):
                ennemi.disparaitre()
                player.marquer()
        print(f"Score = {player.score} points")
        # placement des objets
        # le joueur
        #player.deplacer()
        #screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
        # la balle
        #tir.bouger()
        #screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
        # les ennemis
        for ennemi in listeEnnemis:
            ennemi.avancer()
            screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur])""" # appel de la fonction qui dessine le vaisseau du joueur
        pygame.display.update() # pour ajouter tout changement à l'écran



        player.tirer(all_sprites)
        player.deplacer(all_sprites)
        balle.deplacer(all_sprites,player)
        balle.toucher(ennemi)

        player2.tirer(all_sprites)
        player2.deplacer(all_sprites)
        balle2.deplacer(all_sprites,player2)
        balle2.toucher(ennemi)


        ennemi.avancer()
        ennemi.disparaitre(player)

        vie.deplacementbarre(ennemi,player)
        vie2.deplacementbarre(ennemi,player2)

menu()