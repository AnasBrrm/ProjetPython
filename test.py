def rotate_bloc (bloc, alea, reponse3, n):
    if reponse3 == 1:
        print("Veuillez selectionner une rotation :")
            print("\n", h + 1, ": \n", end="")
            for i in range(len(list_bloc[n])):
                for j in range(len(list_bloc[n][i])):
                    if list_bloc[h][i][j] == 1:
                        print("■", end=" ")
                    else:
                        print(". ", end="")
                print()
    