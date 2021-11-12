import tkinter as tk


def style_root():
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)  # com essa chamanda a janela nao vai ser redinicionada
    return root


def style_label(root):
    label = tk.Label(
        root, text='Sem conta', anchor='e', justify='right',
        background='#fff'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def style_display(root):
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justtify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', display_comtrol_a)
    return display

def displaplay_control(evento):
    pass