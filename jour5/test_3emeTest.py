#autres concepts basés sur les annotations au lieu de set_up et teardown(module)

import pytest

@pytest.fixture(scope="module")
def setup():
    print("ouvrir la base de donnée")
    yield
    print("fermer la base de donnée")
@pytest.fixture(scope="function")
def before():
    print("ouvrir le navigateur")
    yield
    print("fermer le navigateur")

def test_login(setup,before):

    print("se connecter sur google")


def test_creerCompte(setup,before):

    print("créer compte google")


def test_reinitialiser_mot_pass():
    print("reinitialise le mot de passe")