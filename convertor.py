import PySimpleGUI as sg


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


layout = [
    [sg.Text('Value:'), sg.Input(key='-INPUT-'), sg.Spin(['sec to min', 'lbs to kg', 'miles to km'], key='-UNIT-'), sg.Button('Convert', key='-CONVERT-')],
    [sg.Text('Result:'), sg.Text(' ', key='-OUTPUT-')]
]

window = sg.Window('Convertor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':

        input_value = values['-INPUT-']

        if is_number(input_value):
            match values['-UNIT-']:
                case 'miles to km':
                    window['-OUTPUT-'].update(f'{round(float(input_value) * 1.609344, 2)} km')
                case 'lbs to kg':
                    window['-OUTPUT-'].update(f'{round(float(input_value) * 0.45359237, 2)} kg')
                case 'sec to min':
                    window['-OUTPUT-'].update(f'{round(float(input_value) / 60, 2)} min')
        else:
            window['-OUTPUT-'].update('Please enter a number')

window.close()
