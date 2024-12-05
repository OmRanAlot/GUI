import PySimpleGUI as sg

def function(event):
    # replace with your code
    print('You pressed', event)
    return event

def hover_effect(window, event, buttons):
    for button_key in buttons:
        if event == button_key:
            window[button_key].update(button_color=("white", "green"))
        else:
            window[button_key].update(button_color=("white", "#007BFF"))

sg.theme('Black')

layout = [[sg.Text("Enter a file to upload:", font=("Arial", 14), justification='center', size=(40, 1))],
          [sg.Input(key='-FILE-'),sg.FilesBrowse('Select')],
          [sg.Button("Upload", key="Upload")],
          [sg.Text("", size=(40, 2), key="-OUTPUT-")]]
          
layout = [[sg.Column(layout, element_justification='center')]]
window = sg.Window("Test_window", layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    elif event == 'Upload':
        print(values['-FILE-'])
        

    hover_effect(window, event, ['Upload'])

window.close()

