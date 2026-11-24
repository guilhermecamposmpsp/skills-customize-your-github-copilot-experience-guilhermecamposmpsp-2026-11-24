
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo de adivinhar palavras usando strings, loops, condicionais, seleção aleatória e entrada de dados do usuário em Python. Ao final desta atividade, você terá um programa interativo completo, do início ao fim.

## 📝 Tarefas

### 🛠️ Seleção da Palavra Secreta e Estado do Jogo

#### Descrição
Escolha aleatoriamente uma palavra da lista predefinida e prepare as variáveis que vão acompanhar o andamento da partida: letras já tentadas, erros cometidos e o limite de tentativas.

#### Requisitos
O programa concluído deve:

- Selecionar palavras aleatoriamente de uma lista predefinida
- Inicializar as variáveis de estado do jogo (letras adivinhadas, tentativas incorretas e máximo de erros permitidos)

### 🛠️ Loop Principal e Palpites

#### Descrição
Crie o loop principal do jogo, em que o jogador digita letras e recebe um retorno sobre o progresso a cada rodada.

#### Requisitos
O programa concluído deve:

- Exibir o progresso atual da palavra no formato `_ _ _`, revelando as letras já acertadas
- Aceitar palpites de letras do usuário
- Verificar cada palpite e atualizar o estado do jogo (letra correta ou tentativa incorreta)
- Rastrear as tentativas incorretas restantes

### 🛠️ Encerramento e Mensagens de Vitória ou Derrota

#### Descrição
Finalize o jogo quando a palavra for descoberta ou as tentativas acabarem, exibindo a mensagem adequada para o jogador.

#### Requisitos
O programa concluído deve:

- Encerrar o jogo quando a palavra for adivinhada
- Encerrar o jogo quando as tentativas se esgotarem
- Exibir mensagens de vitória ou derrota ao final da partida (na derrota, mostrar a palavra secreta)