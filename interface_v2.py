from tkinter import *
from CalculadoraIP_v2 import *
from MainCALC import *


############################################INTERFACE GRAFICA############################################################
janela = Tk()
#TITULO DA JANELA#
janela.title("Calculadora")
janela['bg'] = 'light sky blue'

#NOME DO PROGRAMA#
titulo = Label(janela, text = "Calculadora IPv4", bg = 'deep sky blue')
titulo.pack(side=TOP, fill=X)

#ENTRADA DE IP#
ip1 = Entry(janela)
ip1.place(x = 100, y = 25)
ipinfo = Label(janela,text="N° IPv4:", fg = 'blue',bg = 'light sky blue')
ipinfo['font'] = ('Arial','10','bold')
ipinfo.place(x = 1, y = 22)

#ENTRADA DA MASCARA DO IP#
subred1 = Entry(janela)
subred1.place(x = 100, y = 50)
subredeinfo = Label(janela,text="Mascara: ", fg = 'blue', bg = 'light sky blue')
subredeinfo['font'] = ('Arial','10','bold')
subredeinfo.place(x = 1, y = 50)

#TITULO IPv4 EM BINÁRIO#
ipbinary = Label(janela, text="IPv4 em Binário:", fg = 'red', bg = 'light sky blue')
ipbinary['font'] = ('Arial','10','bold')
ipbinary.place(x = 1, y = 80)

#RESULTADO IPV4 EM BINARIO#
ipbinresult = Label(janela, text='', fg = 'red', bg = 'light sky blue')
ipbinresult['font'] = ('Arial','10','bold')
ipbinresult.place(x = 110, y = 80)

#TITULO MASCARA DE SUB-REDE EM BINARIO#
subredebin = Label(janela, text="Máscara da Sub-rede em Binário:", fg = 'red', bg = 'light sky blue')
subredebin['font'] = ('Arial','10','bold')
subredebin.place(x = 1, y = 110)

#RESULTADO DA MASCARA DE SUBREDE EM BINARIO#
srbininfo = Label(janela, text='', fg = 'red', bg = 'light sky blue')
srbininfo['font'] = ('Arial','10','bold')
srbininfo.place(x = 220, y = 110)

#TITULO ENDEREÇO DA SUBREDE#
endsubrede = Label(janela, text="Endereço da sub-rede:", fg='green', bg = 'light sky blue')
endsubrede['font'] = ('Arial','10','bold')
endsubrede.place(x = 1, y=140)

#RESULTADO DO ENDEREÇO DA SUBREDE#
endsrinfo = Label(janela,text='',fg='green', bg = 'light sky blue')
endsrinfo['font'] = ('Arial','10','bold')
endsrinfo.place(x = 150, y = 140)

#TITULO ENDEREÇO DA SUBREDE EM BINARIO#
endsubin = Label(janela, text="Endereço da sub-rede em Binário:", fg='green', bg = 'light sky blue')
endsubin['font'] = ('Arial','10','bold')
endsubin.place(x = 1, y=170)

#RESULTADO ENDEREÇO DA SUBREDE EM BINARIO#
endsubinfo = Label(janela,text='',fg='green', bg = 'light sky blue')
endsubinfo['font'] = ('Arial','10','bold')
endsubinfo.place(x = 222, y = 170)

#TITULO ENDEREÇO DE BROADCAST#
broadcast = Label(janela, text="Endereço de Broadcast:", fg='green', bg = 'light sky blue')
broadcast['font'] = ('Arial','10','bold')
broadcast.place(x = 1, y=200)

#RESULTADO ENDEREÇO DE BROADCAST#
broadcastinfo = Label(janela,text='',fg='green', bg = 'light sky blue')
broadcastinfo['font'] = ('Arial','10','bold')
broadcastinfo.place(x = 155, y = 200)

#TITULO ENDEREÇO DE BROADCAST EM BINARIO#
brodbin = Label(janela, text="Endereço de Broadcast em Binário:",fg='green', bg = 'light sky blue')
brodbin['font'] = ('Arial','10','bold')
brodbin.place(x = 1, y = 230)

#RESULTADO ENDEREÇO DE BROADCAST EM BINARIO#
brodbininfo = Label(janela, text="Endereço de Broadcast em Binário:",fg='green', bg = 'light sky blue')
brodbininfo['font'] = ('Arial','10','bold')
brodbininfo.place(x = 155, y = 230)

#BOTAO CALCULAR#
bt = Button(janela, text = "Calcular", fg = 'blue', bg = 'white', command = bt_click)
bt['font'] = ('Arial','10','bold')
bt.pack(side=BOTTOM, fill=X)


janela.geometry('1000x300+200+200')
janela.mainloop()
