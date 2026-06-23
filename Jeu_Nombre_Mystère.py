import random

def niveau():
    while True:
        choix = input("Choisi un niveau (Facile / Difficile / Hardcore) : ")

        if choix == "Facile":
            return random.randint(0, 30), None

        elif choix == "Difficile":
            return random.randint(0, 100), None

        elif choix == "Hardcore":
            return random.randint(0, 500), 10
        
        else:
            print("Niveau invalide, recommence.")

def message ():

    liste = [
    "Bravo, tu es un génie !",
    "Incroyable, tu as trouvé !",
    "Bien joué, champion !",
    "Tu maîtrises le jeu 👑",
    "Facile pour toi 😎",
    "Tu es imbattable !",
    "Quel talent !",
    "GG, victoire parfaite !",
    "Tu l'as explosé 💥",
    "Mission accomplie !"]

    return random.choice(liste)


def jeu_devine():
    nombre, limite = niveau()
    nb_essais = 0

    while True:
        try:
            nombre_donne = int(input("Donne un chiffre ? "))
        except ValueError:
            print("Erreur : Ce n'est pas un nombre")
            continue  

        nb_essais += 1

        if limite is not None and nb_essais >= limite:
            print("Bien tenté, mais tu as échoué !")
            break

        if nombre_donne > nombre:
            print("Nombre d'essais :", nb_essais)
            print("Trop grand !")

        elif nombre_donne < nombre:
            print("Nombre d'essais :", nb_essais)
            print("Trop petit ...")

        else:
            print("Nombre d'essais :", nb_essais)
            print(message())
            break

jeu_devine()
#print(type((1,4)))