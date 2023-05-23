# execution avec un marqueur (
import pytest

# @pytest.fixture(scope="module")
# def setup():
#     print("ouvrir la base de donnée")
#     yield
#     print("fermer la base de donnée")
# @pytest.fixture(scope="function")



@pytest.mark.soumaya
def testpremier():

    print("1")

@pytest.mark.charge
def test_2eme():
    print("2")

@pytest.mark.charge
def test_3eme():
    print("3")
@pytest.mark.skip
def test_4eme():
    print("4")

@pytest.mark.regression
def test_5eme():
    print("5")