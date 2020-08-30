# Faça um algoritmo que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)

temperatura_farenheit = float(input('Digite a temperatura em Farenheit: '))
temperatura_celsius = 5 * ((temperatura_farenheit - 32) / 9)

print('A temperatura equivalente em graus Celsius é %.2f' %(temperatura_celsius))