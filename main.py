import random
def valeur():
    global list_bloc, grid, bloc, Testjeu, score, reponse 
    list_bloc = [[[[1,4,4],[1,4,4],[1,1,1],]],#
                [[1,4,4],[1,1,4]],  #Petit L
                [[1,1,1],[4,1,4]],  #T
                [[1,1,1]],  #_
                [[1,1,1],[1,1,1],[1,1,1]],  #Carré
                [[1,1,4],[1,1,4]],  #Petit carré
                [[1,1,4],[4,1,1]]] #Z
    grid = []
    bloc = []
    Testjeu = False
    reponse = 0
    score = 0
#Fonctions#aa
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
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                grid[i][j]=int(grid[i][j])
            except :
                pass
        
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
    #Affiche le plateau de jeu    
    print("  _________________", str(score),"________________")
    print("   A B C D E F G H I J K L M N O P Q R S")
    print("  _____________________________________")
    c = 'A'
    for i in range(len(grid)):
        print(c,"|", end="")
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                print(" ", end=" ")
            elif grid[i][j] == 1:
                print(".", end=" ")
            elif grid[i][j] == 2:
                print("■", end=" ")
        print()
        c = chr(ord(c) + 1)

def select_bloc(reponse3):
    #Affiche les blocs possibles
    if reponse3 == 1:
        print("Veuillez selectionner un bloc :")
        for h in range(len(list_bloc)):
            print("\n", h + 1, ": \n", end="")
            for i in range(len(list_bloc[h])):
                for j in range(len(list_bloc[h][i])):
                    if list_bloc[h][i][j] == 1:
                        print("■", end=" ")
                    else:
                        print(". ", end="")
                print()
    #Ajouter dans la liste bloc le bloc choisi par l'utilisateur 
        n = int(input())
        for i in range(len(list_bloc[n-1])):
                bloc.append(list_bloc[n-1][i])
    #Afficher le bloc choisi par l'utilisateur
        print("Vous avez choisi :")
        for i in range(len(list_bloc[n - 1])):
            for j in range(len(list_bloc[n - 1][i])):
                if list_bloc[n - 1][i][j] == 1:
                    print("■", end=" ")
                else:
                    print(". ", end="")
            print()

    if reponse3 == 2:
        print("Veuillez selectionner un bloc :")
        cpt = 0
        alea = []
        while cpt <3:
            alea1 = random.randint(0,6)
            alea.append(alea1)
            print("\n", cpt+1, ": \n", end="")
            for i in range(len(list_bloc[alea1])):
                for j in range(len(list_bloc[alea1][i])):
                    if list_bloc[alea1][i][j] == 1:
                        print("■", end=" ")
                    else:
                        print(". ", end="")
                print()
            cpt +=1
        n = int(input())
        print("Vous avez choisi :" )
        alea1=alea[n-1]
        for i in range(len(list_bloc[alea1])):
            bloc.append(list_bloc[alea1][i])
    #Afficher le bloc
        for i in range(len(list_bloc[alea1])):
            for j in range(len(list_bloc[alea1][i])):
                if list_bloc[alea1][i][j] == 1:
                    print("■", end=" ")
                else:
                    print(". ", end="")
            print()

def valid_position(grid, bloc):
    global Valid_pos, Xi, Yi
    Valid_pos = True
    x = input("Veuillez saisir la ligne souhaitée : ")
    y = input("Veuillez saisir la colonne souhaitée : ")
    X = Xi= ord(x)-97
    Y= Yi =ord(y)-97
    
    X = X - len(bloc)+ 1
    for i in range(len(bloc)):
        if Valid_pos == False:
            break
        for j in range(len(bloc[i])):
            if (bloc[i][j] + grid[X][Y] == 3) or (bloc[i][j] + grid[X][Y] == 0) or (bloc[i][j] + grid[X][Y] == 1):
                Valid_pos = False
                break
            if bloc[i][j] + grid[X][Y] == 2:
                Valid_pos = True
            Y += 1  
        X += 1
        Y -= 3

def emplace_bloc(grid, bloc, Xi, Yi, Valid_pos):
    Xi = Xi - len(bloc)+ 1 
    if Valid_pos == True:
        for i in range(len(bloc)):
            for j in range(len(bloc[i])):
                if bloc[i][j] + grid[Xi][Yi] == 2:
                   grid[Xi][Yi] = grid[Xi][Yi]+1
                Yi += 1  
            Xi += 1
            Yi -= 3
    else : 
        print("VOUS NE POUVEZ PAS POSER LE BLOC ICI ! \n" )

def row_state(grid):
        global row_test, row_len
        row_len = 0
        for i in range(len(grid)):
            if 1 in grid[i]:
                row_test = False
            else :
                row_test = True
                row_len = i
                break

def row_clear(grid, row_test, row_len, score):
    if row_test == True:
        for j in range(len(grid[row_len])):
            if grid[row_len][j] == 2:
                score = score + 1
        
        for j in range(len(grid[row_len])):
                if grid[row_len][j] == 2 :
                    grid[row_len][j] = 1          
            
        for k in range(row_len, 0, -1):
            for j in range(len(grid[k])):
                if grid[k-1][j] == 2:
                    grid[k][j] = 2
                    grid[k-1][j] = 1

def update_score(row_test, score):
    if row_test == True:
        for j in range(len(grid[row_len])):
            if grid[row_len][j] == 2:
                score += 1

    

#------------------------------------#
valeur()
while reponse != 2 :
    print("----------------------------------------------------------------------------------------\n")
    print("--------------------------Bienvenue sur le jeu TETRIS ----------------------------------\n")
    print("----------------------------------------------------------------------------------------\n")
    print("Choisissez une action en entrant 1 ou 2 :\n")
    print("1 - Afficher les règles du jeu \n")
    print("2 - Commencer à jouer \n")
    reponse = int(input())
    while reponse < 0 or reponse > 2:
        reponse = int(input(" Le chiffre n'est pas reconnu veuillez réessayer ") )
    end = -1
    if reponse == 1 :
        while end == -1:
            print("-----------------------------Règles du jeu --------------------------------------")
            print("Le but du tétris est de placer des blocs sur un tableau de manière à la remplir entièrement")
            print("Vous devez remplir le tableau en un minimum de coups possibles")
            print("Vous ne pouvez pas placer un bloc sur une case déjà prise et il ne doit pas sortir du tableau\n")
            print("Appuyer 1 pour revenir au menu principal :")
            end = int(input())
    if reponse == 2 :
        print("-----------------------------Choix du plateau--------------------------------------")
        print("Quelle forme de plateau voulez-vous ? Choisissez en entrant le chiffre correspondant : \n")
        print("1 - Losange")
        print("2 - Cercle")
        print("3 - Triangle ")
        path = int(input())
        while path < 1 or path > 3:
            path = int(input("Veuillez vérifier que votre chiffre est correct et réessayez "))
        if path == 1:
            print("Vous avez choisi le losange, Bonne chance !!\n")
        elif path == 2:
            print("Vous avez choisi le Cercle, Bonne chance !!\n")
        elif path == 3:
            print("Vous avez choisi le Triangle, Bonne chance !! \n")
        print("--------------------------Mode de Jeu ----------------------------------")
    print("Choisissez un mode de jeu en entrant 1 ou 2 :\n")
    print("1 - Choix manuel des blocs ")
    print("2 - 3 blocs sélectionnés aléatoirement \n")
    reponse3 = int(input())
    while reponse3 < 0 or reponse3 > 2:
        reponse3 = int(input(" Le chiffre n'est pas reconnu veuillez réessayer ") )
read_grid(path, grid)
print_grid(grid)
select_bloc(reponse3)
while Testjeu == False:
    valid_position(grid, bloc)
    emplace_bloc(grid, bloc, Xi, Yi, Valid_pos)
    row_state(grid)
    update_score(row_test, score)
    row_clear(grid, row_test, row_len, score)
    bloc = []
    print_grid(grid)
    select_bloc(reponse3)
    
    