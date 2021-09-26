from tkinter import  *
import csv
import requests


class EarningsCalendar(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        font = ('Courier', 15, 'bold')

        self.title = Label(self, text="Earnings Calendar", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                          font=font).place(x=300, y=10)

        self.symbol = Label(self, text="SYMBOL", bg='grey', fg='white', relief=RAISED, borderwidth=3, font=font).place(
            x=15, y = 50)

        self.name = Label(self, text="NAME", bg='grey', fg='white', relief=RAISED, borderwidth=3, font=font).place(
            x=100, y = 50)

        self.reportDate = Label(self, text="REPORT DATE", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                              font=font).place(x=160, y = 50)

        self.fiscalDataEnding = Label(self, text="Fiscal Data Ending ", bg='grey', fg='white', relief=RAISED,
                                      borderwidth=3,
                              font=font).place(x=300, y = 50)

        self.estimate = Label(self, text="ESTIMATE", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                              font=font).place(x=490, y = 50)

        self.currency = Label(self, text="CURRENCY", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                              font=font).place(x=500, y = 50)




        scrollbar = Scrollbar(self, width=15)
        scrollbar.pack(side=LEFT, fill=Y, pady=100)

        mylist = Listbox(self, yscrollcommand = scrollbar.set)

        CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=demo'

        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)

        del my_list[0]

        for row in my_list:
            mylist.insert(END, f"{row[0][:10]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
            mylist.insert(END, "----------------")


        scrollbar.config(command=mylist.yview)
        mylist.pack(side=LEFT, fill=BOTH, pady= 100, ipady=30, ipadx=300)







