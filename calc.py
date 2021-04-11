import PySimpleGUI as sg

sg.theme('Dark Grey 13')

linha1 = [sg.Button('AC', size=(3, 2), key='-AC-', pad=(0,0), button_color=('white', '#585b5e'), font=('Helvetica', 12)), 
          sg.Button('+/-', size=(3, 2), key='-POSNEG-', pad=(0,0), button_color=('white', '#585b5e'), font=('Helvetica', 12)), 
          sg.Button('%', size=(3, 2), key='%', pad=(0,0), button_color=('white', '#585b5e'), font=('Helvetica', 12)), 
          sg.Button('/', size=(3, 2), key='/', pad=(0,0), button_color=('white', '#bf780d'), font=('Helvetica', 12))]

linha2 = [sg.Button('7', size=(3, 2), key='7', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('8', size=(3, 2), key='8', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('9', size=(3, 2), key='9', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('*', size=(3, 2), key='*', pad=(0,0), button_color=('white', '#bf780d'), font=('Helvetica', 12))]

linha3 = [sg.Button('4', size=(3, 2), key='4', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('5', size=(3, 2), key='5', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('6', size=(3, 2), key='6', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('-', size=(3, 2), key='-', pad=(0,0), button_color=('white', '#bf780d'), font=('Helvetica', 12))]

linha4 = [sg.Button('1', size=(3, 2), key='1', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('2', size=(3, 2), key='2', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('3', size=(3, 2), key='3', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('+', size=(3, 2), key='+', pad=(0,0), button_color=('white', '#bf780d'), font=('Helvetica', 12))]

linha5 = [sg.Button('0', size=(11, 2), key='0', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button(',', size=(3, 2), key=',', pad=(0,0), button_color=('white', '#888b8f'), font=('Helvetica', 12)), 
          sg.Button('=', size=(3, 2), key='=', pad=(0,0), button_color=('white', '#bf780d'), font=('Helvetica', 12))]

layout = [
     [sg.Text('0', size=(13,1), pad=(0,0), key='-RESULT-', text_color='white', background_color='#414345', font=('Helvetica', 30), justification='right')],
     linha1,
     linha2,
     linha3,
     linha4,
     linha5
]

# layout =  [[sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]


window = sg.Window('Calculadora', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-UM-':
        window['-RESULT-'].update()

window.close()