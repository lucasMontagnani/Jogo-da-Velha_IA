def iniciar():
  return [[' '] * 3 for _ in range(3)]

def desenhar(estado):
  for i in range(3):
    print('|', end = '')
    for j in range(3):
      print('{}|'.format(estado[i][j]), end ='')
    print()
  print()

#retorna:
#'x' se x ganhou
#'o' se o ganhou
#'-' se empatou
#' ' se não acabou
def acabou(estado):
  #checando vitorias horizontais e verticais
  for i in range(3):
    if estado[i] == ['x'] * 3:
      return 'x'
    if estado[i] == ['o'] * 3:
      return 'o'
    if estado[0][i] != ' ' and estado[0][i] == estado[1][i] and estado[1][i] == estado[2][i]:
      return estado[0][i]
    
  #checando a diagonal principal
  if estado[0][0] != ' ' and estado[0][0] == estado[1][1] and estado[1][1] == estado[2][2]:
    return estado[0][0]

  #checando a diagonal invertida
  if estado[0][2] != ' ' and estado[0][2] == estado[1][1] and estado[1][1] == estado[2][0]:
    return estado[0][2]

  if ' ' in estado[0] + estado[1] + estado[2]:
    return ' '

  return '-'

#retorna uma tupla sendo o:
#1o valor: pontuação do estado
#2o valor: posição da jogada que resulta na pontuação do 1o valor
def jog_max(estado):
  final = acabou(estado)
  if final == 'x':
    return(1, (-1, -1))
  if final == 'o':
    return(-1, (-1, -1))
  if final == '-':
    return(0, (-1, -1))

  maior = -2 #
  for i in range(3):
    for j in range(3):
      if estado[i][j] == ' ':
        estado[i][j] = 'x' #
        (pontuacao, (jog_x, jog_y)) = jog_min(estado)
        if pontuacao > maior: #
          maior = pontuacao
          melhor_jogada = (i, j)
        estado[i][j] = ' '

  return(maior, melhor_jogada)

def jog_min(estado):
  final = acabou(estado)
  if final == 'x':
    return(1, (-1, -1))
  if final == 'o':
    return(-1, (-1, -1))
  if final == '-':
    return(0, (-1, -1))

  menor = 2 #
  for i in range(3):
    for j in range(3):
      if estado[i][j] == ' ':
        estado[i][j] = 'o' #
        (pontuacao, (jog_x, jog_y)) = jog_max(estado)
        if pontuacao < menor: #
          menor = pontuacao
          melhor_jogada = (i, j)
        estado[i][j] = ' '

  return(menor, melhor_jogada)

def jogar_ia_vs_ia(estado):
  score, move = jog_max(estado)  # jogada da IA-X
  estado[move[0]][move[1]] = 'x'
  desenhar(estado)
  score, move = jog_min(estado)  # jogada da IA-O
  estado[move[0]][move[1]] = 'o'
  desenhar(estado)

  final = acabou(estado)
  if (final != 'x' and final != 'o' and final != '-'):
    jogar_ia_vs_ia(estado)

def jogar_ia_vs_humano(estado):
  human_check(estado) #jogada do player
  desenhar(estado)
  score, move = jog_min(estado) #jogada da IA
  estado[move[0]][move[1]] = 'o'
  desenhar(estado)

  final = acabou(estado)
  if(final != 'x' and final != 'o' and final != '-'):
    jogar_ia_vs_humano(estado)

def human_check(estado):
  #|1|2|3|
  #|4|5|6|
  #|7|8|9|

  count = 0
  check = int(input("Marque um campo disponivel (valor 1-9):"))

  for i in range(3):
    for j in range(3):
      count = count + 1
      if count == check:
        if estado[i][j] != ' ':
          print(count,check)
          print("Campo indisponivel, tente novamente:")
          human_check(estado)
        else:
          if check == 1:
            estado[0][0] = 'x'
          elif check == 2:
            estado[0][1] = 'x'
          elif check == 3:
            estado[0][2] = 'x'
          elif check == 4:
            estado[1][0] = 'x'
          elif check == 5:
            estado[1][1] = 'x'
          elif check == 6:
            estado[1][2] = 'x'
          elif check == 7:
            estado[2][0] = 'x'
          elif check == 8:
            estado[2][1] = 'x'
          elif check == 9:
            estado[2][2] = 'x'

def jog_max_alpha_beta(estado, alfa, beta):
  final = acabou(estado)
  if final == 'x':
    return (1, (-1, -1))
  if final == 'o':
    return (-1, (-1, -1))
  if final == '-':
    return (0, (-1, -1))

  maior = -2  #
  for i in range(3):
    for j in range(3):
      if estado[i][j] == ' ':
        estado[i][j] = 'x'  #
        (pontuacao, (jog_x, jog_y)) = jog_min_alpha_beta(estado, alfa, beta)
        if pontuacao > maior:  #
          maior = pontuacao
          melhor_jogada = (i, j)
        estado[i][j] = ' '
        alfa = max(alfa, pontuacao)
        if beta <= alfa:
          break

  return (maior, melhor_jogada)

def jog_min_alpha_beta(estado, alfa, beta):
  final = acabou(estado)
  if final == 'x':
    return (1, (-1, -1))
  if final == 'o':
    return (-1, (-1, -1))
  if final == '-':
    return (0, (-1, -1))

  menor = 2  #
  for i in range(3):
    for j in range(3):
      if estado[i][j] == ' ':
        estado[i][j] = 'o'  #
        (pontuacao, (jog_x, jog_y)) = jog_max_alpha_beta(estado, alfa, beta)
        if pontuacao < menor:  #
          menor = pontuacao
          melhor_jogada = (i, j)
        estado[i][j] = ' '
        beta = min(beta, pontuacao)
        if beta <= alfa:
          break

  return (menor, melhor_jogada)

def jogar_ia_vs_humano_alpha_beta(estado):
  human_check(estado) #jogada do player
  desenhar(estado)
  score, move = jog_min_alpha_beta(estado, float("-inf"), float("inf")) #jogada da IA
  estado[move[0]][move[1]] = 'o'
  desenhar(estado)

  final = acabou(estado)
  if(final != 'x' and final != 'o' and final != '-'):
    jogar_ia_vs_humano(estado)

def jogar_ia_vs_ia_alpha_beta(estado):
  score, move = jog_max_alpha_beta(estado, float("-inf"), float("inf"))  # jogada da IA-X
  estado[move[0]][move[1]] = 'x'
  desenhar(estado)
  score, move = jog_min_alpha_beta(estado, float("-inf"), float("inf"))  # jogada da IA-O
  estado[move[0]][move[1]] = 'o'
  desenhar(estado)

  final = acabou(estado)
  if (final != 'x' and final != 'o' and final != '-'):
    jogar_ia_vs_ia(estado)

#estado = iniciar()
#desenhar(estado)

#jogar_ia_vs_humano(estado)

#jogar_ia_vs_ia(estado)

#jogar_ia_vs_humano_alpha_beta(estado)

#jogar_ia_vs_ia_alpha_beta(estado)

def menu():
  estado = iniciar()
  print("Escolha um dos modos abaixo:")
  print("1 - jogar_ia_vs_humano")
  print("2 - jogar_ia_vs_ia")
  print("3 - jogar_ia_vs_humano_alpha_beta")
  print("4 - jogar_ia_vs_ia_alpha_beta")
  print("5 - sair")
  option = int(input("Digite o código do modo que deseja:"))
  if option == 1:
    desenhar(estado)
    jogar_ia_vs_humano(estado)
  elif option == 2:
    desenhar(estado)
    jogar_ia_vs_ia(estado)
  elif option == 3:
    desenhar(estado)
    jogar_ia_vs_humano_alpha_beta(estado)
  elif option == 4:
    desenhar(estado)
    jogar_ia_vs_ia_alpha_beta(estado)
  elif option == 5:
    exit()
  else:
    print("Código invalido, tente novamente:")
    menu()

menu()