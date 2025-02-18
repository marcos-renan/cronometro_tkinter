import tkinter as tk

#definindo cores
preto = '#0a0a0a'
branco = '#fafcff'
verde = '#21c25c'
vermelho = '#eb463b'
cinza = '#dedcdc'
azul = '#3080f0'


#definindo a janela
win = tk.Tk() #criando a janela com win 'window'
win.title('Cronômetro') #definindo o titulo da janela
win.geometry('300x180') #definindo o tamanho da janela
win.configure(bg=preto) #cor de fundo
win.resizable(width=False, height=False) #bloqueando o redimensionamento da janela


#variaveis globais
global tempo
global rodar
global contador

tempo = '00:00:00'
rodar = False
contador = -5


#funcao para iniciar o cronometro
def iniciar():
  #variaveis globais
  global tempo
  global contador

  if rodar:
    #antes do conometro iniciar
    if contador <= -1:
      inicio = 'Começamdo em ' + str(contador)
      label_tempo['text'] = inicio
      label_tempo['font'] = 'Arial 10'
    else:
      print('Condição else satisfeita')
      contador += 1

#funcao para dar inicio a funcao iniciar
def start():
  

#label nome do app
label_nome = tk.Label(win, text='Cronômetro', fon=('Arial 10'), bg=preto, fg=branco)
label_nome.place(x=20, y=5) #localidade dentro da janela

#label do cronometro
label_tempo = tk.Label(win, text=tempo, fon=('Times 50 bold'), bg=preto, fg=vermelho)
label_tempo.place(x=20, y=30) #localidade dentro da janela

#botao para iniciar o cronometro
botao_iniciar = tk.Button(win, text='Iniciar', width=10, height=2, bg=preto, fg=branco, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=25, y=130) #localidade do botao na janela

#botao para parar o cronometro
botao_parar = tk.Button(win, text='Parar', width=10, height=2, bg=preto, fg=branco, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_parar.place(x=110, y=130) #localidade do botao na janela

#botao para reiniciar o cronometro
botao_reiniciar = tk.Button(win, text='Reiniciar', width=10, height=2, bg=preto, fg=branco, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=195, y=130) #localidade do botao na janela


#loop para o funcionamento do software
win.mainloop()
