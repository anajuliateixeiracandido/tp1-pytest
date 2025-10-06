import pytest 
from CadeiaCaracteres import validar_t, validar_cc, procurar_caractere

# validar_t - partições: inteiros válidos (1-20), inteiros inválidos (<1, >20), não-inteiros
@pytest.mark.parametrize("t, esperado", [
    # inteiros válidos (1-20)
    (1, True),
    (10, True),
    (20, True),

    # inteiros inválidos (abaixo do limite)
    (0, ValueError),
    (-5, ValueError),

    # inteiros inválidos (acima do limite)
    (21, ValueError),
    (25, ValueError),
    
    # não-inteiros
    (3.14, ValueError),
    ("10", ValueError),
    (None, ValueError),
])
def test_validar_t_pe(t, esperado):
    if esperado == ValueError:
        with pytest.raises(ValueError):
            validar_t(t)
    else:
        assert validar_t(t) == esperado


# validar_cc - partições: tamanho correto, tamanho menor, tamanho maior
@pytest.mark.parametrize("cc, t, esperado", [
    # tamanho correto
    ("abc", 3, True),
    ("", 0, True),
    ("python", 6, True),
    
    # tamanho menor que t
    ("ab", 3, ValueError),
    ("", 1, ValueError),
    ("test", 5, ValueError),
    
    # tamanho maior que t
    ("abcd", 3, ValueError),
    ("python", 5, ValueError),
    ("hello", 4, ValueError),
])
def test_validar_cc_pe(cc, t, esperado):
    if esperado == ValueError:
        with pytest.raises(ValueError):
            validar_cc(cc, t)
    else:
        assert validar_cc(cc, t) == esperado


# procurar_caractere - partições: caractere válido/inválido, encontrado/não encontrado, múltiplas ocorrências
@pytest.mark.parametrize("cc, c, esperado", [
    # caractere válido (uma ocorrência)
    ("python", "p", [0]),
    ("hello", "h", [0]),
    ("abc", "c", [2]),

    # caractere válido (múltiplas ocorrencias)
    ("banana", "a", [1, 3, 5]),
    ("hello", "l", [2, 3]),
    ("ababa", "b", [1, 3]),

    # caractere válido (nenhuma ocorrencia)
    ("python", "z", []),
    ("abc", "x", []),
    ("hello", "w", []),

    # caractere inválido (string vazia)
    ("abc", "", ValueError),

    # caractere inválido (múltiplos caracteres)
    ("abc", "xy", ValueError),
    ("test", "ab", ValueError),
])
def test_procurar_caractere_pe(cc, c, esperado):
    if esperado == ValueError:
        with pytest.raises(ValueError):
            procurar_caractere(cc, c)
    else:
        assert procurar_caractere(cc, c) == esperado 