
import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Jeu du Pendu')

# Chargement des images du pendu


# Liste de mots pour le jeu
liste_mots = ['rooney', 'zidane', 'ronaldo', 'neymar', 'messi', 'hazard','kimmich', 'benzema', 'maradona', 'xavi', 'mbappe', 'pogba', 'kante', 'drogba', 'nasri']
mot_a_deviner = random.choice(liste_mots)

# Polices de texte
police = pygame.font.SysFont('Arial', 40)
police_petite = pygame.font.SysFont('Arial', 20)

# Variables du jeu
lettres_trouvees = []
lettres_proposees = []
nb_essais = 0


def les_erreurs(i):
    # [Le code de dessin du pendu]
    # Base
    for i in range(10): 
        if i == 1:
            pygame.draw.line(ecran, BLANC, (50, 500), (150, 500), 5)
    # Poteau
        if i ==2:
            pygame.draw.line(ecran, BLANC, (100, 500), (100, 100), 5)
    # Traverse
        if i ==3:
            pygame.draw.line(ecran, BLANC, (100, 100), (300, 100), 5)
    # Corde
        if i ==4:
            pygame.draw.line(ecran, BLANC, (300, 100), (300, 150), 5)
    # Tête
        if i==5:
            pygame.draw.circle(ecran, BLANC, (300, 180), 30, 5)
    # Corps
        if i ==6:
            pygame.draw.line(ecran, BLANC, (300, 210), (300, 350), 5)
    # Bras gauche
        if i==7:
            pygame.draw.line(ecran, BLANC, (300, 250), (250, 300), 5)
    # Bras droit
        if i==8:
            pygame.draw.line(ecran, BLANC, (300, 250), (350, 300), 5)
    # Jambe gauche
        if i==9:
            pygame.draw.line(ecran, BLANC, (300, 350), (250, 400), 5)
    # Jambe droite
        if i==10:
            pygame.draw.line(ecran, BLANC, (300, 350), (350, 400), 5)
    print(i)
    
# Fonction pour dessiner le texte
def dessiner_texte(texte, x, y, taille, couleur):
    font = pygame.font.Font(None, taille)
    surface_texte = font.render(texte, True, couleur)
    ecran.blit(surface_texte, (x, y))

# Fonction pour dessiner le pendu

    

# Fonction pour afficher les lettres
def afficher_lettres():
    texte = ''
    for lettre in mot_a_deviner:
        if lettre in lettres_trouvees:
            texte += lettre + ' '
        else:
            texte += '_ '
    dessiner_texte(texte, 300, 400, 40, BLANC)

# Boucle principale du jeu
def jouer():
    global nb_essais

    while True:
        ecran.fill(NOIR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key >= 97 and event.key <= 122:  # Vérifier si une lettre a été pressée
                    lettre = chr(event.key)
                    if lettre not in lettres_proposees:
                        lettres_proposees.append(lettre)
                        if lettre in mot_a_deviner:
                            lettres_trouvees.append(lettre)
                        else:
                            nb_essais += 1

        
        afficher_lettres()
        


        # Vérifier si le joueur a gagné ou perdu
        if all(lettre in lettres_trouvees for lettre in mot_a_deviner):
            dessiner_texte("Vous avez gagné ! Le mot était :", 150, 300, 40, BLANC)
            dessiner_texte(mot_a_deviner.upper(), 380, 350, 40, BLANC)
        elif nb_essais == 6:
            dessiner_texte("Vous avez perdu ! Le mot était :", 150, 300, 40, BLANC)
            dessiner_texte(mot_a_deviner.upper(), 380, 350, 40, BLANC)

        pygame.display.update()

# Lancement du jeu
jouer()

