"""Funções de ordenação implementadas para a disciplina de Projeto e Análise de Algoritmos."""


def insertionSort(arr):
    """Ordena uma lista em ordem crescente usando o algoritmo Insertion Sort.

    A cada iteração, o elemento atual (chave) é inserido na posição correta
    dentro do prefixo já ordenado da lista, deslocando para a direita os
    elementos maiores que ele.

    A ordenação é feita in-place (a própria lista é modificada) e é estável
    (elementos iguais mantêm a ordem relativa original).

    Complexidade de tempo:
        - Melhor caso: O(n)   -> lista já ordenada; cada elemento é comparado
          apenas uma vez com o anterior e nenhum deslocamento é feito.
        - Caso médio:  O(n²)  -> em média, cada elemento é deslocado por metade
          do prefixo ordenado (~n²/4 comparações/deslocamentos).
        - Pior caso:   O(n²)  -> lista em ordem decrescente; cada elemento é
          deslocado por todo o prefixo ordenado (~n²/2 comparações/deslocamentos).

    Uso de memória:
        - O(1) de espaço auxiliar, pois ordena in-place usando apenas algumas
          variáveis extras (chave e índices).

    Args:
        arr (list): Lista de elementos comparáveis a ser ordenada.

    Returns:
        list: A mesma lista recebida, agora ordenada em ordem crescente.
    """
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        # Desloca para a direita os elementos maiores que a chave
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr


if __name__ == "__main__":
    exemplo = [5, 2, 9, 1, 5, 6]
    print(insertionSort(exemplo))  # [1, 2, 5, 5, 6, 9]
