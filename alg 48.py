sm = float(input("\nEntre com um salário mínimo: "))
qtd = float(input("\nEntre com quantidade em quilowatt: "))
preco = sm / 700
vp = preco * qtd
vd = vp * 0.9
print("\nPreço do quilowatt: ", preco, "\nvalor a ser pago: ", vp, "\nvalor com desconto: ", vd)
print("\n")


