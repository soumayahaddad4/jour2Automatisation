#1- il ya des lignes qui se repete :DRY("Dont Repeat Yourself"): ouverture et fermeture de navigateur se repètent
#2- il y'a une solution:de hook (pre et post conditions)
#def teardown_function(function): execution apres chaque fonction 0
# def teardown_module(module):execution apres chaque module ou suite de test
import pytest

def setup_module(module):
    print("ouvrir le navigateur")

def teardown_module(module):
    print("fermer le navigateur")

def test_login():
    #print("ouvrir le navigateur")
    print("se connecter sur google")
   # print("fermer le navigateur")

def test_creerCompte():
    #print("ouvrir le navigateur")
    print("créer compte google")
    #print("fermer le navigateur")

def test_reinitialiser_mot_pass():
    print("reinitialise le mot de passe")

