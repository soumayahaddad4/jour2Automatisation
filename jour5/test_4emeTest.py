#ajouter des annotations (@pytest.mark.usefixtures("setup","before"))pour ajouter les setup et teardown
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

@pytest.mark.usefixtures("setup","before")
def test_login(setup,before):

    print("se connecter sur google")

@pytest.mark.usefixtures("setup","before")
def test_creerCompte(setup,before):
    print("créer compte google")

@pytest.mark.usefixtures("setup","before")
def test_reinitialiser_mot_pass():
    print("reinitialise le mot de passe")