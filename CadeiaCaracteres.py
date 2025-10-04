while True:
    try:
        T = int(input("Digite um inteiro positivo entre 1 e 20: "))
        if 1 <= T <= 20:
            break
        else:
            print("O número deve estar entre 1 e 20.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

while True:
    CC = input(f"Digite uma cadeia de caracteres com {T} caracteres: ")
    if len(CC) == T:
        break
    else:
        print(f"A cadeia deve ter exatamente {T} caracteres.")

while True:
    C = input("Digite o caractere a ser procurado: ")
    if len(C) == 1:
        posicoes = [i for i, ch in enumerate(CC) if ch == C]
        if posicoes:
            print(f"O caractere '{C}' aparece nas posições: {posicoes}")
        else:
            print(f"O caractere '{C}' não foi encontrado na cadeia.")
    else:
        print("Digite apenas um caractere.")

    O = input("Deseja procurar outro caractere? (s/n): ").lower()
    if O != 's':
        break

print("Programa encerrado.")