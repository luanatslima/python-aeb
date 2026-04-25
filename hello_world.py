# PRIMEIRO PROGRAMA
# String e Variáveis! 

print("Hello World!")   
print("Esse é apenas um entre os meus vários programas em Python!")

n_1 = 9
n_2 = 7

soma = n_1 + n_2

print(n_1)
print(n_2)

print(f"A soma dos valores é: {soma}")

# Entrada de Dados
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
idade = int(idade) # Convertendo a idade para inteiro
print(f"Olá {nome}, você tem {idade} anos!")

facul_anos = 5
facul_idade = idade + facul_anos
print(f"Quando você concluir a faculdade terá {facul_idade} anos!")


# Quebra de linha
print("Olá, tudo bem? \nSeja bem-vindo ao mundo da programação!")

print("""
    frase 1
    frase 2
    frase 3
    """
)

# Converter string para inteiro ou float
numero = "10"
numero = int(numero) # Convertendo para inteiro

pi = "3.14"
pi = float(pi) # Convertendo para float

print(f"numero: {numero}")
print(f"pi: {pi}")

# Operadores Aritméticos e módulo math (conjunto de funções e valores constantes 
    # que podemos importar para realizar operações matemáticas)
# Exemplos de operadores aritméticos:
#   +, -, *, /, // (divisão inteira), % (módulo), ** (exponenciação)
# Exemplos de Módulo math: 
#   (math.sqrt(), math.pow(), math.pi, etc.)

import math

