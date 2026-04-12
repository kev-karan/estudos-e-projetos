qtdMouse = int(input('Digite a quantidade de mouses: '))

defeitos = []

esfera = 0
limpeza = 0
cabo = 0
quebrado = 0

print('\nDigite o defeito de cada mouse:')
print('1 - necessita da esfera')
print('2 - necessita de limpeza')
print('3 - necessita troca do cabo ou conector')
print('4 - quebrado ou inutilizado')

for i in range(qtdMouse):
    while True:
        defeito = int(input(f'Mouse {i+1}: '))
        if defeito in [1, 2, 3, 4]:
            defeitos.append(defeito)
            if defeito == 1:
                esfera += 1
            elif defeito == 2:
                limpeza += 1
            elif defeito == 3:
                cabo += 1
            elif defeito == 4:
                quebrado += 1
            break
        else:
            print('Opção inválida, tente novamente!')

print(f'\nQuantidade de mouses: {qtdMouse}')
print('\nSituação\t\t\tQuantidade\t\tPercentual')
print(f'1- necessita da esfera\t\t\t{esfera}\t\t       {(esfera/qtdMouse)*100:.0f}%')
print(f'2- necessita de limpeza\t\t\t{limpeza}\t\t       {(limpeza/qtdMouse)*100:.0f}%')
print(f'3- necessita troca do cabo ou conector  {cabo}\t\t       {(cabo/qtdMouse)*100:.0f}%')
print(f'4- quebrado ou inutilizado\t\t{quebrado}\t\t       {(quebrado/qtdMouse)*100:.0f}%')
