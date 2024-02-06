import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

df=pd.read_csv('sales.csv')
print(df.head())
sales_data_dict = df.set_index("month")["sales"].to_dict() #Create a dictionary with month as key and sales amount as value
print("Sales data dictionary:", sales_data_dict)
total_sales = df["sales"].sum()# Calculate the total sales across all months
print("Total sales across all months:", total_sales)# Print the total sales

df["Change"] = df["sales"].pct_change() * 100    # This method calculates the percentage change between the current and previous element in the 'sales' column. It computes the percentage change as (current - previous) / previous.
#print(df) 

average_sales = df["sales"].mean()  #Calculate the average sales across all months
print("Average sales across all months:", average_sales)# Print the average sales

highest_sales_month = df["sales"].idxmax()#Find the month with the highest sales
lowest_sales_month = df["sales"].idxmin()# Find the month with the lowest sales
print("The month with minimum sales: ",lowest_sales_month)
print("Month with highest sales:", highest_sales_month)# Print the results
print("Month with lowest sales:", lowest_sales_month)

plt.bar(df['month'], df['sales'], color='skyblue', edgecolor='black')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales by Month')
plt.show()