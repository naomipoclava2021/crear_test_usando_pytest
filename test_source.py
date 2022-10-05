import pytest
from my_librery import utils

def test_sum():
    a =5 
    b = 4
    assert utils.suma(a,b) == 9


def test_rest():
    assert utils.resta(2,1)==1



def test_multiplicacion():
    assert utils.multiplicacion(2,2)==4


def test_string_a_lista():
    assert utils.string_a_lista("hola") == ["h", "o", "l", "a"]

def test_saludo():
    assert utils.saludo("naomi") == "hola naomi"
