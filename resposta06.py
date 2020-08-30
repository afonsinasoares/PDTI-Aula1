#Faça um algoritmo que peça o raio de um círculo, calcule e mostre sua área
# A = pi * (r * r)
import math

raio = int(input('Digite o valor do raio de císculo: '))
area = math.pi * raio ** 2
print("Área do circúlo = %.2f" %(area))
