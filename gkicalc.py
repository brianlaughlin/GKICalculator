import PySimpleGUI as sg


def calcGKI(glucose, ketone):
    return glucose / ketone

def ketoMessage(gki):
    if (gki <= 1.0 ): result = "You are in the highest therapeutic level of ketosis."
    if (gki > 1 and gki <= 3): result = "You're in a high therapeutic level of ketosis."
    if (gki > 3 and gki <= 6): result = "You're in a moderate level of ketosis.";
    if (gki > 6 and gki <= 9): result = "You're in a low level of ketosis.";
    if (gki >= 9): result = "You are NOT in ketosis.";

    return result;

layout = [[sg.Text('GKI Calculator')],
          [sg.Text('Enter your glucose')],
          [sg.InputText()],
          [sg.Text('Enter your ketone')],
          [sg.InputText()],
          [sg.Submit(), sg.Cancel()],
          [sg.Text('Your GKI is: ', size=[17, 1] , key='output')],
          [sg.Text('', size=[53, 1], key='message')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.Read()
    if event is None or event == "Exit":
        break
    glucose = float(values[0])
    ketone = float(values[1])
    result = "Your GKI is: " + str(round(calcGKI(glucose, ketone), 3))
    window.Element('output').Update(result)
    window.Element('message').Update(ketoMessage(calcGKI(glucose,ketone)))


window.Close()
