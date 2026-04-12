matriz = []

colunaEscolhida = int(input('Digite o número da coluna: '))
operacao = input('Digite a operação [S] para soma ou [P] para produto: ')
print()

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um número inteiro: '))
        linha.append(valor)
    matriz.append(linha)

print()
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end='\t|\t')
    print()

if operacao == 'S':
    resultado = 0
    for i in range(3):
        resultado += matriz[i][colunaEscolhida]
    print(f'\nSoma dos números na coluna {colunaEscolhida} é: {resultado}')
elif operacao == 'P':
    resultado = 1
    for i in range(3):
        resultado *= matriz[i][colunaEscolhida]
    print(f'\nProduto dos números na coluna {colunaEscolhida} é: {resultado}')
else:
    print('\nOperação inválida!')
