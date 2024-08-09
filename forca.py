from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Jogo da Forca")

vidas = 6
palavra = ''

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
palavraMascarada = Entry(root, width=30, borderwidth=5, state='readonly')
palavraMascarada.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

def validaPalavra(valor):
    if valor.isalpha() == True:
        
        return True
    else:
        return False

def validaEntrada(valor):
    return len (valor) <= 1 and valor.isalpha() and valor.isidentifier

def bloqueiaEntrada():
    vcmd = (root.register(validaEntrada), '%P')
    e.config(validate='key', validatecommand=vcmd)

def convertePalarva():
    global palavra
    resultado = ''
    for i in palavra:
        resultado += '*'
    palavraMascarada.configure(state='normal')
    palavraMascarada.insert(0, resultado)
    palavraMascarada.configure(state='readonly')
    bloqueiaEntrada()
        
def confirma():
    global palavra
    current = e.get()  # Obter a palavra digitada pelo usuário
    valida = validaPalavra(current)  # Validar a palavra digitada
    
    if valida:
        palavra = current  # Atribuir a palavra digitada à variável global 'palavra'
        e.delete(0, END)
        return True
    else:
        return False
    
def iniciar():
    confirmarPalavra.grid_forget()
    confirmarLetra.grid(row=3, column=0)  

def diminuirVida():
    global vidas
    vidas -= 1
    if vidas == 0:
        messagebox.showerror("Fim de jogo", "A palavra era " + palavra)
        root.destroy()
      

def verificaPalavra():
    global palavra
    global palavraMascarada
    current = e.get()
    letra = current.lower
    e.delete(0, END)
    resultado = list(palavraMascarada.get())  # Obtém o texto atual como uma lista de caracteres
    atualizado = False

    for i in range(len(palavra)):
        if palavra[i] == letra:
            resultado[i] = letra
            atualizado = True

    if atualizado:
        palavraMascarada.configure(state='normal')
        palavraMascarada.delete(0, END)  # Limpa o texto atual
        palavraMascarada.insert(0, ''.join(resultado))  # Insere o texto atualizado
        palavraMascarada.configure(state='readonly')
    else:
        diminuirVida()
        quantidadeVidas = Button(root, text=vidas, padx=20, pady=5)
        quantidadeVidas.grid(row=3, column=2)
    

confirmarPalavra = Button(root, text='Confirmar Palavra', padx=40, pady=5, command=lambda: (iniciar(), convertePalarva()) if confirma() else None)
confirmarPalavra.grid(row=3, column=0)
quantidadeVidas = Button(root, text=vidas, padx=20, pady=5)
quantidadeVidas.grid(row=3, column=2)
confirmarLetra = Button(root, text='Confirmar Letra', padx=40, pady=5, command=lambda: verificaPalavra())
confirmarLetra.grid_forget()



root.mainloop()