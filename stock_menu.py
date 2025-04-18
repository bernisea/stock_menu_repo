# -*- coding: utf-8 -*-
"""
Date: November 11 2023

Name: Bernice Antwi
"""
from datetime import datetime
from stock_class import Stock, DailyData
from account_class import Robo, Traditional
#from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import csv


def add_stock(stock_list):
      print("This method is under construction")
      #set option to “”
      option = ""
      while option != "0":
          print("Adding Stock ----")
          symbol = input('Enter Ticker Symbol: ').upper()
          name = input('Enter Company Name: ')
          shares = float(input('Enter Number of Shares: '))
          new_stock = Stock(symbol, name,shares)
          stock_list.append(new_stock)
          option = input('Stock Added - Enter to Add Another Stock or 0 to Stop: ')


# Remove stock and all daily data
def delete_stock(stock_list):
    print('Delete Stock * * *')
    print('Stock List: [ ', end='')
    for stock in stock_list:
        print(stock.symbol, ' ',end='')
    print(']')
    symbol = input('Which stock do you want to delete: ')
    found = False
    i=0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
        i = i+1
    if found == True:
        print('Deleted', symbol)
    else:
        print('Symbol not found')
    _=input('Press enter to continue')
    
  
    
    
# List stocks being tracked
def list_stocks(stock_list):
    print('Stock List ----')
    print('SYMBOL \t\t   NAME \t\t   SHARES')
    print('=======================================')
    for stock in stock_list:
        print(stock.symbol,' ' * (14-len(stock.symbol)),stock.name, ' ' * (14-len(stock.name)), stock.shares)
    print()
    _=input('Press Enter to Continue * * *')

    
    # Add Daily Stock Data
def add_stock_data(stock_list):
    print("Add Daily Stock Data ----")
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ",symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date,float(price),float(volume))
          
            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")

    
def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    date =[]
    price = []
    volume = []
    company = ''
    for stock in stock_list:
        if stock.symbol == symbol:		
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
                
    plt.plot(date, price) 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()


# Display Chart
def display_chart(stock_list):
    print('Stock chart --')
    print('Stock List: [', end='')
    for stock in stock_list:
        print(stock.symbol, ' ', end='') 
    print(']')
    symbol = input('Print stock for a chart: ').upper()
    found = False
    
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        display_stock_chart(stock_list, current_stock.symbol) 
    else:
        print('symbol not found')
        _=input('Press enter to continue')
    
    
                
 # Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")
    
   # Display Report 
def display_report(stock_list):
    print("This method is under construction")
    
def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            
            print("Goodbye")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()