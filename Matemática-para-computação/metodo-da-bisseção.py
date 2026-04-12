import subprocess


def bissecao(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em f(a) e f(b).")

    for i in range(max_iter):
        c = (a + b) / 2.0

        if f(c) == 0 or (b - a) / 2.0 < tol:
            return c, i + 1

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise Exception("O método não convergiu no número máximo de iterações.")


def minha_funcao(x):
    return x**3 - x - 2


def main():
    subprocess.run(["cls"], shell=True)

    print("=== Encontrador de Raízes: Método da Bisseção ===")
    print("Função atual: f(x) = x^3 - x - 2\n")

    try:
        limite_inferior = float(input("Digite o valor do limite inferior (a): "))
        limite_superior = float(input("Digite o valor do limite superior (b): "))
        tolerancia = input("Digite o critério de parada (aperte Enter para 1e-6): ")

        print("\nCalculando...")
        if tolerancia == "":
            raiz_encontrada, num_iteracoes = bissecao(
                minha_funcao, limite_inferior, limite_superior
            )
        else:
            raiz_encontrada, num_iteracoes = bissecao(
                minha_funcao, limite_inferior, limite_superior, tol=float(tolerancia)
            )

        print("-" * 30)
        print(f"Raiz encontrada: {raiz_encontrada:.5f}")
        print(f"Número de iterações: {num_iteracoes}")
        print("-" * 30)

    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("\nErro: Por favor, digite apenas números (use ponto para decimais).")
        else:
            print(f"\nErro no intervalo escolhido: {e}")
    except Exception as e:
        print(f"\nErro inesperado na execução: {e}")


main()
