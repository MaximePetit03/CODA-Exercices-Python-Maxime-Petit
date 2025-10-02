# Exemple avec un seul exercice
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

# Exercice 2
def exercice2():
    prénom = input("Comment tu t'appelles ?")
    print("Bonjour", prénom," ! ")

#Exercice 3
def exercice3():
    print("Bonjour\n au revoir\n merci")

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2" :
        exercice2()
    elif choix == "3" :
        exercice3()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
