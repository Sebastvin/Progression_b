from core import *
import re
import requests

url ='https://api.exchangerate-api.com/v4/latest/USD'

class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        #first convert it into USD if it is not in USD
        # because our base currency is USD
        if from_currency != 'USD':
            amount /= self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class ConverterCurrencies(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.currency_converter = RealTimeCurrencyConverter(url)
        self.label = Label(self, text='KANTOR', bg='grey', fg='white', relief=RAISED, borderwidth=3)
        self.label.config(font=('Courier', 15, 'bold'))
        self.date_label = Label(self, text=f"Date : {self.currency_converter.data['date']}", relief=SUNKEN,
                                borderwidth=5)
        # Entry box
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        # restrictNumberOnly function will restrict these user to enter invalid number number in Amount field.
        # We will define it later in code
        self.amount_field = Entry(self, bd=3, relief=RIDGE, justify=CENTER, validate='key',
                                  validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=RIDGE,
                                                  justify=CENTER, width=17, borderwidth=3)
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("PLN")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")  # deafult value
        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(
            self.currency_converter.currencies.keys()), font=font, state='readonly', width=15, justify=CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(
            self.currency_converter.currencies.keys()), font=font, state='readonly', width=12,
                                                 justify=CENTER)
        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.label.grid(row=0, column=1, padx=65, pady=5)
        self.date_label.grid(row=1, column=1, padx=65, pady=5)
        self.from_currency_dropdown.grid(row=2, column=0, padx=65, pady=5)
        self.to_currency_dropdown.grid(row=2, column=3, padx=65, pady=5)
        self.convert_button.grid(row=2, column=1, padx=65, pady=5)
        self.amount_field.grid(row=3, column=0, padx=65, pady=5)
        self.converted_amount_field_label.grid(row=3, column=3, padx=65, pady=5)

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

