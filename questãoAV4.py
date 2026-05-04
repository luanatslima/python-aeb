#import math
#def calcula_vertice(a, b, c):
 #   delta = (b ** 2) - 4 * a * c
  #  xv = -b / (2 * a)
   # yv = -delta / (4 * a)
    #resultado = (math.floor(xv), math.floor(yv))
    #return resultado
#valores = calcula_vertice(-34453, 4234654, 44575)
#print(valores)

def fibonacci(n):
    if (n == 1):
        return 1
    if (n == 0):
        return 0
    return fibonacci(n - 2) + fibonacci(n - 1)

n = 27
soma = 0

# O range(n + 1) garante que ele vá de 0 até 27
for i in range(n + 1):
    soma += fibonacci(i)

print(soma)
