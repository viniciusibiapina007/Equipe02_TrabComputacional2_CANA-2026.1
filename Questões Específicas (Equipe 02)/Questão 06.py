class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def push(self, valor):
        novo_no = No(valor)

        if self.cabeca is None:
            self.cabeca = novo_no
            return

        atual = self.cabeca

        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo_no

    def mostrar(self):
        elementos = []

        atual = self.cabeca

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos


def selectionSortEncadeado(lista):
    atual = lista.cabeca

    while atual is not None:
        menorNo = atual

        buscador = atual.proximo

        while buscador is not None:
            if buscador.valor < menorNo.valor:
                menorNo = buscador

            buscador = buscador.proximo

        atual.valor, menorNo.valor = menorNo.valor, atual.valor

        atual = atual.proximo

    return lista


lista_desorganizada = ListaEncadeada()

elementos = [-1, -90, 58, -2, 4, 10, 5]

for elemento in elementos:
    lista_desorganizada.push(elemento)

print(f"Lista Original: {lista_desorganizada.mostrar()}")

selectionSortEncadeado(lista_desorganizada)

print(f"Lista Organizada: {lista_desorganizada.mostrar()}")
