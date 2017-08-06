import pandas_datareader.data as web
import pandas as pd
from datetime import date, timedelta
import datetime
import csv
import matplotlib.pyplot as plt
import numpy as np


def intro():
    menu = """
    ---------------------------------
    Stock price download Application
    ---------------------------------

    Hello there!

    Welcome to the stock price download application!

    Please follow the steps to either calculate stock return or download/create spreadsheet for stock price!

    """
    print (menu)

def change():
    tickers=[]
    response_ticker = input("What is the ticker you would like to calculate the return?  ")
    tickers.append(str(response_ticker))
    sd = input ("What is the start date, please choose WEEKDAY? Type in YYYYMMDD format: ")
    ed= input ("What is the end date, please choose WEEKDAY? Type in YYYYMMDD format: ")
    datasource = "yahoo"
    datatype = "Adj Close"
    start = datetime.datetime(int(sd[:4]),int(sd[4:6]), int(sd[-2:]))
    end = datetime.datetime(int(ed[:4]),int(ed[4:6]), int(ed[-2:]))
    response_startprice = web.DataReader(tickers,datasource, start, start)
    response_endprice = web.DataReader(tickers,datasource, end, end)
    start_data = response_startprice.ix[str(datatype)]
    end_data = response_endprice.ix[str(datatype)]
    pct_change = (((end_data.values /start_data.values - 1))*100)[0][0]
    print (tickers[0],"'s stock price has changed...")
    print (format(pct_change, '.2f'),"%")



def datasource():
    datasource = input("What datasource do you want to use? Choose either from 'Google' or 'Yahoo': ")
    if datasource.upper() =="GOOGLE":
        datasource = "google"
    elif datasource.upper() =="YAHOO":
        datasource = "yahoo"
    else:
        print("Please choose either from GOOGLE or YAHOO")
        quit()
    return datasource

def create_tickerlist(tickers): #create tickers
    while True:
        ticker = input("Enter your ticker(s) when done, type 'DONE': ")
        ticker = ticker.upper()
        if ticker=="DONE":
            break
        else:
            tickers.append(str(ticker))
            print("You have chosen...", (tickers))

def datetype():
    datetype = input ("Specify date range.\n If you want to download most current data, type 'C'.\n If you want 'relative day' data from today, type in 'R'. \n If you want to specify 'exact date range' type in 'E'\n")
    datetype = datetype.upper()
    if datetype == "R":
        relativeday = input ("How many days do you want to go back from today? Enter number:")
        start = str(date.today() - timedelta(days=int(relativeday)))
        end = str(date.today())

    elif datetype == "C":
        start = str(date.today())
        end = str(date.today())

    elif datetype == "E":
        sd = input ("What is the start date? Type in YYYYMMDD format: ")
        ed= input ("What is the end date? Type in YYYYMMDD format: ")
        start = datetime.datetime(int(sd[:4]),int(sd[4:6]), int(sd[-2:]))
        end = datetime.datetime(int(ed[:4]),int(ed[4:6]), int(ed[-2:]))
    else:
        print ("You did not enter neither R nor E, please try again from the beginning.")
        quit()
    return start, end

def datatype():
    datatype = input ("Specify data type. \n Choose from Open, High, Low, Close, Adj Close (Yahoo Finance only), Volume\n")
    datatype = datatype.title()
    return datatype


def chart():
    create_chart = input ("Do you want to create chart for stock price? Yes or No: ")
    if create_chart.upper() == "YES":

        my_data = pd.read_csv('data/stock_price.csv',index_col = 0)
        array_data=np.array(my_data)
        my_data.plot()
        plt.show()
        plt.close()
    elif create_chart.upper()=="NO":
        print ("Ok, No chart is created!")
    else:
        print("You have not chosen Yes nor No. Good bye!")


#User Application
# input symbol, start date and end date
def run():
    intro()
    choice = input("1. Calculate simple change of a stock price.\n2. Download stock price\n\nWhich do you choose? 1 or 2: ")
    if choice == str(1):
        change()
    elif choice == str(2):
        tickers = []
        source = datasource()
        create_tickerlist(tickers)
        start, end = datetype()
        data_type = datatype()
        #output
        f = web.DataReader(tickers,source.lower(), start, end)
        data = f.ix[str(data_type)]
        print(data)
        csv_file_path = "data/stock_price.csv"
        data.to_csv(csv_file_path)
        chart()
        print ("Good Bye!")
    else:
        print ("You have selected neither 1 nor 2.\nPlease re-run the application")

if __name__ == "__main__":
    run()
