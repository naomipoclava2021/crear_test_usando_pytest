import pytest
from main import suma, Calculadora

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [ 
        (2,3,5),
        (3,2,5),
        (suma(3,2),5,10),
        (5,suma(3,2), 10)
    ]
)

def test_suma(input_a, input_b, expected):
    suma(input_a, input_b) == expected


def test_class_monkey(monkeypatch):
    monkeypatch.setattr(Calculadora, "sumar", lambda x:4)
    c = Calculadora()
    assert c.sumar() == 4

def test_class_resta(monkeypatch):
    monkeypatch.setattr(Calculadora, "resta", lambda x:5)
    c = Calculadora()
    assert c.resta() == 5

def test_class_multiplicar(monkeypatch):
    monkeypatch.setattr(Calculadora, "multiplicar", lambda x:4)
    c = Calculadora()
    assert c.multiplicar() == 4

def test_class_dividir(monkeypatch):
    monkeypatch.setattr(Calculadora, "dividir", lambda x: 5)
    c=Calculadora()
    assert c.dividir() == 5