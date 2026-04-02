import os


def exibir_nome_do_programa():
    print("Sabor Express\n")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair")


def opcao_invalida():
    print("Opção inválida!\n")
    input("Digite uma tecla para voltar ao menu principal")
    main()


def finalizar_app():
    os.system("cls")
    print("Encerrando o programa\n")


def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                print("Cadastrar restaurante")
            case 2:
                print("Listar restaurantes")
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except Exception:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
