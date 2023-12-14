
# Exercice 1 :


# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombre : ")

# Convertit la liste de chaine de caractère en liste de nombre
liste_nombres = [int(nombre) for nonbre in liste_nombres.split()]

# Calcul de la somme des nombres de la liste
somme = 0
for nombre in liste_nombres:
    somme += nombre

# Affichage de la somme des nombre de la liste
print("La somme des nombres de la liste est : ", somme)



#**********************************************
print("---------------------------------------")
#**********************************************


# Exercice 2 :


# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombre : ")

# Convertit la liste de chaine de caractère en liste de nombre
liste_nombres = [int(nombre) for nonbre in liste_nombres.split()]

# Initialisation du compteur de nombre pair
nb_nombre_pairs = 0

# Itère sur la liste de somme
for nombre in liste_nombres:
    # Vérifie si le nombre pair
    if nombre % 2 == 0:
        # Incrémentation du compteur
        nb_nombre_pairs +=1

# Affiche le nombre de nombres pairs de la liste
print("Le nombre de nombres pairs de la liste est : ", nb_nombre_pairs)


#**********************************************
print("---------------------------------------")
#**********************************************


# Exercice 3 :


# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombre : ")

# Convertit la liste de chaine de caractère en liste de nombre
liste_nombres = [int(nombre) for nonbre in liste_nombres.split()]

# Tri la liste par ordre croissant
liste_nombres.sort()

# Affichage de la liste triée par ordre croissant
print("La liste triée par ordre croissant est : ", liste_nombres)



#**********************************************
print("---------------------------------------")
#**********************************************


# Exercice 4 : 


# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombre : ")

# Convertit la liste de chaine de caractère en liste de nombre
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Inverse la liste
liste_nombres.reverse()

# Affichage de la liste inversée
print("La liste inversée est : ", liste_nombres)


#**********************************************
print("---------------------------------------")
#**********************************************


# Exercice 5 :


# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombre : ")

# Convertit la liste de chaine de caractère en liste de nombre
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Demander à l'utilisateur de saisir le nombre à rechercher
nombre_a_rechercher = int(input("Saisisez le nombre : "))

nb_occurrence = 0 

# Itère sur la liste de nombres
for nombre in liste_nombres:
    # Vérifie si le nombre est égal au nombre à rechercher
    if nombre == nombre_a_rechercher:
        # Incrémente le compteur
        nb_occurrence +=1

# Affiche le nombre d'occurrence

print("Le nombre d'occurrence est de : ", nb_occurrence)


#**********************************************
print("---------------------------------------")
#**********************************************


# Exercice 7 :


# Demande à l'utilisateur de saisir une liste de nombres
liste_nombres = input("Saisissez une liste de nombre : ")

# Convertit la liste de chaine de caractère en liste de nombre
liste_nombres = [int(nombre) for nombre in liste_nombres.split()]

# Demander à l'utilisateur de saisir le nombre à rechercher
valeur_a_rechercher = int(input("Saisisez la valeur à rechercher : "))

# Initialiser les listes des nombre à la valeur donnée
liste_nombres_inferieurs = []
liste_nombres_superieurs = []

# Itérer sur la liste nombres

for nombre in liste_nombres:
    # Ajoute le nombre a la liste des nombres inferieurs à la  valeur donnée
    if nombre < valeur_a_rechercher:
        liste_nombres_inferieurs.append(nombre)
    else:
        liste_nombres_superieurs.append(nombre)
    print("La liste avec les nombres supérieur à la valeur donnée placés en fin de liste est : ", liste_nombres)



#**********************************************
print("---------------------------------------")
#**********************************************  