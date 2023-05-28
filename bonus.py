import PySimpleGUI as sg
from zipcreator import make_archive

label1 = sg.Text("Select a file to compress")
input_1 = sg.Input()
choose_button1 = sg.FilesBrowse("choose", key="files")

label2 = sg.Text("Select a destination folder")
input_2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose", key="folders")
compress_button = sg.Button("compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window('File Compressor', layout=[[label1, input_1, choose_button1],
                                              [label2, input_2, choose_button2], [compress_button, output_label]])

while True:
    events, values = window.read()
    print(events, values)
    filepaths = values["files"].split(";")
    folder = values['folders']
    make_archive(filepaths, folder)
    window["output"].update(value="compression successful")

window.read()
window.close()
