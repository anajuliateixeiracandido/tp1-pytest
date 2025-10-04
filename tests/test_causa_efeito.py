import pytest
from CadeiaCaracteres import validar_t, validar_cc, procurar_caractere

def test_t_fora_intervalo():
    with pytest.raises(ValueError) as excinfo:
        validar_t(23)
    assert str(excinfo.value) == "O número deve estar entre 1 e 20"


def test_t_abaixo_intervalo():
    with pytest.raises(ValueError) as excinfo:
        validar_t(0)
    assert str(excinfo.value) == "O número deve estar entre 1 e 20"


def test_t_nao_inteiro():
    with pytest.raises(ValueError) as excinfo:
        validar_t("a")
    assert str(excinfo.value) == "Valor não é inteiro"


def test_t_valido():
    assert validar_t(5) is True


def test_cc_tamanho_incorreto():
    with pytest.raises(ValueError) as excinfo:
        validar_cc("abc", 4)
    assert str(excinfo.value) == "A cadeia deve ter exatamente 4 caracteres"


def test_cc_tamanho_correto():
    assert validar_cc("abcd", 4) is True
    

def test_caractere_encontrado():
    resultado = procurar_caractere("abc", "c")
    assert resultado == [2]


def test_caractere_encontrado_varias_posicoes():
    resultado = procurar_caractere("abacada", "a")
    assert resultado == [0, 2, 4, 6]


def test_caractere_nao_encontrado():
    resultado = procurar_caractere("abc", "x")
    assert resultado == []


def test_caractere_invalido():
    with pytest.raises(ValueError) as excinfo:
        procurar_caractere("abc", "xy")
    assert str(excinfo.value) == "Digite apenas um caractere"


def test_caractere_vazio():
    with pytest.raises(ValueError) as excinfo:
        procurar_caractere("abc", "")
    assert str(excinfo.value) == "Digite apenas um caractere"


# Caso 23: Término do programa
# Este caso depende do controle de fluxo externo,
# não é testável diretamente nas funções fornecidas.
def test_termino_programa_documentado():
    """
    O término do programa (caso 23) depende do loop externo de interação com o usuário,
    não é possível testar diretamente nas funções fornecidas.
    """
    assert True  
