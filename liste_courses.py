# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py liste_courses.py"

# Variables
liste_course = {
    "pates": 2,
    "sauce tomate": 1,
    "parmesan": 1
}

# Fonctions



def Ajouter():
    article = input('Quel article voulez vous ajouter?')
    quantite = int(input('Quelle quantite voulez vous en ajouter?'))
    liste_course[article] = quantite

def Supprimer():
    afficher_liste_numerotee(liste_course)
    numero_supprimer = int(input('Entrez le numéro de l\'article à supprimer: '))

def afficher_liste_numerotee(liste):
    for i, (article, quantite) in enumerate(liste.items(), start=1):
        print(f"{i} - {article}: {quantite}")

def Modifier():
    afficher_liste_numerotee(liste_course)

def show_actions():
    print("1 - Ajouter")
    print("2 - Supprimer")
    print("3 - Modifier")
    print("4 - Quitter")


    




#########################
### Début du programe ###
#########################

print("Bienvenue dans la liste de courses.\n")
print("Que voulez vous faire ?")
show_actions()
saisi = int(input('Quelle chiffre'))

if saisi == 1:
    Ajouter()

if saisi == 2:
    Supprimer()
    
print("A bientot")