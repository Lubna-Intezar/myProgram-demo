import csv

sales = []
months = []

with open('sales.csv', 'r') as csv_file:
    read_content = csv.DictReader(csv_file)
    
    for row in read_content:
        months.append(row['month'])
        sales.append(int(row['sales']))

    sales_dict = {month: sale for month, sale in zip(months, sales)}

    print(sales_dict)

    total = sum(sales)
    print("The total sale is:", total)

minimum_value = min(sales)
print("sales on", minimum_value)

maximum_value = max(sales)
print("Maximum sales value:", maximum_value)

'''import csv
import math

sales=[]
month=[]
with open('sales.csv','r') as csv_file:
        read_content=csv.DictReader(csv_file)
    
        for row in read_content:
            print(row)
        
            
            sale_int=int(row['sales'])
            sales.append(sale_int)
            sales_dict = {months: sale for months, sale in zip(month, sales)}    
            print(sales_dict)        

            #data= {'month':sales}
            #result = data.values() 
            #print("values for each month",result)
        
        total=sum(sales) 
        print("the total sale is: ",total) 
        minimum_values=min(sales)
        print(minimum_values)
        maximum_values=max(sales)
        print(maximum_values)'''










           

        
         
































'''import csv

sales = []
with open('sales.csv', 'r') as sales_csv:
    spreadsheet = csv.DictReader(sales_csv)
    for row in spreadsheet:
        sale = int(row['sales'])
        sales.append(sale)

total = sum(sales)
print('Total sales:', total)'''

'''import pandas as pd
import numpy as np

def read_data(): 
    data = [] 
    with open('sales.csv', 'r') as sales_csv: 
       spreadsheet = csv.DictReader(sales_csv) 
       for row in spreadsheet: 
             data.append(row) 
    return data 
def run(): 
    data = read_data() 
    sales = [] 
    for row in data: 
         sale = int(row['sales']) 
         sales.append(sale) 
    total = sum(sales) 
    print('Total sales: {}'.format(total)) 
    # Create a DataFrame from the sales data
    df = pd.DataFrame(data)

    # Calculate monthly changes
    df["Change"] = df["sales"].pct_change() * 100

    # Set the first value to NaN (optional)
    df["Change"].iloc[0] = np.nan

    # Format the "Change" column (optional)
    df["Change"] = df["Change"].apply("{:.2f}%".format)

    # Print the DataFrame with monthly changes
    print(df)
    
'''

