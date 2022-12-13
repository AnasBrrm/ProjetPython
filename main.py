import random
def modeJeu(path):
    print("--------------------------Mode de Jeu ----------------------------------")
    print("choisissez un mode de jeu en entrant 1 ou 2 :")
    print("1 - Choix manuel des blocs ")
    print("2 - 3 blocs sélectionnés aléatoirement ")
    reponse3 = int(input())
    while reponse3 < 0 or reponse3 > 2:
        reponse3 = int(input(" Le chiffre n'est pas reconnu veuillez réessayer ") )
    if reponse3 == 1:
        print("Vous avez choisi le mode manuel")
        read_grid(path)
    if reponse3 == 2:
        print("Vous avez choisi le mode aléatoire")
        read_grid(path)
    # rediriger vers la fonction jeu


def read_grid(path, grid):

    if path == 1:
        with open(r"losange.txt", "r") as f1:
            contenus = f1.readlines()
        '''for ligne in contenus:
            grid.append(ligne)'''
    elif path == 2:
        with open(r"cercle.txt", "r") as f1:
            contenus = f1.readlines()
        '''for ligne in contenus :
            grid.append(ligne)'''
    elif path == 3 :
        with open(r"triangle.txt", "r") as f1:
            contenus = f1.readlines()
    for ligne in contenus:
        L = ligne.split(" ")
        L[-1] = L[-1][:-1] #supprimer l'anti slash n
        grid.append(L)
    for row in grid:
        print(row)
    print(grid[1][1])



def save_grid(path, grid):
    if path == 1:
        with open(r"losange.txt", "w") as f2:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    f2.write(grid[i][j])
    elif path == 2:
        with open(r"cercle.txt", "w") as f2:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    f2.write(grid[i][j])
    elif path == 3:
        with open(r"triangle.txt", "w") as f2:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    f2.write(grid[i][j])

def print_grid(grid):
    print("   a b c d e f g h i j k l m n o p q r s")
    print("  _____________________________________")
    c = 'a'
    for i in range(len(grid)):
        print(c,"|", end="")
        for j in range(len(grid[i])):
            if grid[i][j] == "0":
                print(" ", end=" ")
            elif grid[i][j] == "1":
                print(".", end=" ")
            elif grid[i][j] == "2":
                print("■", end=" ")
        print()
        c = chr(ord(c) + 1)

def select_bloc():
    print("--------------------------Mode de Jeu ----------------------------------")
    print("choisissez un mode de jeu en entrant 1 ou 2 :")
    print("1 - Choix manuel des blocs ")
    print("2 - 3 blocs sélectionnés aléatoirement ")
    reponse3=int(input())
    if reponse3 == 1:
        print("Veuillez selectionner un tetros parmis cela :")
        for h in range(len(block)):
            print(h + 1, ": \n", end="")
            for i in range(len(block[h])):
                for j in range(len(block[h][i])):
                    if block[h][i][j] == 1:
                        print("■", end=" ")
                    else:
                        print(". ", end="")
                print()
        n = int(input())
        bloc.append(block[n-1])
        print("Vous avez choisi :")
        for i in range(len(block[n - 1])):
            for j in range(len(block[n - 1][i])):
                if block[n - 1][i][j] == 1:
                    print("■", end=" ")
                else:
                    print(". ", end="")
            print()
    if reponse3 == 2:
        print("Veuillez selectionner un tetros parmis cela :")
        cpt = 0
        alea = []
        while cpt <3:
            alea1 = random.randint(0,6)
            alea.append(alea1)
            print(cpt+1, ": \n", end="")
            for i in range(len(block[alea1])):
                for j in range(len(block[alea1][i])):
                    if block[alea1][i][j] == 1:
                        print("■", end=" ")
                    else:
                        print(". ", end="")
                print()
            cpt +=1
        n = int(input())
        print("Vous avez choisi :" )
        alea1=alea[n-1]
        bloc.append(block[alea1])
        for i in range(len(block[alea1])):
            for j in range(len(block[alea1][i])):
                if block[alea1][i][j] == 1:
                    print("■", end=" ")
                else:
                    print(". ", end="")
            print()

def valide_position(grid, bloc, X, Y):
    i=1
    j=1
    for Y in range(grid[Y-3],grid[Y]):
        for X in range(grid[Y][X],grid[Y][X+3]):
            if grid[Y][X] + bloc[i][j] == 0:
                test +=1
            j+=1
        i+=1
        j=1
#--------------------------------------------------------------------------------------------------------------------
bloc= []
reponse = 3
grid = []
block = [[[1,0,0],[1,0,0],[1,1,1]],[[1, 0, 0], [1, 1, 0], [0, 0, 0]],[[1, 1, 1], [0, 1, 0], [0, 0, 0]],[[1, 1, 1], [0, 0, 0], [0, 0, 0]],
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]],[[1, 1, 0], [1, 1, 0], [0, 0, 0]],[[1, 1, 0], [0, 1, 1], [0, 0, 0]]]

while reponse != 2 :
    print("--------------------------Bienvenue sur le jeu TETRIS ----------------------------------")
    print("choisissez une action en entrant 1 ou 2 :")
    print("1 - Afficher les règles du jeu ")
    print("2 - Commencer à jouer ")
    reponse = int(input())
    while reponse < 0 or reponse > 2:
        reponse = int(input(" Le chiffre n'est pas reconnu veuillez réessayer ") )
    end = -1
    if reponse == 1 :
        while end == -1:
            print("-----------------------------Règles du jeu --------------------------------------")
            print("Le but du tétris est de placer des blocs sur un tableau de manière à la remplir entièrement")
            print("Vous devez remplir le tableau en un minimum de coups possibles")
            print("Vous ne pouvez pas placer un bloc sur une case déjà prise et il ne doit pas sortir du tableau")
            print("Appuyer 1 pour revenir au menu principal :")
            end = int(input())
    if reponse == 2 :
        print("Vous allez commencer à jouer :")
        print("Quelle forme voulez-vous choisir ? Choisissez en entrant le chiffre correspondant : ")
        print("1 - Losange")
        print("2 - Cercle")
        print("3 - Triangle ")
        path = int(input())
        while path < 1 or path > 3:
            path = int(input("Veuillez vérifier que votre chiffre est correct et réessayez "))
        if path == 1:
            print("Vous avez choisi le losange, Bonne chance !!")
        elif path == 2:
            print("Vous avez choisi le Cercle, Bonne chance !!")
        elif path == 3:
            print("Vous avez choisi le Triangle, Bonne chance !!")
read_grid(path, grid)

#save_grid(path, grid)
print_grid(grid)
select_bloc()


print("C4EST UN TEST : Donnez les coordonnés x,y sous forme de lettre :")
ci = input("x : ")
cj = input("y : ")
X = ord(ci)-97
Y=ord(cj)-97
print("Les cordonnées sont : ", str(X), " ", str(Y))
print(grid[X][Y])
i = 1
j = 1
tesst= 0
print(type(X))

for i in range(grid[Y-3],grid[X]):
    for j range
