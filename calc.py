import PySimpleGUI as sg

sg.theme('Dark Grey 13')

""" Configuração de formato e cores dos botões """
fb = { 'size':(3, 2), 'pad':(0,0), 'button_color':('white', '#585b5e'), 'font':('Helvetica', 12) }
op = { 'size':(3, 2), 'pad':(0,0), 'button_color':('white', '#bf780d'), 'font':('Helvetica', 12) }
nm = { 'size':(3, 2), 'pad':(0,0), 'button_color':('white', '#888b8f'), 'font':('Helvetica', 12) }
lb = { 'size':(11, 2), 'pad':(0,0), 'button_color':('white', '#888b8f'), 'font':('Helvetica', 12) }

""" Linhas de botões da calculadora com suas devidas formatações """
linha1 = [sg.Button('AC', key='-AC-', **fb), 
          sg.Button('+/-', key='-POSNEG-', **fb), 
          sg.Button('%', key='%', **fb), 
          sg.Button('/', key='/', **op)]

linha2 = [sg.Button('7', key='7', **nm), 
          sg.Button('8', key='8', **nm), 
          sg.Button('9', key='9', **nm), 
          sg.Button('*', key='*', **op)]

linha3 = [sg.Button('4', key='4', **nm), 
          sg.Button('5', key='5', **nm), 
          sg.Button('6', key='6', **nm), 
          sg.Button('-', key='-', **op)]

linha4 = [sg.Button('1', key='1', **nm), 
          sg.Button('2', key='2', **nm), 
          sg.Button('3', key='3', **nm), 
          sg.Button('+', key='+', **op)]

linha5 = [sg.Button('0', key='0', **lb), 
          sg.Button('.', key='.', **nm), 
          sg.Button('=', key='=', **op)]

""" Organização das linhas em um layout (formato de exibição ordem dos componentes de forma integrada) """
layout = [
     [sg.Text('0', size=(13,1), pad=(0,0), key='-RESULT-', text_color='white', background_color='#414345', font=('Helvetica', 30), justification='right')],
     linha1,
     linha2,
     linha3,
     linha4,
     linha5
]

""" Cria a janela em si usando o layout que foi criado acima """
window = sg.Window('Calculadora', layout)

view_model = { '' }

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    # já que não aprendi ainda como evitar o "while True" a condição de saída é a primeira opção do meu loop
    if event == sg.WIN_CLOSED:
        break
    if event == '-UM-':
        window['-RESULT-'].update()

window.close()