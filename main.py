import time

#   Paramètres officiels

"""
Zemidjan (taxi-moto)

-   Tarif de base: 150 FCFA
-   Prix au km   :  75 FCFA/km
-   Majoration heure de pointe: +15% sur le prix total
______________________________________________________

Taxi (Voiture)

-   Tarif de base: 200 FCFA
-   Prix au km   : 150 FCFA/km
-   Majoration heure de pointe: +25% sur le prix total

"""

#   Déclaration des constantes et variables
#   CONSTANTES
#   Zemidjan
PRIX_DE_BASE_ZEM = 150
PRIX_ZEM_KM = 75
MAJORATION_ZEM = 0.15

#   Taxi
PRIX_DE_BASE_TAXI = 200
PRIX_TAXI_KM = 100
MAJORATION_TAXI = 0.25

#   Variables
kilometrage = float()
heure = int()

#   Affichage de bienvenue à l'utilisateur

print(60*'_')
print(" Bienvenue sur Midjo ".center(60,' '))
print(60*'_')
print("\nCet programme écrit en Python vous permet de déterminer le \ncoût de toutes vos courses à Lomé.")


#   Collecte d'information sur le trajet

try:


