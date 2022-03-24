from tkinter import *
import re
import requests
from tkinter import ttk
import csv
import numpy as np

url = 'https://api.exchangerate-api.com/v4/latest/USD'


class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD
        # because our base currency is USD
        if from_currency != 'USD':
            amount /= self.currencies[from_currency]

        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class ConverterCurrencies(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.configure(bg='white')
        font = ("Courier", 12, "bold")
        self.currency_converter = RealTimeCurrencyConverter(url)

        fonty = ('Courier', 15, 'bold')
        self.title = Label(self, text="Currency Converter", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                           font=fonty)
        self.title.place(x=300, y=10)

        self.date = Label(self, text=f"Date : {self.currency_converter.data['date']}", relief=SUNKEN, borderwidth=5)
        self.date.place(x=360, y=50)

        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.place(x=385, y=100)

        valid = (self.register(self.restrictNumberOnly), '%d', '%P')

        # put values and see results fields
        self.amount_field = Entry(self, bd=3, relief=RIDGE, justify=CENTER, validate='key', validatecommand=valid)
        self.amount_field.place(x=80, y=150)

        self.converted_field = Label(self, text='', fg='black', bg='white', relief=RIDGE, justify=CENTER, width=17,
                                     borderwidth=3)
        self.converted_field.place(x=600, y=150)

        # default values for buttons
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("PLN")  # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")  # deafult value
        self.option_add('*TCombobox*Listbox.font', font)

        # full name currency labels
        with open('real_curr.csv', newline='') as f:
            reader = csv.reader(f)
            self.cr = list(reader)

        self.cr = list(np.concatenate(self.cr).flat)

        self.from_full_name = Label(self, text="Polish Zloty", fg='black', bg='white', relief=RIDGE, justify=CENTER,
                                    width=17,
                                    borderwidth=3)
        self.to_full_name = Label(self, text="United States Dollar", fg='black', bg='white', relief=RIDGE,
                                  justify=CENTER, width=17,
                                  borderwidth=3)

        self.from_full_name.place(x=600, y=180)
        self.to_full_name.place(x=80, y=180)

        # pick currency lists
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(
            self.currency_converter.currencies.keys()), font=font, state='readonly', width=15, justify=CENTER)

        self.from_currency_dropdown.place(x=580, y=100)
        self.from_currency_dropdown.bind('<<ComboboxSelected>>', self.from_select)

        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(
            self.currency_converter.currencies.keys()), font=font, state='readonly', width=15, justify=CENTER)

        self.to_currency_dropdown.place(x=60, y=100)
        self.to_currency_dropdown.bind('<<ComboboxSelected>>', self.to_select)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
        test = self.to_currency_dropdown.get()
        print(test)
        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 5)
        self.converted_field.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

    def to_select(self, event):
        selected = event.widget.get()

        self.to_full_name['text'] = self.full_name(selected)

    def from_select(self, event):
        selected = event.widget.get()

        self.from_full_name['text'] = self.full_name(selected)

    def full_name(self, str):
        return self.cr[self.cr.index(str) + 1]
