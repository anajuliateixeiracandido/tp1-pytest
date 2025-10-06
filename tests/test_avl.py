import pytest
from CadeiaCaracteres import validar_t, validar_cc, procurar_caractere

# validar_t - testa os limites 1-20 e  adjacentes
@pytest.mark.parametrize("t, esperado", [
    # limite inferiores
    (0, ValueError),    
    (1, True),         
    (2, True),          

    # limite superiores
    (19, True),        
    (20, True),        
    (21, ValueError),   
])
def test_validar_t_avl(t, esperado):
    if esperado == ValueError:
        with pytest.raises(ValueError):
            validar_t(t)
    else:
        assert validar_t(t) == esperado


# validar_cc - testa tamanhos 
@pytest.mark.parametrize("cc, t, esperado", [
    # Limite inferior (t=1)
    ("", 1, ValueError),       
    ("a", 1, True),            
    ("ab", 1, ValueError),     

    # Valor médio (t=10)
    ("123456789", 10, ValueError),     
    ("1234567890", 10, True),          
    ("12345678901", 10, ValueError),  

    # Limite superior (t=20)
    ("1234567890123456789", 20, ValueError),    
    ("12345678901234567890", 20, True),          
    ("123456789012345678901", 20, ValueError),  

    ("", 0, True),             # string vazia 
])
def test_validar_cc_avl(cc, t, esperado):
    if esperado == ValueError:
        with pytest.raises(ValueError):
            validar_cc(cc, t)
    else:
        assert validar_cc(cc, t) == esperado


# procurar_caractere - testa posições limite
@pytest.mark.parametrize("cc, c, esperado", [
    # primeiro e último caractere
    ("a", "a", [0]),           # primeiro e único caractere
    ("abc", "a", [0]),         # primeiro caractere
    ("abc", "c", [2]),         # último caractere

    # String de tamanho mínimo
    ("x", "x", [0]),           # encontrado
    ("x", "y", []),            # não encontrado

    # String vazia
    ("", "a", []), 

    # Limites do tamanho do caractere de busca
    ("abc", "", ValueError),   # caractere vazio
    ("abc", "a", [0]),         # caractere válido
    ("abc", "ab", ValueError), # múltiplos caracteres
])
def test_procurar_caractere_avl(cc, c, esperado):
    if esperado == ValueError:
        with pytest.raises(ValueError):
            procurar_caractere(cc, c)
    else:
        assert procurar_caractere(cc, c) == esperado
