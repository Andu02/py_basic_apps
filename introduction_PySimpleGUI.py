import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events=True, key='-TEXT-'), sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Button', key='-BUTTON1-')],
    [sg.Input(key='-INPUT-')],
    [sg.Text('Test'), sg.Button('Button', key='-BUTTON2-')]
]

window = sg.Window('Convertor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':
        window['-TEXT-'].update(visible=False)

    if event == '-BUTTON2-':
        print('something else')

    if event == '-TEXT-':
        print('text was pressed')

window.close()
