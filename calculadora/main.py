from factories import style_root, style_display, style_label,\
    make_buttons
from cal_class import Calcu


def main():
    root = style_root()
    display = style_display(root)
    label = style_label(root)
    buttons = make_buttons(root)
    calculator = Calcu(root, label, display, buttons)
    calculator.start()


if __name__ == '__main__':
    main()