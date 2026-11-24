# 📘 Atividade: Estatística com Python

## 🎯 Objetivo

Aprenda a calcular medidas estatísticas com Python, usando **numpy** para cálculos sobre arrays e **pandas** para analisar tabelas. Você vai calcular medidas de tendência central e dispersão, comparar grupos, identificar outliers e medir a relação entre duas variáveis.

O conjunto de dados (`data.csv`) traz as horas de estudo e as notas de 24 alunos de duas turmas (`A` e `B`).

## 📝 Tarefas

### 🛠️ Medidas de Tendência Central com NumPy

#### Descrição
Calcule a média, a mediana e o desvio padrão das notas usando funções do numpy. Depois, veja como um único valor muito baixo afeta cada uma dessas medidas.

#### Requisitos
O programa completo deve:

- Converter a coluna `exam_score` para um array com `to_numpy()`
- Calcular `np.mean`, `np.median` e `np.std` sobre as notas e imprimir os três valores com 2 casas decimais
- Remover a nota mais baixa com uma máscara booleana (ex.: `scores[scores > scores.min()]`)
- Imprimir a média e a mediana antes e depois da remoção e identificar qual delas mudou mais


### 🛠️ Comparar Turmas com Pandas

#### Descrição
Use o pandas para resumir o conjunto de dados e comparar o desempenho das turmas `A` e `B`.

#### Requisitos
O programa completo deve:

- Imprimir o resultado de `df.describe()` e entender o significado de cada linha (`count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, `max`)
- Usar `groupby("class")` para calcular média, mediana e desvio padrão de `exam_score` por turma
- Imprimir o número de alunos de cada turma com `value_counts()`
- Dizer, em um `print`, qual turma teve a maior média


### 🛠️ Quartis e Outliers

#### Descrição
Identifique notas atípicas usando a regra do intervalo interquartil (IQR). Um valor é considerado outlier quando está abaixo de `Q1 - 1.5 × IQR` ou acima de `Q3 + 1.5 × IQR`.

#### Requisitos
O programa completo deve:

- Calcular os quartis `Q1` e `Q3` de `exam_score` com `quantile(0.25)` e `quantile(0.75)`
- Calcular o `IQR` (`Q3 - Q1`) e os limites inferior e superior
- Filtrar com máscara booleana os alunos cuja nota está fora dos limites
- Imprimir o `student_id`, a turma e a nota de cada outlier encontrado


### 🛠️ Correlação e Reta de Regressão

#### Descrição
Este é o desafio final. Meça a relação entre horas de estudo e nota, e ajuste uma reta que estime a nota a partir das horas estudadas.

#### Requisitos
O programa completo deve:

- Calcular a correlação de Pearson entre `study_hours` e `exam_score` com `corr()`
- Ajustar uma reta com `np.polyfit(study_hours, exam_score, 1)` e imprimir a inclinação e o intercepto
- Estimar a nota de um aluno que estude 5 horas, usando a reta encontrada
- Repetir o cálculo da correlação sem o outlier identificado na tarefa anterior e comentar, no código, se a correlação ficou mais forte ou mais fraca
