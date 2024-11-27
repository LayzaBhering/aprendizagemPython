from tkinter import *

janela = Tk()

def buttonClick():
    print("buttonClick")

    if(str(num1.get()).isnumeric() and str(num2.get()).isnumeric()):
        numero1 = int(num1.get())
        numero2 = int(num2.get())

        labelUm["text"] = numero1 + numero2
    else:
        print('Tente novamente!')

num1 = Entry(janela)
num1.place(x=100, y=100)

num2 = Entry(janela)
num2.place(x=100, y=130)

button = Button(janela, text="soma", width=10, command=buttonClick)
button.place(x=250, y =120)

labelUm  = Label(janela, text="Soma de valores [ 1 ] + [ 2 ]")
labelUm.place(x=80, y=200)

janela.geometry("500x300+400+200")

janela.mainloop()