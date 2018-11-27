from tkinter import * #chamando o tkinter#
from CalculadoraIP_v2 import * #chamando o CODIGO - BACKEND#
from Interface_v2 import * #chamando o CODIGO INTERFACE - FRONTEND#

def bt_click():
	a = ipv4()
	b = masc()
	c,d = broad(b,a)
	f,g = end(b,a)
	ipbinresult['text'] = a
	srbininfo['text'] = b
	endsrinfo['text'] = g
	endsubinfo['text'] = f
	broadcastinfo['text'] = d
	brodbininfo['text'] = c
