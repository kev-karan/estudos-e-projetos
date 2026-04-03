import subprocess

restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
    {"nome": "Pizza Superma", "categoria": "Pizza", "ativo": True},
    {"nome": "Cantina", "categoria": "Italiano", "ativo": False},
]


def exibir_nome_do_programa():
    print("Sabor Express\n")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair")


def finalizar_app():
    exibir_subtitulo("Encerrando o programa")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal ")
    main()


def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    subprocess.run(["cls"], shell=True)
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f" - {nome_restaurante} | {categoria} | {ativo}")
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (
                f"O restaurante {nome_restaurante} foi ativado com suscesso"
                if restaurante["ativo"]
                else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            )
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")
    voltar_ao_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except Exception:
        opcao_invalida()


def main():
    subprocess.run(["cls"], shell=True)
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
