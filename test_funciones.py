import pytest
from codigo import funciones

@pytest.mark.parametrize(
    "a, b, expected",
    [ 
        (3,4,7),
        (3,5,8)
    ]
)

def test_suma(a,b, expected):
    funciones.suma(a,b) == expected


@pytest.mark.parametrize(
    "some_input, some_output",
    [ 
        ("A", 1),
        ("B", 2)
    ]

)

def test_some(some_input, some_output):
    assert funciones.some(some_input) == some_output