from converter import *
from crypto import *
from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.notebook = ttk.Notebook()
        self.geometry("800x500")
        self.add_tab()
        self.notebook.grid(row = 0)
        self.notebook.grid(row = 1, column = 0, sticky = W, pady = 2)

    def add_tab(self):
        tab = ConverterCurrencies(self.notebook)
        tab2 = Crypto(self.notebook)
        self.notebook.add(tab, text="Converter")
        self.notebook.add(tab2, text="CRYPTO")


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    my_app = App()
    my_app.mainloop()