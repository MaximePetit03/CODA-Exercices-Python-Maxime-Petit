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

#Exercice 4
def exercice4():
    année = int(input("En quelle année est tu né(e) ?"))
    année_actuelle = 2025
    age = année_actuelle - année
    print(age)

#Exercice 5
def exercice5():
    a = int(input("Donnez un nombre positif"))
    b = int(input("donner un 2ème nombre positif à additionner au précédent"))
    c = a + b
    print(c)

#Exercice 6
def exercice6():
    a = int(input("Donnez un nombre positif"))
    b = int(input("donner un 2ème nombre positif à soustraire au précédent"))
    c = a - b
    print(c)

#Exercice 7
def exercice7():
    a = int(input("Donnez un nombre positif"))
    b = int(input("donner un 2ème nombre positif à multiplié au précédent"))
    c = a * b
    print(c)


def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2" :
        exercice2()
    elif choix == "3" :
        exercice3()
    elif choix == "4" :
        exercice4()
    elif choix == "5" :
        exercice5()
    elif choix == "6" :
        exercice6()
    elif choix == "7" :
        exercice7()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
