
# ...............TASK_12.................................
# .....Implementing list,dictionary in  a program.......
# creating menu_cafe List with four items:

menu_cafe=["coffee","sandwich","cupcake","Hot_chocolate"]

# creating dictionary for stock values:
# Assign stock values for each item:
stock_dict={"coffee":20,
            "sandwich":30,
            "cupcake":10,
            "Hot_chocolate":40}

# creating dictionary for price of item:
# Assign price for each item:

price_dict={"coffee":3.45,
            "sandwich":4.25,
            "cupcake":3.99,
            "Hot_chocolate":2.45}

# initializing total_stock:
total_stock_networth=0

# going through loop to each item:
for item in menu_cafe:
     # calculating item_value:  
    item_value=(stock_dict[item]*price_dict[item]) 

    #caculate total stock worth for these items:
    total_stock_networth+=item_value 
print("The total stock value worth is {} : ".format(total_stock_networth))