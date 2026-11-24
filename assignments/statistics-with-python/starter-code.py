import numpy as np
import pandas as pd

# Carrega horas de estudo e notas de 24 alunos (turmas A e B)
df = pd.read_csv("data.csv")

scores = df["exam_score"].to_numpy()

# Tarefa 1: calcule média, mediana e desvio padrão de `scores` com NumPy.

# Tarefa 2: use describe() e groupby() do pandas para comparar as turmas A e B.

# Tarefa 3: calcule Q1, Q3, IQR e identifique os outliers de exam_score.

# Tarefa 4: calcule a correlação entre study_hours e exam_score e a reta de regressão.
