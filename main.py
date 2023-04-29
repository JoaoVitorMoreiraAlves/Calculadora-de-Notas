from tkinter import *


janela = Tk()

janela.geometry("550x450")
janela.resizable(width=False, height=False)
janela.configure(bg="#A020F0")
janela.title("Calculadora da Média")
janela.iconbitmap("icone.ico")

#lógica dos calculos

def calcula():
    nota1 = float(e_nota1.get())
    nota2 = float(e_nota2.get())
    sub = float(e_sub.get())
    
    if nota1 + nota2 < 12.0:
        if nota1 < nota2:
            if nota1 < sub:
                media = (nota2+sub)/2
            else:
                media = (nota2+nota1)/2
        elif nota2 < nota1:
            if nota2 < sub:
                media = (nota1+sub)/2       
            else:
                media = (nota1+nota2)/2
        else:
            media = (nota1+nota2)/2
    else:
        media = (nota1+nota2)/2

    l_resultado["text"] = "{:.1f}".format(media)



def limpa():
    l_resultado["text"] = "00.0"
    e_nota1.delete(0, END)
    e_nota2.delete(0, END)
    e_sub.delete(0, END)






#Criando Frames

frame_borda_cima = Frame(janela, width=550, height=20, bg="#A020F0")
frame_borda_cima.grid(row=0, column=0)

frame_cima = Frame(janela, width=510, height=100, bg="#FFFFFF",bd=3, relief=SOLID)
frame_cima.grid(row=1, column=0)

frame_borda_meio = Frame(janela, width=550, height=20, bg="#A020F0")
frame_borda_meio.grid(row=2, column=0)

frame_baixo = Frame(janela, width=510, height=290, bg="#FFFFFF",bd=3, relief=SOLID)
frame_baixo.grid(row=3, column=0)


#Criando Label para o Frame cima


l_titulo = Label(frame_cima, text="Calculadora da Média de Notas", font="Arial 14 bold", 
                 width=30, height=2, relief=FLAT, bg="#FFFFFF")
l_titulo.place(x=75, y=23)





#Criando Labels e Entrys para o Frame de Baixo


#Nota 1
l_nota1 = Label(frame_baixo, text="1º Nota:", font="Arial 12 bold", bg="#FFFFFF")
l_nota1.place(x=30, y=30)
#Entry 1
e_nota1 = Entry(frame_baixo, width=5, relief=SOLID, bd=3)
e_nota1.place(x=130, y=33)



#Nota 2
l_nota2 = Label(frame_baixo, text="2º Nota:", font="Arial 12 bold", bg="#FFFFFF")
l_nota2.place(x=30, y=70)
#Entry 2
e_nota2 = Entry(frame_baixo, width=5, relief=SOLID, bd=3)
e_nota2.place(x=130, y=73)




#Nota Substitutiva
l_sub = Label(frame_baixo, text="Nota SUB:", font="Arial 12 bold", bg="#FFFFFF")
l_sub.place(x=30, y=110)

e_sub = Entry(frame_baixo, width=5, relief=SOLID, bd=3)
e_sub.place(x=130, y=113)



#Label da Média
l_media = Label(frame_baixo, text="Média", font="Arial 12 bold", bg="#FFFFFF")
l_media.place(x=330, y=30)


l_resultado = Label(frame_baixo, text="00.0", font="Arial 16 bold", width=10, height=3, 
                    bg="#A020F0", fg="#FFFFFF", bd=3, relief=SOLID)
l_resultado.place(x=285, y=60)




#Botão para calcular o resultado das provas

b_resultado = Button(frame_baixo,text="Calcular a Média", width=35, height=1, relief=SOLID,
                     border=3, font="Arial 16 bold", bg="#A020F0", fg="#FFFFFF", command=calcula)
b_resultado.place(x=20, y=230)


#Botão para limpar as notas e média

b_limpa = Button(frame_baixo,text="Limpar as Informações", width=35, height=1, relief=SOLID,
                     border=3, font="Arial 16 bold", bg="#A020F0", fg="#FFFFFF", command=limpa)
b_limpa.place(x=20, y=170)








janela.mainloop()