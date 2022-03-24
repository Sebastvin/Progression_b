from tkinter import *
import re
import requests
from tkinter import ttk


def get_info(real, digital):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' \
          f'{real}&to_currency=' \
          f'{digital}' \
          f'&apikey=A8NNGHYPH9FAV2HO'
    r = requests.get(url)
    data = r.json()
    return data['Realtime Currency Exchange Rate']


def restrictNumberOnly(action, string):
    regex = re.compile(r"[A-Za-z]*$")
    result = regex.match(string)
    return string == "" or (string.count('.') <= 1 and result is not None)


class Crypto(Frame):
    def __init__(self, name, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.configure(bg='white')
        font = ('Courier', 15, 'bold')

        self.real_curr_codes = ['USD', 'EUR', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD', 'CHF', 'CNY', 'PLN']
        self.digital_curr_codes = ['BTC', 'ETH', 'XLM', 'BNB', 'ADA', 'DOGE', 'XRP', 'LTC', 'BCH', 'DOT', 'BUSD']

        self.none_a = Label(self, bg='white')  # empty row 0
        self.none_b = Label(self, bg='white')  # empty row 3
        self.none_c = Label(self, bg='white')  # empty row 4

        self.title = Label(self, text='Cryptocurrencis', bg='grey', fg='white', relief=RAISED, borderwidth=3, font=font)
        self.title.place(x=300, y=10)

        self.info = Label(self, width=13, text="INFORMATION", bg='black', fg='white', relief=RAISED, borderwidth=3, \
                          font=font)
        self.info.place(x=313, y=90)

        self.data = Label(self, text="-------------------------------", relief=SUNKEN, borderwidth=5)
        self.data.place(x=313, y=130)

        self.info_label_start = Label(self, text='1 NONE cost', font=('Courier', 10, 'bold'))
        self.info_label_end = Label(self, text='', font=('Courier', 10, 'bold'))

        self.price = Label(self, text='', fg='black', bg='white', relief=RIDGE, justify=CENTER, width=17, borderwidth=3)

        self.bid_price = Label(self, text="Bid Price:", font=('Courier', 10, 'bold'))
        self.bid_price_data = Label(self, text='', fg='black', bg='white', relief=RIDGE, justify=CENTER, width=17,
                                    borderwidth=3)
        self.bid_price_end = Label(self, text="", font=('Courier', 10, 'bold'))

        self.ask_price = Label(self, text="Ask Price:", font=('Courier', 10, 'bold'))
        self.ask_price_data = Label(self, text='', fg='black', bg='white', relief=RIDGE, justify=CENTER, width=17,
                                    borderwidth=3)
        self.ask_price_end = Label(self, text="", font=('Courier', 10, 'bold'))
        self.warning_label = Label(self, bg='white',
                                   text="The program uses a free API. You can check calls only 5 times per "
                                        "minute, after this time the counter restarts. Daily limit is 500 calls.")

        self.code_label = Label(self, text="Type your cyptro code: ")
        self.curr_label = Label(self, text="Type currency what you want: ")

        self.check_button = Button(self, text="Convert", fg="black", command=self.perform)

        self.real_curr = StringVar(self)
        self.real_curr.set("USD")  # default value

        self.digital_curr = StringVar(self)
        self.digital_curr.set("BTC")  # default value

        self.real_curr_butt = ttk.Combobox(self, textvariable=self.real_curr, values=self.real_curr_codes,
                                           state='readonly', width=15, justify=CENTER)

        self.digital_curr_butt = ttk.Combobox(self, textvariable=self.digital_curr, values=self.digital_curr_codes,
                                              state='readonly', width=15, justify=CENTER)

        ################  SETTING UP ON THE GRID  #######################

        self.none_a.grid(row=1, column=0, padx=10, pady=10)
        self.none_b.grid(row=3, column=0, padx=10, pady=10)
        self.none_c.grid(row=4, column=0, padx=10, pady=10)

        self.code_label.grid(row=2, column=0, padx=10, pady=10)
        self.curr_label.grid(row=2, column=2, padx=10, pady=10)
        self.real_curr_butt.grid(row=2, column=3, padx=0, pady=10)
        self.digital_curr_butt.grid(row=2, column=1, padx=10, pady=10)
        self.check_button.grid(row=2, column=4, padx=30, pady=10)

        self.price.grid(row=5, column=1, padx=0, pady=10)
        self.info_label_start.grid(row=5, column=0, padx=0, pady=10)
        self.info_label_end.grid(row=5, column=2, padx=0, pady=10, columnspan=2)

        self.bid_price.grid(row=6, column=0, padx=10, pady=10)
        self.bid_price_data.grid(row=6, column=1, padx=10, pady=10)
        self.bid_price_end.grid(row=6, column=2, padx=0, pady=10, columnspan=2)

        self.ask_price.grid(row=7, column=0, padx=10, pady=10)
        self.ask_price_data.grid(row=7, column=1, padx=10, pady=10)
        self.ask_price_end.grid(row=7, column=2, padx=0, pady=10, columnspan=2)

        self.warning_label.grid(row=8, column=0, columnspan=4)

    def perform(self, ):
        code = self.digital_curr.get()
        currency = self.real_curr.get()
        data = get_info(code, currency)

        self.info_label_start.config(text=f"1 {data['2. From_Currency Name']} cost:")
        self.info_label_end.config(text=f"{data['4. To_Currency Name']}, ({data['3. To_Currency Code']})")

        self.data.config(text=f"Last data: {data['6. Last Refreshed']}")
        self.price.config(text=str(round(float(data['5. Exchange Rate']), 2)))

        self.bid_price_data.config(text=f"{round(float(data['8. Bid Price']), 2)}")
        self.bid_price_end.config(text=f"{data['4. To_Currency Name']}, ({data['3. To_Currency Code']})")

        self.ask_price_data.config(text=f"{round(float(data['9. Ask Price']), 2)}")
        self.ask_price_end.config(text=f"{data['4. To_Currency Name']}, ({data['3. To_Currency Code']})")
