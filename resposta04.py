# Faça um algoritmo que peça as 4 notas bimestrais e mostre a média

nota1 = int(input(f"Digite a 1ª nota: "))
nota2 = int(input(f"Digite a 2ª nota: "))
nota3 = int(input(f"Digite a 3ª nota: "))
nota4 = int(input(f"Digite a 4ª nota: "))
media = float((nota1 + nota2 + nota3 + nota4)/4)
print("média = %.2f" %(media))