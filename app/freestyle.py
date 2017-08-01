import pandas_datareader.data as web
from datetime import date, timedelta
import datetime
import csv
import os
import matplotlib.pyplot as plt
import matplotlib

def intro():
    print("----------------------------")
    print("Stock price download Application")
    print("----------------------------")
    print("Hello "+os.getlogin())
    menu = """
    Welcome to the stock price download application!

    Please follow the steps to either calculate stock return or download/create spreadsheet for stock price!

    """
    print (menu)


def change():
    tickers=[]
    response_ticker = input("What is the ticker you would like to calculate the return?  ")
    tickers.append(str(response_ticker))
    sd = input ("What is the start date? Type in YYYYMMDD format: ")
    ed= input ("What is the end date? Type in YYYYMMDD format: ")
    datasource = "google"
    datatype = "Close"
    start = datetime.datetime(int(sd[:4]),int(sd[4:6]), int(sd[-2:]))
    end = datetime.datetime(int(ed[:4]),int(ed[4:6]), int(ed[-2:]))
    response_startprice = web.DataReader(tickers,datasource, start, start)
    response_endprice = web.DataReader(tickers,datasource, end, end)
    start_data = response_startprice.ix[str(datatype)]
    end_data = response_endprice.ix[str(datatype)]
    pct_change = (((end_data.values /start_data.values - 1))*100)[0][0]
    print ("Your stock has changed...")
    print (format(pct_change, '.2f'),"%")



def datasource():
    datasource = input("What datasource do you want to use? Choose either from 'Google' or 'Yahoo': ")
    if datasource.upper() =="GOOGLE":
        datasource = "google"
    elif datasource.upper() =="YAHOO":
        datasource = "yahoo"
    else:
        print("Please choose either from GOOGLE or YAHOO")
        datasource()
    return datasource

def create_tickerlist(tickers): #create tickers
    while True:
        ticker = input("Enter your ticker(s) when done, type 'DONE': ")
        ticker = ticker.upper()
        if ticker=="DONE":
            break
        else:
            tickers.append(str(ticker))

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
        datetype()
    return start, end

def datatype():
    datatype = input ("Specify data type. \n Choose from Open, High, Low, Close, Volume\n")
    datatype = datatype.capitalize()
    return datatype

def savecsv():
    save_csv = input("Do you want to save this data into CSV? Yes or No:")
    if save_csv.upper()=="YES":
        csv_file_path = "data/stock_price.csv"
        data.to_csv(csv_file_path)
        print ("Congratulation! Data is saved! File name 'stock_price.csv'")
    elif save_csv.upper()=="NO":
        print("We have not saved data")
    else:
        print("You have not chosen Yes nor No")


#APPLICATION below###########################
# input symbol, start date and end date
intro()

choice = input("1. Calculate simple change of a stock.\n2. Download stock price\nWhich do you choose?: ")
if choice == str(1):
    change()
elif choice == str(2):
    tickers = []
    datasource = datasource()
    create_tickerlist(tickers)
    start, end = datetype()
    datatype = datatype()
    #output
    f = web.DataReader(tickers,datasource.lower(), start, end)
    data = f.ix[str(datatype)]
    print(data)
    savecsv()
else:
    print ("You have selected neither 1 nor 2")
