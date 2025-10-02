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

#Exercice 8
def exercice8():
    a = int(input("Donnez un nombre positif"))
    b = int(input("donner un 2ème nombre positif à diviser au précédent"))
    c = a / b
    print(c)

#Exercice 9
def exercice9():
    a = int(input("Donnez un nombre"))
    b = a**2 
    print(b)

#Exercice 10
def exercice10():
    a = int(input("Donnez un nombre"))
    b = a*2 
    print(b)

#Exercice 11
def exercice11():
    a = int(input("Donnez un nombre"))
    b = a/2 
    print(b)

#Exercice 12
def exercice12():
    for i in range(5):
        print("bonjour")

#Exercice 13
def exercice13():
    for i in range (1, 6):
     print(i)

#Exercice 14
def exercice14():
    n = int(input("Entrez un chiffre ou un nombre "))
    print("La table de multiplication de ", n,"est :")
    for i in range(1,6):
     print(i , " x ", n, " = ",i*n)

#Exercice 15
def exercice15():
    longueur = int(input("Donner moi la longueur d'un coté d'un carré :"))
    périmètre = longueur*4
    print("le périmètre de ce carré est :", périmètre)

#Exercice 16
def exercice16():
    longueur = int(input("Donner moi la longueur d'un coté d'un carré :"))
    aire = longueur**2
    print("l'aire de ce carré est :", aire)

#Exercice 17
def exercice17():
    euro = int(input("Donne moi une somme d'argent : "))
    dollars = euro*1.1
    print("L'équivalent en dollars est", dollars)

#Exercice 18
def exercice18():
    minute = int(input("Donne moi un temps en minute à convertir en seconde : "))
    seconde = minute*60
    print("Ton temps en seconde est :", seconde)

#Exercice 19
def exercice19():
    prixHt = int(input("Donner un prix pour y ajouter la TVA : "))
    TVA = 20/100
    PrixTVA = prixHt*(1+TVA)
    print("Votre prix vaut", PrixTVA, "avec la TVA")



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
    elif choix == "8" :
        exercice8()
    elif choix == "9" :
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()
