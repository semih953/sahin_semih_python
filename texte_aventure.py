personnage = {
    "PV": 70
}

pouvoirs = [
    "Un pour Tous",
    "Contrôler la gravité",
    "Faire des explosions",
    "Être une grenouille",
    "Créer des objets",
    "Mi-chaud mi-froid",
    "Aller très vite"
]

plats = "Ramen,Onigiri,Udon,Curry"                     # À transformer en liste     
liste_plats = ["Ramen", "Onigiri", "Udon", "Curry"]  
print(liste_plats)
                    

plats_stock = {"Ramen": 2, "Onigiri": 2, "Udon": 2, "Curry": 2}  # À remplir avec les plats

objets_cles = ["smartphone"]
inventaire = {}

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************


def proposer_lieux(mots_cles):
    lieux_disponibles = [
        "Hall d'entrée",
        "Couloir du RDC",
        "Classe 1-A",
        "Couloir du 1er étage",
        "Cafétéria",
        "Salle d'entraînement"
        ]
    # A remplir ici
    print(lieux_disponibles)

def proposer_actions(actions):
    actions_disponibles = "│[Actions] "
    # A remplir ici
    print("Actions disponibles :")
    print("1. Observer")
    print("2. Quitter")
    print("3. Demander le passe")
    print("4. Montrer les badges")
    print("5. Manger")
    print("6. Combattre")

def action_hall():
    print("Actions disponibles :")
    print("1. Observer")
    print("2. Quitter")


def action_couloir_rdc():
    print("Actions disponibles :")
    print("1. Observer")


def action_classe_1A():
    print("Actions disponibles :")
    print("1. Observer")
    print("2. Demander le passe")
    print("3. Montrer les badges")


def action_couloir_1er_etage():
    print("Actions disponibles :")
    print("1. Observer")


def action_cafeteria():
    print("Actions disponibles :")
    print("1. Observer")
    print("2. Manger")


def action_salle_entrainement():
    print("Actions disponibles :")
    print("1. Observer")
    print("2. Combattre")

def choisir_action(lieu):
    if lieu == "Hall d'entrée":
        action_hall()
    elif lieu == "Couloir du RDC":
        action_couloir_rdc()
    elif lieu == "Classe 1A":
        action_classe_1A()
    elif lieu == "Couloir du 1er étage":
        action_couloir_1er_etage()
    elif lieu == "Cafétéria":
        action_cafeteria()
    elif lieu == "Salle d'entraînement":
        action_salle_entrainement()

# ********************************************************************************
# INTRODUCTION
# ********************************************************************************


def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    print("===============================")
    print("Commençons par créer ton personnage.")
    print("\nQuel âge as-tu ?")

    # Demander un âge et écrire cette information dans le dictionnaire "personnage"
    age = input("Quel âge as-tu ? ")
    personnage["âge"] = age

    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un
    print("\nVoici la liste des pouvoirs disponibles :")
    for x, pouvoir in enumerate(pouvoirs, 1):
        print(f"{x}. {pouvoir}")

    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"
    choix_pouvoir = int(input("Choisit ton personnage avec son numéro : "))
    personnage["pouvoir"] = pouvoirs[choix_pouvoir : 1]

    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"


    lieu_hall()

# ********************************************************************************
# LIEUX
# ********************************************************************************


def lieu_hall():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_lieux(["couloir_rdc, classe_1A"])  # À compléter
        proposer_actions(["quitter, observer"])  # À compléter
        reponse = input("├─> ")
        print("└────────────────────────────────────────")


        if reponse == "quitter":
            print("Tu décides de quitter le jeu.")
            break  # Sortir de la boucle while

        elif reponse == "observer":
            print("Tu observes attentivement les environs.")

        elif reponse == "couloir_rdc":
            print("Tu te diriges vers le couloir du rez-de-chaussée.")
            lieu_couloir_rdc()  # Appeler la fonction pour le lieu du couloir du RDC

        elif reponse == "classe_1a":
            print("Tu te diriges vers la classe 1-A.")
            lieu_classe_1a() 

        # Gérer ici toutes les réponses possibles, qu'elles soient correctes ou non


def lieu_couloir_rdc():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est le couloir du rez de chaussé.")
    print("On y trouve entre autres le couloir du 1er étage.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_lieux(["couloir_1er_etage, classe_1A"])  # À compléter
        proposer_actions(["observer"])  # À compléter
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

        if reponse() == "observer":
            # Observer l'environnement
            print("Vous observez votre environnement.")
        elif reponse() in ["couloir_1er_etage", "classe_1A"]:
            # Aller vers le lieu choisit
            print(f"Vous vous dirigez vers {reponse}.")
            break  # Sort de la boucle while pour continuer avec le nouveau lieu choisi
        else:
            print("Réponse invalide. Veuillez choisir une option valide.")  # Si la réponse n'est pas valide


def lieu_couloir_1er_etage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\Tu viens d'entrer dans le couloir du 1er étage.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_lieux(["salle_entrainement, cafeteria"])  # À compléter
        proposer_actions(["observer"])  # À compléter
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

def lieu_cafeteria():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nTu viens d'entrer dans la Caféteria.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_lieux(["couloir_1er_etage, salle_entrainement"])  # À compléter
        proposer_actions(["observer, manger"])   
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

def manger():
    print("Vous avez choisi de manger.")
    plat = input("Quel plat souhaitez-vous manger ? ")

    if plat in plats_stock and plats_stock[plat] > 0:
        print(f"Vous mangez {plat} et gagnez 10 PV.")
        personnage["PV"] += 10
        plats_stock[plat] -= 1
        print(f"PV actuels : {personnage['PV']}")
    else:
        print("Ce plat n'est plus disponible.")


def lieu_salle_entrainement():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\Tu viens d'entrer dans la salle d'entraînement.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_lieux(["salle_entrainement"])  # À compléter
        proposer_actions(["observer, combattre"])  # À compléter
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

def combattre():
    print("Tu entres dans la salle d'entraînement et commence le combat.")
    pv_pnj = 100
    pv_joueur = 100

    while pv_pnj > 0 and pv_joueur > 0:
        print(f"PV du mannequin : {pv_pnj}")
        print(f"Vos PV : {pv_joueur}")

        action = input("Faite votre choix (combattre/refuser) :")

        if action == "combattre":
            pv_pnj -= 20
            print("Vous attaquez le pnj.")

            if pv_pnj > 0:
                pv_joueur -= 10
                print("Le pnj riposte.")
            else:
                print("Vous avez vaincu le pnj et gagnez un badge.")
                if "badge" in inventaire:
                    inventaire["badge"] += 1
                else:
                    inventaire["badge"] = 1
        elif action == "fuir":
            print("Vous fuyez le combat.")
            break
        else:
            print("Action invalide. Choisissez une action valide.")
    else:
        if pv_joueur <= 0:
            print("Vous avez perdu. Fin du jeu.")
            exit()

def lieu_classe_1a():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la classe 1A.")
    print("On y trouve le proffeseur.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_lieux(["couloir_rdc, haull d'entrée"])  # À compléter
        proposer_actions(["observer, demander le passe, montrer les badges"])  # À compléter
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

def demander_passe():
    if "passe" not in objets_cles:
        objets_cles.append("passe")
        print("Vous avez obtenu le passe pour la salle d'entraînement.")
    else:
        print("Vous avez déjà le passe.")

def montrer_badges():
    if "badge" in inventaire and inventaire["badge"] >= 3:
        print("Félicitations ! Vous avez montré trois badges. Vous avez réussi !")
        print("Fin du jeu.")
        exit()
    else:
        print("Vous n'avez pas assez de badges.")






# ********************************************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")