import tkinter as tk
from typing import List
import re


class Calcu:
    def __init__(
        self,
        root: tk.Tk,
        label: tk.Label,
        display: tk.Entry,
        buttons: List[List[tk.Button]]
     ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

    def start(self):
        self._config_buttons()
        self._config_display()
        self.root.mainloop()

    def _config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']

                if button_text == '«':
                    button.bind('<Button-1>', self.clear)

                if button_text in '0123456789.+-÷*)(^':
                    button.bind('<Button-1>', self.add_text_to_display)

                if button_text == '=':
                    button.bind('<Button-1>', self.calculate)

    def _config_display(self):
        fixed_text = self._fix_text(self.display.get())


    def _fix_text(self, text):
        # substitui tudo que não for 0123456789./*-+^
        text = re.sub(r'[^\d\.\÷\*\-\+\^\(\)e]', r'', text, 0)
        # Substitui sinais repetidos para apenas um sinal
        text = re.sub(r'([\.\+\÷\-\*\^])\1+', r'\1', text, 0)
        # Substitui () *() para nada
        text = re.sub(r'\*?\(\)', '', text)
        return text

    def clear(self, evento=None):
        self.display.delete(0, 'end')

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])

    def calculate(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)
        try:
            ...
        except OverflowError:
            self.label.config(text='Não consegui realizar essa conta')
        except Exception as erro:
            print(f'Esse foi o erro {erro}')
            self.label.config(text='Conta inválida')

    def _get_equations(self, text):
        return re.split(r'\^', text, 0)