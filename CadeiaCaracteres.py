def validar_t(t):
    if not isinstance(t, int):
        raise ValueError("Valor não é inteiro")
    if not (1 <= t <= 20):
        raise ValueError("O número deve estar entre 1 e 20")
    return True

def validar_cc(cc, t):
    if len(cc) != t:
        raise ValueError(f"A cadeia deve ter exatamente {t} caracteres")
    return True

def procurar_caractere(cc, c):
    if len(c) != 1:
        raise ValueError("Digite apenas um caractere")
    posicoes = [i for i, ch in enumerate(cc) if ch == c]
    return posicoes