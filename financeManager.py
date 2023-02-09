import csv 
import gspread
import time 

month = 'january'

file = f"Affinity_{month}.csv"

transactions = []


def AffinityFin(file):
    with open(file, mode='r') as csv_file: 
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            Date = row[0]
            Description = row[1]
            Amount = row[4]
            Category = 'other'
            if 'To Share 0200' in Description:
                Category = 'Bill'
            if 'TMOBILE' in Description:
                Category = 'Bill'
            if 'LIFETIME' in Description:
                Category = 'Gym'
            if '-' not in Amount:
                Category = 'Income'
            transaction = (Date, Description, Amount, Category)
            transactions.append(transaction)
            print(transactions)
        return transactions
        
        

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{month}")

rows = AffinityFin(file)

for row in rows: 
    wks.insert_row([row[0], row[1], row[2], row[3]], 8)
    print('data pushed')
    time.sleep(2)

