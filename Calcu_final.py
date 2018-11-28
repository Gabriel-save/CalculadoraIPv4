from tkinter import *

janela = Tk()
############################################CODIGO DA CALCULADORA#######################################################
def ipv4(): #Recebe o numero do ip e passar pela função da coleta.
  global ip
  ip = ""
  i = ip1.get()
  coletar(i)
  ip = resultado
#-------------------------------------------------------------#
def masc(): #Recebe o numero da mascara e passa pela função da coleta.
  global masc
  masc = ""
  g = masc1.get()
  coletar(g)
  masc = resultado
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
#-------------------------------------------------------------#

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
  subrededec['text'] = resultado

  print("\nEndereço da subrede em binario é =",endereco)
  subredebin['text'] = endereco


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
  broaddec['text'] = resultado

  print("\nBroadcast da subrede em binario é =",broadcast)
  broabin['text'] = broadcast


#----------------------------------------------------------

def core(): #Organiza todas as funções.

  global masc,ip,classe,broadcast,ip
  print('\nEndereço IP em binário: ',ip)
  ipbin['text'] = ip
  print('\nMáscara de sub-rede em binário: ',masc)
  mascbin['text'] = masc

#---------------------------------------------------------
############################################INTERFACE GRAFICA############################################################
def bt_click():
	ipv4()
	masc()
	core()
	broad()
	end()

#TITULO DA JANELA#
janela.title("Calculadora")
janela['bg'] = 'light sky blue'

#NOME DO PROGRAMA#
titulo = Label(janela, text = "Calculadora IPv4", bg = 'deep sky blue')
titulo.pack(side=TOP, fill=X)

#ENTRADA DE IP#
ip1 = Entry(janela)
ip1.place(x = 100, y = 25)

#TITULO DA ENTRADA DO IP#
iptitle = Label(janela,text="N° IPv4:", fg = 'blue',bg = 'light sky blue')
iptitle['font'] = ('Arial','10','bold')
iptitle.place(x = 1, y = 22)

#ENTRADA DA MASCARA DO IP#
masc1 = Entry(janela)
masc1.place(x = 100, y = 50)

#TITULO DA ENTRADA DA MASCARA DO IP#
masctitle = Label(janela,text="N° Sub-rede:", fg = 'blue', bg = 'light sky blue')
masctitle['font'] = ('Arial','10','bold')
masctitle.place(x = 1, y = 50)

#TITULO IPv4 EM BINÁRIO#
ipbintitle = Label(janela, text="IPv4 em Binário:", fg = 'red', bg = 'light sky blue')
ipbintitle['font'] = ('Arial','10','bold')
ipbintitle.place(x = 1, y = 80)

#RESULTADO IPV4 EM BINARIO#
ipbin = Label(janela, text='', fg = 'red', bg = 'light sky blue')
ipbin['font'] = ('Arial','10','bold')
ipbin.place(x = 110, y = 80)

#TITULO MASCARA DE SUB-REDE EM BINARIO#
mascbintitle = Label(janela, text="Máscara da Sub-rede em Binário:", fg = 'red', bg = 'light sky blue')
mascbintitle['font'] = ('Arial','10','bold')
mascbintitle.place(x = 1, y = 110)

#RESULTADO DA MASCARA DE SUBREDE EM BINARIO#
mascbin = Label(janela, text='', fg = 'red', bg = 'light sky blue')
mascbin['font'] = ('Arial','10','bold')
mascbin.place(x = 220, y = 110)

#TITULO ENDEREÇO DA SUBREDE#
subredetitle = Label(janela, text="Endereço da sub-rede:", fg='green', bg = 'light sky blue')
subredetitle['font'] = ('Arial','10','bold')
subredetitle.place(x = 1, y=140)

#RESULTADO DO ENDEREÇO DA SUBREDE#
subrededec = Label(janela,text='',fg='green', bg = 'light sky blue')
subrededec['font'] = ('Arial','10','bold')
subrededec.place(x = 150, y = 140)

#TITULO ENDEREÇO DA SUBREDE EM BINARIO#
subredebintitle = Label(janela, text="Endereço da sub-rede em Binário:", fg='green', bg = 'light sky blue')
subredebintitle['font'] = ('Arial','10','bold')
subredebintitle.place(x = 1, y=170)

#RESULTADO ENDEREÇO DA SUBREDE EM BINARIO#
subredebin = Label(janela,text='',fg='green', bg = 'light sky blue')
subredebin['font'] = ('Arial','10','bold')
subredebin.place(x = 222, y = 170)

#TITULO ENDEREÇO DE BROADCAST#
broadtitle = Label(janela, text="Endereço de Broadcast:", fg='green', bg = 'light sky blue')
broadtitle['font'] = ('Arial','10','bold')
broadtitle.place(x = 1, y=200)

#RESULTADO ENDEREÇO DE BROADCAST#
broaddec = Label(janela,text='',fg='green', bg = 'light sky blue')
broaddec['font'] = ('Arial','10','bold')
broaddec.place(x = 155, y = 200)

#TITULO ENDEREÇO DE BROADCAST EM BINARIO#
broadbintitle = Label(janela, text="Endereço de Broadcast em Binário:",fg='green', bg = 'light sky blue')
broadbintitle['font'] = ('Arial','10','bold')
broadbintitle.place(x = 1, y = 230)

#RESULTADO ENDEREÇO DE BROADCAST EM BINARIO#
broabin = Label(janela, text="Endereço de Broadcast em Binário:",fg='green', bg = 'light sky blue')
broabin['font'] = ('Arial','10','bold')
broabin.place(x = 155, y = 230)

#BOTAO CALCULAR#
bt = Button(janela, text = "Calcular", fg = 'blue', bg = 'white', command=bt_click)
bt['font'] = ('Arial','10','bold')
bt.pack(side=BOTTOM, fill=X)


janela.geometry('1000x300+200+200')
janela.mainloop()

#POPUP#

from tkinter import *

janela = Tk()
janela.title('error')
janela['bg'] = 'black'
error = Label(janela, text='''
  ERROR!
  Os Valores inforados estão incorretos!
  ''')
error.pack(side=LEFT)
error['bg'] = 'black'
error['fg'] = 'red'
error['font'] = ("Arial","10","bold")
janela.geometry('350x200+100+100')
janela.mainloop()
