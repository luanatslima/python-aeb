#estudante = {"nome": "Joana", "idade": 20, "nota1": 10, "nota2": 6}

#estudante["curso"] = "Algoritmos em Python"
#estudante["idade"] = 21

#media = int((estudante["nota1"] + estudante["nota2"]) / 2)
#estudante["media"] = media

#print(estudante)

#################################################################################

#import math
#import random

# Aqui está a lista de preços
#precos = [2.50, 5.99, 1.20, 10.00, 4.35, random.uniform(0.1, 5.0)]

# Aqui está a variável que armazenará a soma dos preços
#total = 0

# TODO Escreva o seu laço de repetição para percorrer a lista e obter a soma dos preços.
# TODO Após isso, calcule e imprima a média aritmética dos preços.

#for preco in precos:
#    total += preco

#media = math.floor(total / len(precos))
#print(media)

##################################################################################

#frase = input("Digite uma frase: ")

#frase = frase[::-1]
#print(frase)

###################################################################################

palavra = input("Digite uma palavra: ").lower()

contagem = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1

print(contagem)