# Faça um algoritmo que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês

hora = float(input('Qual o vallor da sua hora trabalhada? '))
quantidade_horas = int(input('Quantas horas vc trabalha no mês? '))
salario = hora * quantidade_horas
print("Valaor do salário = %.2f" %(salario))