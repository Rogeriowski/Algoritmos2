p = float(input('\nDigite o valor da aplicação: '))
i = float(input('\nDigite a taxa ( 0 - 1): '))
n = int(input('\nDigite o número de meses: '))
va = float(p * (((1 + i) ** n) -1) / i)
print(f'\nO valor acumulado: {va:.2f}')
print('\n')

