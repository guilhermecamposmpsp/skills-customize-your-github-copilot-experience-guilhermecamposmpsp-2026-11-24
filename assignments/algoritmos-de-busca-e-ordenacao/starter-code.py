# Implemente cada função e teste com listas de diferentes tamanhos.

def linear_search(values, target):
    # TODO: Percorrer a lista e retornar o índice da primeira ocorrência.
    # Retorne -1 se target não estiver em values.
    pass


def binary_search(sorted_values, target):
    # TODO: Pesquisar em uma lista já ordenada, descartando metade
    # do intervalo a cada comparação.
    # Retorne -1 se target não estiver em sorted_values.
    pass


def insertion_sort(values):
    # TODO: Criar e retornar uma nova lista ordenada com insertion sort.
    # Não altere a lista recebida.
    pass


if __name__ == "__main__":
    numbers = [8, 3, 5, 3, 9, 1]
    ordered_numbers = insertion_sort(numbers)

    print("Lista original:", numbers)
    print("Lista ordenada:", ordered_numbers)
    print("Busca linear por 5:", linear_search(numbers, 5))
    print("Busca binária por 5:", binary_search(ordered_numbers, 5))
