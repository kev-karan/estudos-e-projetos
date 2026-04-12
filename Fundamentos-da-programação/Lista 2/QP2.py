qtdFuncionarios = int(input('Digite a quantidade de funcionários aptos à aposentadoria: '))

nomes = []
idades = []

for i in range(qtdFuncionarios):
    while True:
        nome = input(f'Digite o nome completo do funcionário número {i+1}: ')
        idade = int(input(f'Digite a idade de {nome}: '))
        if idade >= 60:
            nomes.append(nome)
            idades.append(idade)
            break
        else:
            print('Esse funcionário não pode se aposentar ainda. Digite novamente!\n')

maisIdoso = 0
for i in range(1, len(idades)):
    if idades[i] > idades[maisIdoso]:
        maisIdoso = i

media = sum(idades) / len(idades)

print('\nFuncionários a se aposentar em 2025')
print('*' * 35)
for i in range(len(nomes)):
    print(f'Nome: {nomes[i]}\tIdade: {idades[i]} anos')

print(f'\nFuncionário mais antigo: {nomes[maisIdoso]}')
print(f'Média de idades das aposentadorias: {media:.0f} anos')
