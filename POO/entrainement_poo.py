# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py entrainement_poo.py"

# Init variables
hero = None
monstre = None

armes = {"Epée": 5, "Arc": 4, "Couteau à beurre": 1}


# Init classes


class Creature():
    
    degats = 0

    def __init__(self, degats, pv):
        self.degats = degats
        self.pv = pv

    def attaque(self, cible):
        cible.subir_degats(self.degats)

    def subir_degats(self, degats):
        self.pv -= degats

class Hero(Creature):
    def __init__(self, nom, pv, degats, pm):
        super().__init__(pv, degats)
        self.nom = nom
        self.pm = pm

    def magie(self, cible):
        if self.pm >= 1:
            cible.subir_degats(self.degats * 2)
            self.pm -= 1
        else:
            print("Mana insuffisant !")

    def afficher_etat(self):
        print(f"{self.nom} - PV: {self.pv}, PM: {self.pm}")


class Monster(Creature):
    def venin(self, cible):
        cible.etat = "Empoisonné"
        print(f"{cible.nom} est empoisonné !")

# Début du jeu


def intro():
    print("===============================================================")
    print("|| Bienvenue dans le système de combat POO (Punch Out Out) ! ||")
    print("===============================================================")
    print("\nQuel est le nom de ton héros.")
    # Choix du nom, choix de l'arme

    nom_hero = input("Nom du héros : ")
    arme = input("Choisissez votre arme (Epée, Arc, Couteau à beurre) : ")


    degats_arme = armes.get(arme, 1)  # Utilisation du dictionnaire d'armes
    global hero, monstre
    hero = Hero(nom_hero, 15, degats_arme, 5)

    # Attention pour modifier les variables globales dans une fonction en python vous devez d'abord utiliser cette ligne
    monstre = Monster(20, 5)

    combat()

# Boucle de combat


def combat():
    while hero.pv > 0 and monstre.pv > 0:
        print("\nTour du héros")
        print("1. Attaque normale")
        print("2. Attaque magique")
        choix = input("Choisissez une action : ")

        if monstre.pv <= 0:
            print("Le monstre est vaincu ! Victoire !")
            break

        print("\nTour du monstre")
        monstre.attaque(hero)

        if hero.pv <= 0:
            print("Le héros est vaincu ! Défaite !")
            break

    


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
