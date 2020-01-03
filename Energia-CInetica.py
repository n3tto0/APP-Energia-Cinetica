from tkinter import *    # Por Maurício N. (Shark)
import tkinter as tk
from PIL import ImageTk, Image 
from  functools import partial
#-----------------------------------------------= Master =----------------------------------------
janela = Tk()
janela.title()

largura = 375
altura = 234

largura_screen = janela.winfo_screenwidth()
altuea_screen = janela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altuea_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
janela.resizable(False, False)

#------------------------------------------------= BG =-------------------------------------------

image1 = Image.open("background.png") # <-- uma forma criativa de ser usar uma imagem como Background!
image2 = ImageTk.PhotoImage(image1)
background_label = Label(janela, image=image2)
background_label.image1=image1
background_label.place(x= 0, y= 0, width=375, height=234)

#-------------------------------------------------------------------------------------------------

#--------------------------------------------= Funções =------------------------------------------
def Calc_Cinetica(calc): #<-- função a ser chamada por um button!
	m = float(ed1.get()) 
	v = float(ed2.get())
	lb["text"] = m * (v ** 2) * (1/2) #<-- O calculo precisa ser necessariamente escrito aqui,
									  # já que foi escrito para ser rodado com Partial
#-------------------------------------------------------------------------------------------------

#--------------------------------------------= Labels =-------------------------------------------

ed1 = Entry(janela,    # Utilizei o place para ter uma admistração maior do layuot do programa!!
	bd=2)
ed1.place(x=5, y=5)

ed2 = Entry(janela,
	bd=2)
ed2.place(x=5, y=25)

lb = Label(janela,
	text="")
lb.place(x=65, y=50)

lb2 = Label(janela,
	text="Resuldado:")
lb2.place(x=5, y=50)

#-------------------------------------------------------------------------------------------------

#--------------------------------------------= Botões =-------------------------------------------

bt1 = Button(janela, text="Calcular",
	bd=3)
bt1["command"] = partial(Calc_Cinetica, bt1) #<-- Partial sendo utilizado nessa parte do código!! 
bt1.place(x=130, y=10)

#-------------------------------------------------------------------------------------------------

janela.mainloop()