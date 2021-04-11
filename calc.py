import PySimpleGUI as sg

sg.theme('Dark Grey 13')

""" Configuração de formato e cores dos botões """
fb = { 'size':(3, 2), 'pad':(0,0), 'button_color':('white', '#585b5e'), 'font':('Helvetica', 12) }
op = { 'size':(3, 2), 'pad':(0,0), 'button_color':('white', '#bf780d'), 'font':('Helvetica', 12) }
nm = { 'size':(3, 2), 'pad':(0,0), 'button_color':('white', '#888b8f'), 'font':('Helvetica', 12) }
lb = { 'size':(11, 2), 'pad':(0,0), 'button_color':('white', '#888b8f'), 'font':('Helvetica', 12) }

""" Linhas de botões da calculadora com suas devidas formatações """
linha1 = [sg.Button('LC', key='-LC-', **fb), 
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
     [sg.Text('0.0', size=(13,1), pad=(0,0), key='-VISOR-', text_color='white', background_color='#414345', font=('Helvetica', 30), justification='right')],
     linha1,
     linha2,
     linha3,
     linha4,
     linha5
]

""" Cria a janela em si usando o layout que foi criado acima """
window = sg.Window('Calculadora', layout, return_keyboard_events=True, use_default_focus=False)

view_model = { 'inteiro': [], 'decimal': [], 'separador':False, 'operacao':'', 'numA': 0., 'numB': 0., 'resultado': 0. }

def juntar_inteiro_decimal():
    """ faz a junção dos números antes e depois da casa decimal """
    return float(''.join(view_model['inteiro']) + '.' + ''.join(view_model['decimal']))

def atualizar_visor_calculadora(valor):
    """ método desponsável por atualizar o visor da calculadora """
    window['-VISOR-'].update(value=valor)

def limpar_view_model():
    """ Método responsável por limpar a variável view_model que guarda a situação da tela """
    global view_model
    view_model['inteiro'].clear()
    view_model['decimal'].clear()
    view_model['separador'] = False 

def ao_clicar_numero(event):
    """ método responsável por adicionar o numero novo no view_model e atualizar o visor """
    global view_model
    if view_model['separador']:
        view_model['decimal'].append(event)
    else:
        view_model['inteiro'].append(event)
    atualizar_visor_calculadora(juntar_inteiro_decimal())

def ao_clicar_operador(event):
    """ metódo responsável por cuidar do uso dos simbolos matemáticos permitidos na calculadora """
    global view_model
    view_model['operacao'] = event
    try:
        view_model['numA'] = juntar_inteiro_decimal()
    except:
        view_model['numA'] = view_model['resultado']
    limpar_view_model()

def ao_clicar_igual():
    """ método responsável por calcular o resultado do calculo feito na calculadora """
    global view_model
    view_model['numB'] = juntar_inteiro_decimal()
    try:
        view_model['resultado'] = eval(str(view_model['numA']) + view_model['operacao'] + str(view_model['numB']))
        atualizar_visor_calculadora(view_model['resultado'])
        limpar_view_model()    
    except:
        atualizar_visor_calculadora("ERROR! DIV/0")
        limpar_view_model()
def ao_clicar_positivo_negativo():
    global view_model
    if view_model['inteiro'][0] == '-':
        del view_model['inteiro'][0]
    else:
        view_model['inteiro'].insert(0, '-')
    atualizar_visor_calculadora(juntar_inteiro_decimal())

while True:  # Event Loop
    (event, values) = window.read()
    print(event, values)
    # já que não aprendi ainda como evitar o "while True" a condição de saída é a primeira opção do meu loop
    if event == sg.WIN_CLOSED:
        break
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        ao_clicar_numero(event)
    if event == '.':
        view_model['separador'] = True
    if event == '-LC-':
        limpar_view_model()
        atualizar_visor_calculadora(0.)
        view_model['result'] = 0.
    if event in ['+','-','*','/']:
        ao_clicar_operador(event)
    if event == '=':
        ao_clicar_igual()
    if event == '-POSNEG-':
        ao_clicar_positivo_negativo()

window.close()