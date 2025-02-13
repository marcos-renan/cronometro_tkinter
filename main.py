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
label_tempo.place(x=20, y=30) #localidade dentro da janela

botao_iniciar = tk.Button(win, text='Iniciar', width=10, height=2, bg=preto, fg=branco, font=('Ivy 8 bold'), relief='raised', overrelief='ridge') #botao para iniciar o cronometro
botao_iniciar.place(x=20, y=130) #localidade do botao na janela

botao_parar = tk.Button(win, text='Parar', width=10, height=2, bg=preto, fg=branco, font=('Ivy 8 bold'), relief='raised', overrelief='ridge') #botao para parar o cronometro
botao_parar.place(x=105, y=130) #localidade do botao na janela

botao_reiniciar = tk.Button(win, text='Reiniciar', width=10, height=2, bg=preto, fg=branco, font=('Ivy 8 bold'), relief='raised', overrelief='ridge') #botao para reiniciar o cronometro
botao_reiniciar.place(x=190, y=130) #localidade do botao na janela





win.mainloop() #loop para o funcionamento do software
