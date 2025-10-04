import pytest 
from Calculadora import Calculadora

# particao de equivalencia

# soma
@pytest.mark.parametrize("val1, val2, resultado", [
    # int+
    (2, 3, 5),

    # int- e int+
    (-7, 5, -2),

    # zero
    (0, 0, 0),
    (0, 9, 9),

    # float
    (2.5, 3.1, 5.6),
    (-7.2, 0.5, -6.7),
])
def test_soma_pe(val1, val2, resultado):
    if isinstance(resultado, float) or isinstance(val1, float) or isinstance(val2, float):
        assert Calculadora.soma(val1, val2) == pytest.approx(resultado)
    else:
        assert Calculadora.soma(val1, val2) == resultado

# sub
@pytest.mark.parametrize("val1, val2, resultado", [
    # int+
    (5, 3, 2),

    # int- e int+
    (-7, 5, -12),

    # zero
    (0, 0, 0),
    (0, 9, -9),

    # float
    (2.5, 3.1, -0.6),
])
def test_sub_pe(val1, val2, resultado):
    if any(isinstance(x, float) for x in [val1, val2, resultado]):
        assert Calculadora.sub(val1, val2) == pytest.approx(resultado)
    else:
        assert Calculadora.sub(val1, val2) == resultado

# mult
@pytest.mark.parametrize("val1, val2, resultado", [
    # int+
    (2, 3, 6),

    # int- e int+
    (-7, 5, -35),

    # int- e int-
    (-7, -2, 14),

    # zero
    (0, 9, 0),

    # float
    (2.5, 3.1, 7.75),
])
def test_mult_pe(val1, val2, resultado):
    if any(isinstance(x, float) for x in [val1, val2, resultado]):
        assert Calculadora.mult(val1, val2) == pytest.approx(resultado)
    else:
        assert Calculadora.mult(val1, val2) == resultado

# div
@pytest.mark.parametrize("val1, val2, resultado", [
    # int+
    (6, 3, 2.0),

    # int- e int+
    (-7, 5, -1.4),

    # int+ e int-
    (7, -2, -3.5),

    # float
    (7.5, 2.5, 3.0),
    (-7.2, 0.5, -14.4),

    # float negativo
    (7.5, -2.5, -3.0),

    # zero no numerador
    (0, 9, 0.0),
])

def test_div_pe(val1, val2, resultado):
    assert val2 != 0
    if any(isinstance(x, float) for x in [val1, val2, resultado]):
        assert Calculadora.div(val1, val2) == pytest.approx(resultado)
    else:
        assert Calculadora.div(val1, val2) == resultado