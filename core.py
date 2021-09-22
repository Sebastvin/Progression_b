from converter import *
from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.notebook = ttk.Notebook()
        self.geometry("800x500")
        self.add_tab()
        self.notebook.grid(row = 0)
        #self.notebook.grid(row = 1, column = 0, sticky = W, pady = 2)

    def add_tab(self):
        tab = ConverterCurrencies(self.notebook)
        tab2 = Tab_2(self.notebook)
        self.notebook.add(tab, text="Tag")
        self.notebook.add(tab2, text="Tag2")


class Tab_2(Frame):
    def __init__(self, name, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.label = Label(self, text="Hi This is Tab2")
        self.l = Label(self, text="XXXXXXXXXXXXXXXXXXXXXXX")

        self.label.grid(row=2, column=0, padx=10, pady=10)
        self.l.grid(row=2, column=1, padx=130, pady=10)
        self.name = name

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    my_app = App()
    my_app.mainloop()