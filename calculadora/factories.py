import tkinter as tk
from typing import List


def style_root():
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=5, pady=10, background='#3A3C55')  #293241
    root.resizable(False, False)  # com essa chamanda a janela nao vai ser redinicionada
    # root.geometry('500x450')
    return root


def style_label(root):
    label = tk.Label(
        root, text='Expressão atual', anchor='e', justify='right',
        background='#4F607D'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def style_display(root):
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(2, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=0, highlightcolor='#ccc', background='#56698A'
    )
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(evento):
    evento.widget.select_range(0, 'end')
    evento.widget.icursor('end')
    evento.config(background='#EE6C4D')
    return 'brenk'


def make_buttons(root) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', '«'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '('],
        ['0', '.', '^', '=', ')'],

    ]

    buttons: List[List[tk.Button]] = []

      # estilos dos buttons
    for row, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row, column=col_index, sticky='news', padx=0.50, pady=0.50)
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=40, width=1, background='#365955', bd=0,
                cursor='hand2', highlightthickness=0,
                highlightcolor='#ccc', activeforeground='#ccc',
                highlightbackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons


