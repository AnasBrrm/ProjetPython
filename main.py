import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre et création de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))

# Titre de la fenêtre
pygame.display.set_caption("Jeu avec personnage carré et plateformes")

# Classe Personnage
class Personnage:
    def __init__(self, x, y, taille):
        self.x = x
        self.y = y
        self.taille = taille
        self.vx = 0
        self.vy = 0
    
    def appliquer_force(self, fx, fy):
        self.vx += fx
        self.vy += fy
    
    def maj_vitesse(self, gravite):
        self.vy += gravite

    
    def deplacer(self, dx, dy):
        self.x += dx
        self.y += dy

    def dessiner(self, fenetre):
        pygame.draw.rect(fenetre, (255, 255, 255), (self.x, self.y, self.taille, self.taille))
        
    def collision(self, niveau, taille_bloc, largeur, hauteur):
        x_min = self.x
        y_min = self.y
        x_max = self.x + self.taille
        y_max = self.y + self.taille

        # Collision avec les bords de la fenêtre
        if x_min < 0:
            self.x = 0
            self.vx = 0
        if y_min < 0:
            self.y = 0
            self.vy = 0
        if x_max > largeur:
            self.x = largeur - self.taille
            self.vx = 0
        if y_max > hauteur:
            self.y = hauteur - self.taille
            self.vy = 0

        # Collision horizontale
        i_min, j_min = int(y_min // taille_bloc), int(x_min // taille_bloc)
        i_max, j_max = int(y_max // taille_bloc), int(x_max // taille_bloc)

        for i in range(i_min, i_max + 1):
            if i < 0 or i >= len(niveau):  # Vérification des limites pour i
                continue
            for j in range(j_min, j_max + 1):
                if j < 0 or j >= len(niveau[0]):  # Vérification des limites pour j
                    continue
                if niveau[i][j] == 1:
                    if self.vx > 0:
                        self.x = j * taille_bloc - self.taille
                        self.vx = 0
                    elif self.vx < 0:
                        self.x = (j + 1) * taille_bloc
                        self.vx = 0
                    break
            else:
                continue
            break

        # Collision verticale
        x_min = self.x
        y_min = self.y
        x_max = self.x + self.taille
        y_max = self.y + self.taille

        i_min, j_min = int(y_min // taille_bloc), int(x_min // taille_bloc)
        i_max, j_max = int(y_max // taille_bloc), int(x_max // taille_bloc)

        for i in range(i_min, i_max + 1):
            if i < 0 or i >= len(niveau):  # Vérification des limites pour i
                continue
            for j in range(j_min, j_max + 1):
                if j < 0 or j >= len(niveau[0]):  # Vérification des limites pour j
                    continue
                if niveau[i][j] == 1:
                    if self.vy > 0:
                        self.y = i * taille_bloc - self.taille
                        self.vy = 0
                    elif self.vy < 0:
                        self.y = (i + 1) * taille_bloc
                        self.vy = 0
                    break
            else:
                continue
            break


    def sur_une_plateforme(self, niveau, taille_bloc, tol=2):
        x_min = self.x
        y_min = self.y
        x_max = self.x + self.taille
        y_max = self.y + self.taille

        i_min, j_min = int((y_min + tol) // taille_bloc), int((x_min + tol) // taille_bloc)
        i_max, j_max = int((y_max - tol) // taille_bloc), int((x_max - tol) // taille_bloc)

        for i in range(i_min, i_max + 1):
            for j in range(j_min, j_max + 1):
                if niveau[i][j] == 1:
                    if self.vy >= 0 and y_max <= (i * taille_bloc) + tol:
                        return True
        return False

# Création d'un personnage
personnage = Personnage(largeur//2, hauteur//2, 40)

# Vitesse du personnage
vitesse = 1

# Matrice représentant le niveau
niveau = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Taille des blocs
taille_bloc = 40

def generer_points_parabole(x0, y0, vx, vy, gravite, nb_points):
    points = []
    for t in range(nb_points):
        x = x0 + vx * t
        y = y0 - (vy * t - 0.5 * gravite * t**2)
        points.append((x, y))
    return points

def dessiner_parabole(fenetre, x0, y0, vx, vy, gravite, nb_points, couleur):
    x, y = x0, y0
    for t in range(1, nb_points):
        x_prec, y_prec = x, y
        x += vx
        y += vy
        vy += gravite
        pygame.draw.line(fenetre, couleur, (x_prec, y_prec), (x, y), 2)




# Fonction pour dessiner les plateformes
def dessiner_plateformes(fenetre, niveau, taille_bloc):
    for i, ligne in enumerate(niveau):
        for j, bloc in enumerate(ligne):
            if bloc:
                pygame.draw.rect(fenetre, (0, 255, 0), (j * taille_bloc, i * taille_bloc, taille_bloc, taille_bloc))

force_max = 200
gravite = 1
vitesse_lancer = 10
deplacement_actif = False

clic_initial = None


while True:
    gravite = 0.2
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion des clics de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                clic_initial = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and clic_initial:  # Bouton gauche de la souris relâché
                cible_x, cible_y = pygame.mouse.get_pos()
                dx = clic_initial[0] - cible_x
                dy = clic_initial[1] - cible_y
                distance = (dx ** 2 + dy ** 2) ** 0.5
                rapport_force = min(1, distance / force_max)
                if distance != 0:
                    personnage.vx = dx * vitesse_lancer * rapport_force / distance
                    personnage.vy = dy * vitesse_lancer * rapport_force / distance
                else:
                    personnage.vx = 0
                    personnage.vy = 0

                deplacement_actif = True
                clic_initial = None

    if not personnage.sur_une_plateforme(niveau, taille_bloc):
        personnage.maj_vitesse(gravite)
    else:
        personnage.vy = 0


    # Appliquer la gravité au personnage si le déplacement est actif
    if deplacement_actif:
        personnage.x += personnage.vx
        personnage.y += personnage.vy
        personnage.collision(niveau, taille_bloc, largeur, hauteur)



    # Effacement de l'écran
    fenetre.fill((0, 0, 0))

    # Dessin des plateformes
    dessiner_plateformes(fenetre, niveau, taille_bloc)

    # Dessin du personnage
    personnage.dessiner(fenetre)

    # Dessin de la ligne de lancement si un clic initial est enregistré
    if clic_initial:
        cible_x, cible_y = pygame.mouse.get_pos()
        dx = clic_initial[0] - cible_x
        dy = clic_initial[1] - cible_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        rapport_force = min(1, distance / force_max)
        if distance != 0:
            vx = dx * vitesse_lancer * rapport_force / distance
            vy = dy * vitesse_lancer * rapport_force / distance
        else:
            vx = 0
            vy = 0
        
        nb_points_min = 10
        nb_points_max = 100
        nb_points = int(nb_points_min + rapport_force * (nb_points_max - nb_points_min))
        
        dessiner_parabole(fenetre, personnage.x + personnage.taille // 2, personnage.y + personnage.taille // 2, vx, vy, gravite, nb_points, (255, 0, 0))

    # Actualisation de l'écran
    pygame.display.flip()

    # Limiter les images par seconde
    pygame.time.Clock().tick(60)
