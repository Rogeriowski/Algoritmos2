vha = float(input("\nEntre com o valor da hora aula: "))
na = int(input("\nEntre com o numero de aulas dadas: "))
pdinss = float(input("\nEntre com o percentual de desconto do INSS: "))
sb = na * vha
td = (pdinss / 100) * sb
sl = sb - td
print("\nSalário líquido é: ", sl)
print("\n")


