def ipv4(): #Recebe o numero do ip e passar pela função da coleta.
  global ip
  ip = ""
  i = str(input("\nInforme o numero do IPV4:"))
  coletar(i)
  ip = resultado

#-------------------------------------------------------------#

def masc(): #Recebe o numero da mascara e passa pela função da coleta.
  global masc
  masc = ""
  g = str(input("\nInforme o numero da Máscara de sub-rede:"))
  coletar(g)
  masc = resultado

#---------------------------------------------------------------#

def limites(n):
  
  x = 0

  global lista

  separar(n)

  while teste == 0:
    if lista[x] < 0 or lista[x] > 255:
      print("\nvalores incorretos")
    else:
      teste = 1
      x += 1

#---------------------------------------------------------------#

def separar(n): #Transforma uma string em lista de numeros inteiros.

  global lista

  linha = ""
  lista = []

  n += "." #Coloquei esse ponto porque sem ele o FOR X In I: náo percorre toda a minha lista, fica faltando o ultimo elemento. é uma gambiarra.

  for x in n: #Esse for é usado para separar os numeros que vão ser convertidos para binario em uma lista, separando cada numero em um vertice diferente da lista.
    if x != ".": #usando o ponto para separar os vertices.
      linha += x
    else:
      mat = int(linha) #transformo o numero de str para int.
      lista.append(mat) #Adiciono a um vertice na lista em INT.
      linha = "" #reinicio o valor da linha

#------------------------------------------------------------------

def coletar(n): #Faz a coleta dos dados e calcula.

  separar(n)
  
  global a, result, resultado, classe,lista
  resultado = ""

  for x in range (len(lista)):
    a = lista[x]
    dec2bin()

    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result

 #-------------------------------------------------------------#

def dec2bin(): #calculadora que vai converter o indice da lista em binario.
  i = 0
  global a, result
  result = ''
  lista = []
  while a>1:
    i = a%2
    lista.append (i)
    a = a//2
  if a == 1:
    lista.append (1)

  while (len(lista))<8: #Deixar o numero sempre sendo um octeto de bit
    lista.append(0)
  lista.reverse()

  for b in lista:  #transformando a lista em uma string
    result += str(b)

#--------------------------------------------------------

def bin2dec(n): #Calculadora que transforma de binario para decimal
  
  global result
  result = ""

  i,dec = 0,0

  lista = n
  lista = list(lista)
  lista.reverse()

  for x in (lista):
    if x == "1":
      dec += 2**i
    i += 1
  result = str(dec)

#--------------------------------------------------------

def end(): #Função que calcula o endereço da subrede e disponibiliza tanto em binario quanto decimal.

  global masc,ip,result,lista
  endereco,resultado = "",""
  listamasc,listaip = [],[]

  for x in masc:
    listamasc.append(x)
  for y in ip:
    listaip.append(y)

  for z in range (len(listamasc)):
    
    if listamasc[z] == "0":
      listaip[z] = "0"

  for b in listaip:  #transformando a lista em uma string
    endereco += str(b)

  separar(endereco)

  for x in range (len(lista)):
    a = str(lista[x])
    bin2dec(a)

    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result

  print("\nEndereço da subrede =",resultado)

  print("\nEndereço da subrede em binario é =",endereco)

#---------------------------------------------------------

def broad():#Função que faz o mesmo porem calcula o broadcast.

  broadcast,resultado = "",""
  global masc,ip,result
  listamasc,listaip = [],[]

  for x in masc:
    listamasc.append(x)
  for y in ip:
    listaip.append(y)

  for z in range (len(listamasc)):
    if listamasc[z] == "0":
      listaip[z] = "1"

  for b in listaip:  #transformando a lista em uma string
    broadcast += str(b)

  separar(broadcast)

  for x in range (len(lista)):
    a = str(lista[x])
    bin2dec(a)

    if x != 3: #Essa condicional evita que seja concatenado junto a string um ponto extra no final
      resultado+=result+'.'
    else:
      resultado+=result

  print("\nBroadcast da subrede =",resultado)

  print("\nBroadcast da subrede em binario é =",broadcast)

#----------------------------------------------------------

def core(): #Organiza todas as funções.

  global masc,ip,classe,broadcast,ip
  print('\nEndereço IP em binário: ',ip)
  print('\nMáscara de sub-rede em binário: ',masc)

#---------------------------------------------------------

def main():
  ipv4()
  masc()
  core()
  end()
  broad()
main()
