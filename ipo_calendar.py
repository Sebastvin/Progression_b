from tkinter import *
import csv
import requests


class IPO(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.configure(bg='white')

        font = ('Courier', 15, 'bold')

        self.title = Label(self, text="IPO Calendar", relief=RAISED, bg='grey', fg='white', borderwidth=3, font=font)
        self.title.place(x=300, y=10)

        self.symbol = Label(self, text="Symbol", relief=RAISED, bg='grey', fg='white', borderwidth=3, font=font)
        self.symbol.place(x=50, y=70)

        self.name = Label(self, text="Name", relief=RAISED, bg='grey', fg='white', borderwidth=3, font=font)
        self.name.place(x=300, y=70)

        self.ipoData = Label(self, text="IPO Data", relief=RAISED, bg='grey', fg='white', borderwidth=3, font=font)
        self.ipoData.place(x=510, y=70)

        self.exchange = Label(self, text="Exchange", relief=RAISED, bg='grey', fg='white', borderwidth=3, font=font)
        self.exchange.place(x=650, y=70)

        data = get_ipo_info(self)
        tmp = 120

        for x in range(1, len(data)):
            if x <= 10:
                Label(self, text=f'{data[x][0]}', fg='black', bg='white', relief=RIDGE, justify=CENTER, width=17,
                      borderwidth=3).place(x=30, y=tmp)

                Label(self, text=f"{' '.join(data[x][1].split()[:6])}", fg='black', bg='white', relief=RIDGE,
                      justify=CENTER,
                      width=45, borderwidth=3).place(x=170, y=tmp)

                Label(self, text=f'{data[x][2]}', fg='black', bg='white', relief=RIDGE, justify=CENTER, width=17,
                      borderwidth=3).place(x=500, y=tmp)

                Label(self, text=f'{data[x][6]}', fg='black', bg='white', relief=RIDGE, justify=CENTER, width=17,
                      borderwidth=3).place(x=640, y=tmp)
                tmp += 45


def get_ipo_info(self, ):
    CSV_URL = 'https://www.alphavantage.co/query?function=IPO_CALENDAR&apikey=A8NNGHYPH9FAV2HO'
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    return my_list
