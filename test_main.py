import pytest
from main import suma, resta, saludo, palindromo

def test_suma():
    assert suma(3,4)==7

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [ 
        (3,2,5),
        (2,3,5),
        (2,2,4),
        (suma(3,2),5,10),
        (3,suma(2,5),10)
    ]
)
def test_multi(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [ 
        (5,3,2),
        (5,2,3),
        (resta(6,2), 3, 1),
        (10,resta(3,2),9)
    ]
    
)

def test_resta(input_a, input_b, expected):
    assert resta(input_a,input_b) == expected


@pytest.mark.parametrize(
    "frase, expected",
    [ 
        ("naomi", "hola naomi"),
        ("mauro", "hola mauro")
    ]
)

def test_saludo(frase,expected):
    assert saludo(frase)==expected


@pytest.mark.parametrize(
    "palabra, expected",
    [ 
        ("oso", "es un palindromo"),
        ("naomi", "no es palindromo")
    ]
)

def test_palindromo(palabra, expected):
    assert palindromo(palabra) == expected

