# Faça um algoritmo que peça a temperatura em graus Celsius, transforme
# e mostre em graus Farenheit.
temperatura_celsius = float(input('Digite a temperatura em Celsius: '))

temperatura_farenheit = (temperatura_celsius + 160)/5
print('A temperatura equivalente em graus Farenheit é %.2f' %(temperatura_farenheit))


temperatura_farenheit = (temperatura_celsius * 9/5) + 32
print('A temperatura equivalente em graus Farenheit é %.2f' %(temperatura_farenheit))