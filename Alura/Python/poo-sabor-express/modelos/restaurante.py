class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    def listar_restaurantes():
        print(
            f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}"
        )
        for restarante in Restaurante.restaurantes:
            print(
                f"{restarante.nome.ljust(25)} | {restarante.categoria.ljust(25)} | {restarante.ativo}"
            )

    @property
    def ativo(self):
        return "⌧" if self._ativo else "☐"


restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_pizza = Restaurante("pizza Express", "Italiana")

Restaurante.listar_restaurantes()
