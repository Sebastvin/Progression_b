from converter import *
from crypto import *
from ipo_calendar import *
from earnings_calendar import *
from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Finance Informator")
        self.notebook = ttk.Notebook()
        self.geometry("811x600")
        self.add_tab()
        self.notebook.pack()

    def add_tab(self):
        tab = ConverterCurrencies(self.notebook)
        tab2 = Crypto(self.notebook)
        tab3 = IPO(self.notebook)
        tab4 = EarningsCalendar(self.notebook)
        self.notebook.add(tab, text="Converter")
        self.notebook.add(tab2, text="CRYPTO")
        self.notebook.add(tab3, text="IPO Calendar")
        self.notebook.add(tab4, text="Earnings Calendar")


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    my_app = App()
    my_app.mainloop()