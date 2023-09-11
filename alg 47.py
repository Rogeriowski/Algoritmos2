num = int(input("\n Digite um número com 3 dígitos: "))
c = num // 100
d = num % 100 // 10
u = num % 10
num1 = u*100 + d*10 + c
print("\nNúmero: ", num)
print("\nO número invertido é: ", num1)
print("\n")



