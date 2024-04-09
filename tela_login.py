from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# cores
cor1 = "#f0f3f5"  # Preto / black
cor2 = "#feffff"  # branco / white
cor3 = "#9703ad"  # roxo / purple
cor4 = "#38576b"  # valor / value
cor5 = "#403d3d"  # letras / letters

#criando janela tkinter
janela = Tk()
janela.title("Login")
janela.geometry("310x300") #tamanho da janela
janela.configure(background=cor2) #cor de fundo
janela.resizable(width=FALSE, height=FALSE) #para as dimensões da janela não ser alterada

#dividindo a janela.                                        estilo          
frame_cima = Frame(janela, width=210, height=50, bg=cor2, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor2, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurando o frame_cima
label_nome = Label(frame_cima, text="LOGIN ♡", anchor=NE,font=("Ivy 25 "),bg=cor2, fg=cor5)
label_nome.place(x=5, y=5)

#label da linha que fica em baixo do nome login
label_linha = Label(frame_cima, text="",width=275, anchor=NW, font=("Ivy 1 "),bg=cor3, fg=cor5)
label_linha.place(x=10, y=45)

#nome do usuario e senha
credenciais = ["laihany", "12345"]

#função para verificar senha
def verificar_senha():
    nome = entry_nome.get()
    senha = entry_pass.get()

#criando uma condição
    #se o nome for igual a lay e senha *********
    if nome =="lay" and senha =="123456789":
#usar mensagem do tkinter
        messagebox.showinfo("Login", "seja bem vindo Lay ♡!")
#caso não for a Lay    
    elif credenciais[0] == nome and credenciais[1] == senha:
         messagebox.showinfo("Login", "seja bem vindo de volta ♡!" +credenciais[0])

        #apagar o que tiver na tela/frame baixo/cima tudo
         for widget in frame_baixo.winfo_children():
            widget.destroy()

         for widget in frame_cima.winfo_children():
            widget.destroy()    

         nova_janela()

#se caso falhar   
    else:
         messagebox.showwarning("Erro", "Verifique o nome e a senha")

#criando nova função para poder entrar        
#função apos verificação
def nova_janela():
    #configurando o frame_cima
    label_nome = Label(frame_cima, text="Usuario: " +credenciais[0], anchor=NE,font=("Ivy 20 "),bg=cor2, fg=cor5)
    label_nome.place(x=5, y=5)

    #configurando o frame_baixo
    label_nome = Label(frame_baixo, text="Seja bem vindo ♡ " +credenciais[0], anchor=NE,font=("Ivy 17 "),bg=cor2, fg=cor5)
    label_nome.place(x=5, y=105)

#label da linha que fica em baixo do nome login
label_linha = Label(frame_cima, text="",width=275, anchor=NW, font=("Ivy 1 "),bg=cor3, fg=cor5)
label_linha.place(x=10, y=45)


#configurando o frame_baixo
label_nome = Label(frame_baixo, text="Nome *", anchor=NW,font=("Ivy 10 "),bg=cor2, fg=cor5)
label_nome.place(x=10, y=20)

entry_nome = Entry(frame_baixo, width=25, justify="left", font=("", 15), highlightthickness=1, relief="solid" )

entry_nome.place(x=14, y=50)

label_pass = Label(frame_baixo, text="Senha *", anchor=NW,font=("Ivy 10 "),bg=cor2, fg=cor5)
label_pass.place(x=10, y=95)
                                                        #SHOW="*" para deixar a senha sem aparecer
entry_pass = Entry(frame_baixo, width=25, justify="left", show="*", font=("", 15), highlightthickness=1, relief="solid" )
entry_pass.place(x=14, y=130)

#botão                                                                       bold = negritado
botao_confirmar = Button(frame_baixo, command=verificar_senha, text="Entrar", width=15, height=2, font=("Ivy 8 bold "),bg=cor3, fg=cor2, relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=100, y=180)



janela.mainloop()