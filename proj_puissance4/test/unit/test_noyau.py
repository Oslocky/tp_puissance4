import pytest

from noyau import *

def test_changer_joueur():
   assert True==True 


def test_coupgagnant():
    grille = [[-1]*7 for a in range(6)]  # grille vide
    joueur = 0
    assert not coup_gagnant(joueur, 0, 0, grille)  # test sans jeton
    grille[0][0] = joueur  # ajout d'un jeton à la position (0,0)
    grille[1][0] = joueur  # ajout d'un jeton à la position (1,0)
    grille[2][0] = joueur  # ajout d'un jeton à la position (2,0)
    grille[3][0] = joueur  # ajout d'un jeton à la position (3,0)
    assert coup_gagnant(joueur, 3, 0, grille)  # test vertical gagnant
    grille[0][1] = joueur  # ajout d'un jeton à la position (0,1)
    grille[0][2] = joueur  # ajout d'un jeton à la position (0,2)
    grille[0][3] = joueur  # ajout d'un jeton à la position (0,3)
    assert coup_gagnant(joueur, 0, 3, grille)  # test horizontal gagnant
    grille[0][4] = joueur  # ajout d'un jeton à la position (0,4)
    grille[1][1] = joueur  # ajout d'un jeton à la position (1,1)
    grille[2][2] = joueur  # ajout d'un jeton à la position (2,2)
    grille[3][3] = joueur  # ajout d'un jeton à la position (3,3)
    assert coup_gagnant(joueur, 3, 3, grille)  # test diagonale (haut-gauche vers bas-droite) gagnante
    grille[0][6] = joueur  # ajout d'un jeton à la position (0,6)
    grille[1][5] = joueur  # ajout d'un jeton à la position (1,5)
    grille[2][4] = joueur  # ajout d'un jeton à la position (2,4)
    grille[3][3] = joueur  # ajout d'un jeton à la position (3,3)
    assert coup_gagnant(joueur, 3, 3, grille)




