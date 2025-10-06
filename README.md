# tp1-pytest

# 1. Descrição do Framework (Pytest)

## 1.1 O que é o Pytest?

O **Pytest** é um framework de testes para **Python**, escolhemos utiliza-lo devido à sua simplicidade, flexibilidade e poder.
Ele permite escrever casos de teste de forma intuitiva, além de suportar **testes unitários, de integração e funcionais**. Sua sintaxe enxuta facilita a escrita e manutenção dos testes.

No nosso projeto, as funções principais geram exceções (`raise ValueError`) quando recebem dados inválidos, como valores fora do intervalo ou tipos errados. Com isso é possível identificar a causa do erro. Nos testes, usamos o **Pytest** para verificar se essas exceções realmente acontecem quando esperado. Assim, garantimos que o sistema está tratando erros corretamente.

---

## 1.2 Instalação e Integração

A instalação do Pytest é simples e pode ser feita via **pip**:

```bash
pip install pytest
```

Para integrar ao projeto, basta criar arquivos de teste com o prefixo `test_` e funções de teste também iniciando com `test_`.
Para executar os testes, utilize:

```bash
pytest
```

O Pytest irá automaticamente identificar e executar todos os testes presentes no projeto.

---

# 2. Categorização do Framework

### i) Técnicas de Teste

O **Pytest** suporta tanto técnicas de teste **caixa-preta** (focando em entradas e saídas) quanto **caixa-branca** (verificando o funcionamento interno do código).

### ii) Níveis de Teste

**Teste Unitário:** testa funções/métodos isoladamente.

### iii) Tipos de Teste

**Teste Funcional:** verifica se o sistema atende aos requisitos especificados.

---

# 3. Nosso Problema

Considere um programa que solicita do usuário um inteiro positivo no intervalo entre **1 e 20** e então solicita uma cadeia de caracteres desse comprimento.
Após isso, o programa solicita um caractere e retorna a posição em que o caractere está presente na cadeia.
O usuário tem a opção de procurar vários caracteres.

---

# 4. Estratégias de Teste

---

## 4.1 Partição de Equivalência

### 4.1.1 O que é?

A **Partição de Equivalência** é uma técnica de teste de caixa-preta que divide o domínio de entrada em **classes de equivalência**, onde todos os elementos de uma mesma classe devem produzir comportamentos similares no sistema. O objetivo é reduzir o número de casos de teste necessários, escolhendo **representantes** de cada partição.

### 4.1.2 Partições Identificadas

Para nosso problema, identificamos as seguintes partições:

#### **validar_t(t) - Validação do Tamanho**

**Partições:**
- **Inteiros válidos (1-20)**: valores dentro do intervalo permitido
- **Inteiros inválidos (<1)**: valores abaixo do limite inferior  
- **Inteiros inválidos (>20)**: valores acima do limite superior
- **Não-inteiros**: tipos diferentes de int (float, string, None)

#### **validar_cc(cc, t) - Validação da Cadeia**

**Partições:**
- **Tamanho correto**: cadeia com comprimento exatamente igual a `t`
- **Tamanho menor**: cadeia com comprimento menor que `t`
- **Tamanho maior**: cadeia com comprimento maior que `t`

#### **procurar_caractere(cc, c) - Busca de Caractere**

**Partições:**
- **Caractere válido - uma ocorrência**: encontra o caractere uma vez
- **Caractere válido - múltiplas ocorrências**: encontra o caractere várias vezes
- **Caractere válido - nenhuma ocorrência**: não encontra o caractere na cadeia
- **Caractere inválido - string vazia**: entrada com ""
- **Caractere inválido - múltiplos caracteres**: entrada com mais de 1 caractere

### 4.1.3 Casos de Teste Implementados

| T  | CC      | C  | Tamanho Esperado | Saída Esperada                                    |
| -- | ------- | -- | ---------------- | ------------------------------------------------- |
| 1  | -       | -  | -                | True                                              |
| 10 | -       | -  | -                | True                                              |
| 20 | -       | -  | -                | True                                              |
| 0  | -       | -  | -                | O número deve estar entre 1 e 20                 |
| -5 | -       | -  | -                | O número deve estar entre 1 e 20                 |
| 21 | -       | -  | -                | O número deve estar entre 1 e 20                 |
| 25 | -       | -  | -                | O número deve estar entre 1 e 20                 |
| 3.14 | -     | -  | -                | Valor não é inteiro                               |
| "10" | -     | -  | -                | Valor não é inteiro                               |
| None | -     | -  | -                | Valor não é inteiro                               |
| 3  | abc     | -  | 3                | True                                              |
| 0  | ""      | -  | 0                | True                                              |
| 6  | python  | -  | 6                | True                                              |
| 3  | ab      | -  | 3                | A cadeia deve ter exatamente 3 caracteres        |
| 1  | ""      | -  | 1                | A cadeia deve ter exatamente 1 caracteres        |
| 5  | test    | -  | 5                | A cadeia deve ter exatamente 5 caracteres        |
| 3  | abcd    | -  | 3                | A cadeia deve ter exatamente 3 caracteres        |
| 5  | python  | -  | 5                | A cadeia deve ter exatamente 5 caracteres        |
| 4  | hello   | -  | 4                | A cadeia deve ter exatamente 4 caracteres        |
| -  | python  | p  | -                | [0]                                               |
| -  | hello   | h  | -                | [0]                                               |
| -  | abc     | c  | -                | [2]                                               |
| -  | banana  | a  | -                | [1, 3, 5]                                        |
| -  | hello   | l  | -                | [2, 3]                                           |
| -  | ababa   | b  | -                | [1, 3]                                           |
| -  | python  | z  | -                | []                                                |
| -  | abc     | x  | -                | []                                                |
| -  | hello   | w  | -                | []                                                |
| -  | abc     | "" | -                | Digite apenas um caractere                        |
| -  | abc     | xy | -                | Digite apenas um caractere                        |
| -  | test    | ab | -                | Digite apenas um caractere                        |
---

#### Legenda:

* **T** = Valor de entrada para o tamanho/campo numérico
* **CC** = Cadeia de caracteres
* **C** = Caractere procurado
* **Tamanho Esperado** = Parâmetro para validar o tamanho da cadeia (quando aplicável)
* **Saída Esperada** = Resultado ou mensagem de erro esperada

---

## 4.2 Análise de Valor Limite (AVL)


---

## 4.3 Grafo de Causa e Efeito

### 4.3.1 O que é?

O **Grafo de Causa e Efeito** é uma técnica formal de derivação de casos de teste baseada em **lógica booleana**.
Ela modela as relações entre **entradas (causas)** e **saídas (efeitos)** do sistema, permitindo identificar combinações relevantes para teste.
A partir desse grafo, é possível construir **tabelas de decisão** que orientam a criação dos casos de teste.

---

<img width="471" height="226" alt="Captura de Tela 2025-10-04 às 21 49 59" src="https://github.com/user-attachments/assets/c4079e81-90b7-4059-9819-0ace9f206fe8" />

### 4.3.2 Causas e Efeitos

**Causas:**

* Inteiro positivo no intervalo de 1 a 20
* Caractere a ser procurado na cadeia
* Procurar outro caractere

**Efeitos:**

* **20.** Inteiro fora do intervalo
* **21.** Posição do caractere na cadeia
* **22.** Caractere não encontrado
* **23.** Término do programa

---

### 4.3.3 Tabela de Decisão (Grafo Causa-Efeito)

|    |   |   |   |   |
| -- | - | - | - | - |
| 1  | 0 | 1 | 1 | - |
| 2  | - | 1 | 0 | - |
| 3  | - | 1 | 1 | 0 |
| 20 | 1 | 0 | 0 | 0 |
| 21 | 0 | 1 | 0 | 0 |
| 22 | 0 | 0 | 1 | 0 |
| 23 | 0 | 0 | 0 | 1 |

---

### 4.3.4 Casos de Teste Derivados

| T  | CC      | C  | Tamanho Esperado | Saída Esperada                                    |
| -- | ------- | -- | ---------------- | ------------------------------------------------- |
| 23 | -       | -  | -                | O número deve estar entre 1 e 20                  |
| 0  | -       | -  | -                | O número deve estar entre 1 e 20                  |
| a  | -       | -  | -                | Valor não é inteiro                               |
| 5  | -       | -  | -                | True                                              |
| 4  | abc     | -  | 4                | A cadeia deve ter exatamente 4 caracteres         |
| 4  | abcd    | -  | 4                | True                                              |
| -  | abc     | c  | -                | [2]                                               |
| -  | abacada | a  | -                | [0, 2, 4, 6]                                      |
| -  | abc     | x  | -                | []                                                |
| -  | abc     | xy | -                | Digite apenas um caractere                        |
| -  | abc     | -  | -                | Digite apenas um caractere                        |
| -  | -       | -  | -                | *(Término do programa, não testável diretamente)* |

---

#### Legenda:

* **T** = Valor de entrada para o tamanho/campo numérico
* **CC** = Cadeia de caracteres
* **C** = Caractere procurado
* **Tamanho Esperado** = Parâmetro para validar o tamanho da cadeia (quando aplicável)
* **Saída Esperada** = Resultado ou mensagem de erro esperada

---

Cada linha da tabela acima foi um teste implementado no código apresentado, cobrindo as principais possibilidades de entradas e suas respectivas saídas, conforme a modelagem do grafo de causa e efeito.

O caso de término do programa (**23**) depende do controle de fluxo externo, **não sendo testável diretamente** nas funções fornecidas, mas está documentado para fins de cobertura da modelagem.

Os testes implementados cobrem **validação de entrada, tamanho da cadeia, busca de caracteres, casos de erro e sucesso**, conforme a estratégia formal definida.

---

## 4.4 Teste Estrutural
