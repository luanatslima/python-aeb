# INTRODUÇÃO À LINGUAGEM PYTHON

#nome = input ("Digite o seu nome: ")

#print("\n---------- Assistente Pessoal (Versão 1.0) ----------", end="\n\n")
#print(f"[INFO] Olá {nome}, como vai?")
#print("[INFO] Me chamo Hebert, como posso ajudar")

# # # # # # # # # # # # # # # 

import math

raio_base = int(input("Digite o valor do raio: "))
h_cilindro = int(input("Digite o valor da altura do cilindro: "))

# Fórmula simplificada fornecida no enunciado: 2 * pi * r * (h + r)
area_total = 2 * math.pi * raio_base * (h_cilindro + raio_base)

# Usamos int() para pegar apenas a parte inteira conforme solicitado
print(int(area_total))
