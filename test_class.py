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