from tkinter import *
import re
import requests
from tkinter import ttk

class Crypto(Frame):
    def __init__(self, name, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
        self.currencies = self.data['rates']

        self.main       = Label(self, text='KRYPTOBOI', bg='grey', fg='white', relief=RAISED, borderwidth=3)
        self.main.config(font=('Courier', 15, 'bold'))

        self.code_label = Label(self, text="Type you cyptro code: ")
        self.curr_label = Label(self, text="Type currency what you want: ")


        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.crypto_code = Entry(self, bd=3, relief=RIDGE, justify=CENTER, validate='key',
                                  validatecommand=valid)

        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD")  # default value
        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.test = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(
            self.currencies.keys()), font=font, state='readonly', width=15, justify=CENTER)

        self.check_button = Button(self, text="Convert", fg="black", command=self.perform)

        self.main.grid(row=1, column=2, padx=10, pady=10)
        self.code_label.grid(row=2, column=0, padx=10, pady=10)
        self.curr_label.grid(row=3, column=0, padx=10, pady=10)
        self.crypto_code.grid(row=2, column=1, padx=10, pady=10)
        self.check_button.grid(row=4, column=2, padx=10, pady=10)
        self.test.grid(row=3, column=1, padx=10, pady=10)



    def perform(self, ):
        code = float(self.crypto_code.get())
        currency = self.from_currency_variable.get()


        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 5)
        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))