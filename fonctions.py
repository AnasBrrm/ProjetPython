import random
import matplotlib as plt

list_bloc = [[[1,0,0],[1,0,0],[1,1,1]], #L
            [[1,0,0],[1,1,0],[0,0,0]],  #Petit L
            [[1,1,1],[0,1,0],[0,0,0]],  #T
            [[1,1,1],[0,0,0],[0,0,0]],  #_
            [[1,1,1],[1,1,1],[1,1,1]],  #Carré
            [[1,1,0],[1,1,0],[0,0,0]],  #Petit carré
            [[1,1,0],[0,1,1],[0,0,0]]]  #Z

grid = []

def read_grid(path, grid):

    if path == 1:
        with open(r"losange.txt", "r") as f1:
            contenus = f1.readlines()
    elif path == 2:
        with open(r"cercle.txt", "r") as f1:
            contenus = f1.readlines()
    elif path == 3 :
        with open(r"triangle.txt", "r") as f1:
            contenus = f1.readlines()
    for ligne in contenus:
        L = ligne.split(" ")
        L[-1] = L[-1][:-1] #supprimer l'anti slash n
        grid.append(L)

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
    print("   A B C D E F G H I J K L M N O P Q R S")
    print("  _____________________________________")
    c = 'A'
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
    print("Choisissez un mode de jeu en entrant 1 ou 2 :")
    print("1 - Choix manuel des blocs ")
    print("2 - 3 blocs sélectionnés aléatoirement ")
    reponse3 = int(input())
    while reponse3 < 0 or reponse3 > 2:
        reponse3 = int(input(" Le chiffre n'est pas reconnu veuillez réessayer ") )

    if reponse3 == 1:
        print("Veuillez selectionner un bloc :")
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