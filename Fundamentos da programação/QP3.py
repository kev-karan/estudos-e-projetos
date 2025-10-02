somaSalarios = 0
somaDiagonal = 0

matriz = [[0,0,0], [0,0,0], [0,0,0]]

profissoes = ['Desenvolvedor Python', 'Cientista de Dados', 'Analista de QA']

for i in range(3):
    print('\nCadastro da profissão:', profissoes[i])
    matriz[i][0] = float(input('Digite o salário médio: '))
    matriz[i][1] = int(input('Digite o tempo mínimo de experiência (anos): '))
    matriz[i][2] = float(input('Digite o valor da hora de trabalho: '))

print('\nSalário médio | tempo mínimo de experiência | valor da hora de trabalho:')
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]}\t|\t', end='')
    print()

for i in range(3):
    somaSalarios += matriz[i][0]

mediaSalarios = somaSalarios / 3

for i in range(3):
    somaDiagonal += matriz[i][i]

print(f'\nA média salarial das três profissões: {mediaSalarios:.2f}')
print(f'A soma dos valores da diagonal principal: {somaDiagonal:.2f}')
