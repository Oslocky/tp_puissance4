import pytest

from noyau import *

def test_exemple():
   joueur=0
   i=2
   j=0
   grille=[[-1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1],
           [0, -1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1],
           [0,  1, -1, -1, -1, -1, -1]]
   assert True==True

def jeton():
    # implementation de la fonction jeton
    pass

def coup_gagnant():
    # implementation de la fonction coup_gagnant qui utilise la fonction jeton
    pass

def test_coup_gagnant():
    # Test d'intégration pour la fonction coup_gagnant

    # Préparer les entrées
    grille = [[None]*7 for _ in range(6)] # une grille vide de 6x7

    # Appeler la fonction coup_gagnant et obtenir la sortie
    jeton_a_jouer = jeton()
    colonne = coup_gagnant(grille, jeton_a_jouer)

    # Vérifier la sortie
    assert colonne in range(7), f"La colonne renvoyée n'est pas dans la plage valide (0-6). colonne = {colonne}"

    # Tester la fonction jeton dans le contexte de coup_gagnant
    jeton_joue = grille[0][colonne]
    assert jeton_joue == jeton_a_jouer, f"Le jeton joué ({jeton_joue}) n'est pas le même que le jeton obtenu ({jeton_a_jouer})."

    # Tester que la colonne renvoyée est bien un coup gagnant
    # (à adapter selon les règles spécifiques du jeu)
    # Si aucun coup gagnant n'est possible, le test peut être ignoré.
    ligne_gagnante = verifier_coup_gagnant(grille, jeton_a_jouer, colonne)
    assert ligne_gagnante is not None, f"Aucun coup gagnant n'est possible pour la colonne {colonne}."



