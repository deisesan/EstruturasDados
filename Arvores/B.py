class No:
    def __init__(self, tam, eh_folha=True):
        # Grau mínimo (tamanho mínimo permitido das chaves)
        self.tam = tam
        # Lista de chaves
        self.chaves = []
        # Lista de ponteiros para os filhos
        self.filhos = []
        # True se o nó for folha
        self.eh_folha = eh_folha

class ArvoreB: 
    def __init__(self, tam):
        self.raiz = No(tam)
        self.tam = tam

    def inserir(self, chave):
        raiz = self.raiz
        # Se a raiz estiver cheia
        if len(raiz.chaves) == 2 * self.tam - 1:
            nova_raiz = No(self.tam, eh_folha=False)
            nova_raiz.filhos.append(self.raiz)
            self.dividir_no_filho(nova_raiz, 0)
            self.raiz = nova_raiz
            self.inserir_no_nao_cheio(self.raiz, chave)
        else:
            self.inserir_no_nao_cheio(raiz, chave)

    def inserir_no_nao_cheio(self, no, chave):
        i = len(no.chaves) - 1
        if no.eh_folha:
            no.chaves.append(None)  # Expande a lista de chaves
            while i >= 0 and chave < no.chaves[i]:
                no.chaves[i + 1] = no.chaves[i]
                i -= 1
            no.chaves[i + 1] = chave
        else:
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            if len(no.filhos[i].chaves) == 2 * self.tam - 1:
                self.dividir_no_filho(no, i)
                if chave > no.chaves[i]:
                    i += 1
            self.inserir_no_nao_cheio(no.filhos[i], chave)

    def dividir_no_filho(self, pai, i):
        tam = self.tam
        filho = pai.filhos[i]
        novo_filho = No(tam, eh_folha = filho.eh_folha)
        # Promove a chave do meio
        pai.chaves.insert(i, filho.chaves[tam - 1])
        pai.filhos.insert(i + 1, novo_filho)
        # Divide as chaves e filhos
        novo_filho.chaves = filho.chaves[tam:]
        filho.chaves = filho.chaves[:tam - 1]
        if not filho.eh_folha:
            novo_filho.filhos = filho.filhos[tam:]
            filho.filhos = filho.filhos[:tam]

    def busca(self, no, chave):
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
        # Chave encontrada
        if i < len(no.chaves) and chave == no.chaves[i]:
            return (no, i)
        # Não encontrado
        elif no.eh_folha:
            return None
        else:
            return self.busca(no.filhos[i], chave)
        
    def visualizar_arvore(self, no):
        if no is not None:
            # Exibe a chave do nó atual
            print(f"[{' '.join(map(str, no.chaves))}]", end=" ")
            # Se o nó não for folha, exibe os filhos na mesma linha
            if not no.eh_folha:
                # Adiciona uma nova linha após a chave do nó
                print()  
                for i, filho in enumerate(no.filhos):
                    self.visualizar_arvore(filho)
                # Adiciona uma nova linha após todos os filhos
                print() 

if __name__ == '__main__':
    arvore_b = ArvoreB(2)
    arvore_b.inserir(10)
    arvore_b.inserir(20)
    arvore_b.inserir(5)
    arvore_b.inserir(6)
    arvore_b.inserir(12)
    arvore_b.inserir(30)
    arvore_b.inserir(7)
    arvore_b.inserir(8)

    print("Estrutura da Árvore B:")
    arvore_b.visualizar_arvore(arvore_b.raiz)  
