"""
Cours "Introduction 1" - Exercice "Billetterie"
"""

# Variables
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8,
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}
stations_names = list(stations.keys())
stations_distances = list(stations.values())
nb_billets_adulte = 0
has_reduit = False

# Introduction
print("           /////// ")
print("         ///       ")
print("  //////////////   ")
print("      ///          ")
print("///////            ")
print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")

# Questions à l'utilisateur

nb_billets_adulte = int(input("Combien de billets adulte voulez-vous? "))
reponse_tarif_reduit = input("Voulez-vous des billets à tarif réduit? (Oui/Non) ")

if reponse_tarif_reduit == "oui":
    nb_billets_tarif_reduit = int(input("Combien de billets à tarif réduit désirez-vous? "))
    has_tarif_reduit = True

# Calculs de l'itinéraire

print("\nStations de la Airport Line:")
for i, station in enumerate(stations_names):
    print(f"{i}. {station}")

while True:
    depart_index = int(input("\nEntrez le numéro de la station de départ: "))
    if 0 <= depart_index < len(stations_names):
        station_depart = stations_names[depart_index]
        break
    else:
        print("Numéro de station invalide. Veuillez réessayer.")

while True:
    arrivee_index = int(input("\nEntrez le numéro de la station d'arrivée: "))
    if 0 <= arrivee_index < len(stations_names):
        station_arrivee = stations_names[arrivee_index]
        break
    else:
        print("Numéro de station invalide. Veuillez réessayer.")

# Choix de la bonne zone tarifaire
        
zones_tarifaires = [
    {"zone": 1,"distance_min": 0,"distance_max": 3,"billet_adulte": 210,"tarif_reduit": 110},
    {"zone": 2,"distance_min": 3.1,"distance_max": 7,"billet_adulte": 260,"tarif_reduit": 130},
    {"zone": 3,"distance_min": 7.1,"distance_max": 11,"billet_adulte": 300,"tarif_reduit": 150},
    {"zone": 4,"distance_min": 11.1,"distance_max": 15,"billet_adulte": 340,"tarif_reduit": 170},
]

for zone in zones_tarifaires:
    if zone["distance_min"]<= zone["distance_max"]:
        zone_tarifaire = zone
        break

# Calcul du coût total
    
cout_total = nb_billets_adulte * zone_tarifaire['billet_adulte']
cout_total_reduit = nb_billets_tarif_reduit * zone_tarifaire['tarif_reduit']

cout_total += cout_total_reduit
print(f"\nCoût total : {cout_total} yens")

# Affichage des détails du voyage et du tarif

# Affichage de la voie du train à emprunter

voie = 1 if depart_index < arrivee_index else 2
print(f"\nEmpruntez la voie {voie} :")
print(" - Dans le sens Meinohama > Fukuokafuko" if voie == 1 else " - Dans le sens inverse")
