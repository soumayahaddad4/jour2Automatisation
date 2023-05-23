#1- Installer pytest (pip --install pytest)
#2- créer un fichier python qui contient le mot "test" au début
#3- importer le pachage "pytest"
#4- creer des fonctions tests
#5- Pour exécuter les test on doit aller dans le dossier des tests et on exécute la commande suivante:
# pytest test_premierTest.py -s -v (-s: pour visualiser sous forme de caractere, -v :pour afficher plus de contenu
import pytest

def test_login():
    print("se connecter sur google")
def test_creerCompte():
    print("créer compte google")