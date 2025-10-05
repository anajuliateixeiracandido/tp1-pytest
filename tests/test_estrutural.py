import pytest 
from CadeiaCaracteres import validar_t, validar_cc, procurar_caractere

@pytest.mark.parametrize("valor_invalido", [
    0,
    21,
    -5
])
def test_validar_t_fora_do_intervalo(valor_invalido):
    with pytest.raises(ValueError) as exc:
        validar_t(valor_invalido)
    assert str(exc.value) == "O número deve estar entre 1 e 20"

@pytest.mark.parametrize("valor_nao_int", [
    3.14, "10", None, [], {}
])
def test_validar_t_tipo_incorreto(valor_nao_int):
    with pytest.raises(ValueError) as exc:
        validar_t(valor_nao_int)
    assert str(exc.value) == "Valor não é inteiro"

@pytest.mark.parametrize("valor_limite", [1, 20])
def test_validar_t_valores_de_borda(valor_limite):
    assert validar_t(valor_limite) is True

@pytest.mark.parametrize("valor_ok", [2, 5, 17])
def test_validar_t_valores_validos_intermediarios(valor_ok):
    assert validar_t(valor_ok) is True


# ---------------------------
# TESTES ESTRUTURAIS: validar_cc
# ---------------------------

def test_validar_cc_tamanho_exato_retorna_true():
    cc = "abc"
    t = 3
    assert validar_cc(cc, t) is True

@pytest.mark.parametrize(
    "cc,t",
    [
        ("", 1),          # menor que t
        ("ab", 3),        # menor que t
        ("abcd", 3),      # maior que t
    ]
)
def test_validar_cc_tamanho_incorreto_gera_erro(cc, t):
    with pytest.raises(ValueError) as exc:
        validar_cc(cc, t)
    assert str(exc.value) == f"A cadeia deve ter exatamente {t} caracteres"

# ---------------------------
# TESTES ESTRUTURAIS: procurar_caractere
# ---------------------------

@pytest.mark.parametrize("caractere_invalido", ["", "ab"])
def test_procurar_caractere_c_invalido(caractere_invalido):
    with pytest.raises(ValueError) as exc:
        procurar_caractere("teste", caractere_invalido)
    assert str(exc.value) == "Digite apenas um caractere"

def test_procurar_caractere_um_caractere_uma_ocorrencia():
    cc = "python"
    c = "p"
    assert procurar_caractere(cc, c) == [0]

def test_procurar_caractere_multiplas_ocorrencias():
    cc = "banana"
    c = "a"
    # 0 1 2 3 4 5 -> 'a' em 1, 3 e 5
    assert procurar_caractere(cc, c) == [1, 3, 5]

def test_procurar_caractere_nenhuma_ocorrencia():
    cc = "abcde"
    c = "z"
    assert procurar_caractere(cc, c) == []
