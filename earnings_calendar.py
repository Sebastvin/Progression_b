from tkinter import  *
import csv
import requests


class EarningsCalendar(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.configure(bg='black')

        fonty = ('Courier', 15, 'bold')
        font = ('Courier', 10, 'bold')

        self.title = Label(self, text="Earnings Calendar", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                          font=fonty).place(x=300, y=10)

        self.symbol = Label(self, text="SYMBOL", bg='grey', fg='white', relief=RAISED, borderwidth=3, font=font).place(
            x=0, y = 50)

        self.name = Label(self, text="NAME", bg='grey', fg='white', relief=RAISED, borderwidth=3, font=font).place(
            x=260, y = 50)

        self.reportDate = Label(self, text="REPORT DATE", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                              font=font).place(x=490, y = 50)

        self.estimate = Label(self, text="ESTIMATE", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                              font=font).place(x=610, y = 50)

        self.currency = Label(self, text="CURRENCY", bg='grey', fg='white', relief=RAISED, borderwidth=3,
                              font=font).place(x=690, y = 50)




        scrollbar = Scrollbar(self, width=35)
        scrollbar.place(x=760, y=100, height=374)

        god= ('Courier', 10, 'normal')
        mylist = Listbox(self, yscrollcommand = scrollbar.set, font=god)

        CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=demo'

        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)

        del my_list[0]



        for row in my_list:

            mylist.insert(END, "{:<5} | {:<50} | {:<13} | {:<8} | {:<10}".format(
                row[0], ' '.join(row[1].split()[:7]), row[2],row[4], row[5]))
            mylist.insert(END,
                         "------|----------------------------------------------------|---------------|----------|--------")



        scrollbar.config(command=mylist.yview)
        mylist.pack(side=LEFT, fill=BOTH, pady= 100, ipady=550, ipadx=300)

def get_len(list, long):
    tmp = ''
    for x in range(0, long - len(list)):
        tmp += '-'

    return tmp