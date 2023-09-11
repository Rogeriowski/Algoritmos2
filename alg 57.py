pr1 = float(input("\nDigite a nota da primeira prova: "))
pr2 = float(input("\nDigite a nota da segunda prova: "))
mf = (pr1 + pr2)/2
print("\nMedia truncada é: ", float(int((mf - 0.5) + 0.001)))
print("\nMedia arredondada é: ", float(int(mf + 0.001)))
print("\n")



