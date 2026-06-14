class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def exibir(self):
        atual = self.cabeca

        while atual is not None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo

        print("None")

    def BuscaSequencial(self, target):
        atual = self.cabeca
        posicao = 0

        while atual is not None:
            if atual.valor == target:
                return posicao

            atual = atual.proximo
            posicao += 1

        return -1

    def meio(self, inicio, fim):
        lento = inicio
        rapido = inicio

        while rapido != fim and rapido.proximo != fim:
            rapido = rapido.proximo.proximo
            lento = lento.proximo

        return lento

    def posicao_no(self, no):
        atual = self.cabeca
        posicao = 0

        while atual is not None:
            if atual == no:
                return posicao

            atual = atual.proximo
            posicao += 1

        return -1

    def BuscaBinaria(self, target):
        inicio = self.cabeca
        fim = None

        while inicio != fim:
            meio = self.meio(inicio, fim)

            if meio.valor == target:
                return self.posicao_no(meio)

            elif meio.valor < target:
                inicio = meio.proximo

            else:
                fim = meio

        return -1

lista = LinkedList()

for valor in [50, 40, 30, 20, 10]:
    lista.inserir_no_inicio(valor)

print("Lista:")
lista.exibir()

print("\nBusca Sequencial:")
print("Posição:", lista.BuscaSequencial(30))

print("\nBusca Binária:")
print("Posição:", lista.BuscaBinaria(30))
