# 📘 Atividade: Algoritmos de Busca e Ordenação em Python

## 🎯 Objetivo

Implemente algoritmos para localizar e ordenar valores em listas. Compare a busca linear com a busca binária e observe como a organização dos dados afeta a quantidade de comparações.

## 📝 Tarefas

### 🛠️ Implementar uma Busca Linear

#### Descrição
Complete `linear_search(values, target)` para percorrer uma lista e localizar o valor procurado.

#### Requisitos
O programa concluído deve:

- Retornar o índice da primeira ocorrência de `target`
- Retornar `-1` quando o valor não estiver na lista
- Funcionar com listas vazias e com valores repetidos


### 🛠️ Implementar uma Busca Binária

#### Descrição
Complete `binary_search(sorted_values, target)` usando a estratégia de dividir pela metade o intervalo de busca. A lista recebida já estará ordenada.

#### Requisitos
O programa concluído deve:

- Retornar o índice de `target` ou `-1` se ele não estiver na lista
- Atualizar os limites da busca a cada comparação para descartar metade do intervalo
- Encontrar valores no início, no meio e no fim, além de tratar uma lista vazia


### 🛠️ Ordenar Valores com Insertion Sort

#### Descrição
Complete `insertion_sort(values)` para ordenar os valores em ordem crescente usando o algoritmo insertion sort. Em seguida, use o resultado para fazer uma busca binária.

#### Requisitos
O programa concluído deve:

- Retornar uma nova lista ordenada sem alterar a lista original
- Ordenar corretamente listas vazias, listas com um elemento e listas com valores repetidos
- Demonstrar que `binary_search` localiza um valor na lista ordenada e retorna `-1` para um valor ausente
