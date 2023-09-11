import math as m
base = float(input("\nDigite a base: "))
altura = float(input("\nDigite a altura: "))
perimetro = 2*(base + altura)
area = base * altura
diagonal = m.sqrt(base**2 + altura**2)
print("\nPerimetro: ", perimetro)
print("\nArea: ", area)
print("\nDiagonal: ", diagonal)
print("\n")


