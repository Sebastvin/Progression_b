# from tkinter import *
# from tkinter import ttk
from main import *


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


class ConverterCurrencies(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.currency_converter = converter

        self.label = Label(self, text='KANTOR', bg='grey', fg='white', relief=RAISED, borderwidth=3)
        self.label.config(font=('Courier', 15, 'bold'))

        self.date_label = Label(self, text=f"Date : {self.currency_converter.data['date']}", relief=SUNKEN,
                                borderwidth=5)



        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        # restrictNumberOnly function will restrict these user to enter invalid number number in Amount field.
        # We will define it later in code
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key',
                                  validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)

        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("PLN") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # deafult value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable = self.from_currency_variable, values = list(
        self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 15, justify = tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(
        self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12,
                                                 justify = tk.CENTER)

        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))



        self.label.grid                         (row=0, column=1, padx=65, pady=5)
        self.date_label.grid                    (row=1, column=1, padx=65, pady=5)
        self.from_currency_dropdown.grid        (row=2, column=0, padx=65, pady=5)
        self.to_currency_dropdown.grid          (row=2, column=3, padx=65, pady=5)
        self.convert_button.grid                (row=2, column=1, padx=65, pady=5)
        self.amount_field.grid                  (row=3, column=0, padx=65, pady=5)
        self.converted_amount_field_label.grid  (row=3, column=3, padx=65, pady=5)




    def perform(self, ):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 5)

        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))



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