class No:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def exibir(self, no=None, nivel=0):
        if no is None:
            no = self.raiz

        print("   " * nivel + str(no.valor))

        for filho in no.filhos:
            self.exibir(filho, nivel + 1)

# Nós
A = No("A")
B = No("B")
C = No("C")
D = No("D")
E = No("E")
F = No("F")
G = No("G")
H = No("H")
I = No("I")
J = No("J")
K = No("K")
L = No("L")
M = No("M")
N = No("N")

# Ligações
A.adicionar_filho(B)
A.adicionar_filho(C)
A.adicionar_filho(D)

B.adicionar_filho(E)
E.adicionar_filho(I)

C.adicionar_filho(F)
C.adicionar_filho(G)

F.adicionar_filho(J)

G.adicionar_filho(K)
G.adicionar_filho(L)

D.adicionar_filho(H)

H.adicionar_filho(M)
M.adicionar_filho(N)

# Árvore
arvore = Arvore(A)

# Exibição
arvore.exibir()
