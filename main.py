import tkinter as tk

#definindo cores
preto = '#0a0a0a'
branco = '#fafcff'
verde = '#21c25c'
vermelho = '#eb463b'
cinza = '#dedcdc'
azul = '#3080f0'

win = tk.Tk() #criando a janela com win 'window'
win.title('Cronômetro') #definindo o titulo da janela
win.geometry('300x180') #definindo o tamanho da janela
win.configure(bg=preto) #cor de fundo
win.resizable(width=False, height=False) #bloqueando o redimensionamento da janela

label_nome = tk.Label(win, text='Cronômetro', fon=('Arial 10'), bg=preto, fg=branco) #Nome do app
label_nome.place(x=20, y=5) #localidade dentro da janela

label_tempo = tk.Label(win, text='00:00:00', fon=('Times 50 bold'), bg=preto, fg=azul) #cronometro
label_tempo.place(x=20, y=25) #localidade dentro da janela





win.mainloop() #loop para o funcionamento do software
