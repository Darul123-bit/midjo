import datetime 

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
PRIX_TOTAL = 0.0
kilometrage = float()
heure = datetime.now()
heurePointe = (datetime.time(7, 00) <= heure <= datetime.time(8, 45)) or (datetime.time(11, 45) <= heure <= datetime.time(13, 00)) or (datetime.time(17, 00) <= heure <= datetime.time(19, 00))
print(heurePointe)

#   Affichage de bienvenue à l'utilisateur
print(60*'_')
print(f'heure: {heure}')
print(60*'_')
print(" Bienvenue sur Midjo ".center(60,' '))
print(60*'_')
print("\nCet programme écrit en Python vous permet de déterminer le \ncoût de toutes vos courses à Lomé.")
print(60*'_')



#   Collecte d'information sur le trajet

try:
    print("Quelle moyen de transport utiliserez-vous ?".center(60, ' '))
    print()
    print("\t1 • Zemidjan (Taxi-moto)")
    print("\t2 • Taxi (Voiture)")
    print(60*'_')
    choix = int(input("\tTapez 1 ou 2 : "))

    while True:
        if choix in range(1, 3, 1):
            
            break           
        else:
            print(60*'_')
            print("\t1 • Zemidjan (Taxi-moto)")
            print("\t2 • Taxi (Voiture)")
            print(60*'_')
            choix = int(input("\tTapez 1 ou 2 : "))

    print(60*'_')
    kilometrage = float(input("\tQuelle est la distance de vôtre trajet ? : "))
    if kilometrage > 0.0:
        pass
    elif kilometrage == 0.0:
        print("Votre saisie est incorrecte")
        kilometrage = float(input("Quelle est la distance de vôtre trajet ? : "))
    else:
        print("Veuillez entrez une distance supérieur à 0 en km")
        kilometrage = float(input("Quelle est la distance de vôtre trajet ? : "))        
except:
        print("Veuillez entrer des informations valides")


match choix:
    case 1:
        if heurePointe:
            PRIX_TOTAL = (PRIX_DE_BASE_ZEM + (PRIX_ZEM_KM*kilometrage))
            PRIX_TOTAL *= MAJORATION_ZEM
        else:
            PRIX_TOTAL = (PRIX_DE_BASE_ZEM + (PRIX_ZEM_KM*kilometrage))
    case 2:
        if heurePointe:
            PRIX_TOTAL = (PRIX_DE_BASE_TAXI + (PRIX_TAXI_KM*kilometrage))
            PRIX_TOTAL *= MAJORATION_TAXI
        else:
            PRIX_TOTAL = (PRIX_DE_BASE_TAXI + (PRIX_TAXI_KM*kilometrage))

print(60*'_')
print(f"Vôtre trajet vous reviens à {PRIX_TOTAL}".center(60, ' '))
print(60*'_')
