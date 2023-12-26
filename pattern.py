#..........TASK 8............................
#....Implementation of control statement to form Pattern.....
'''
*
**
***
****
*****
****
***
**
*
'''

#Assign a value for number of rows
num_rows = 5

#loop to generate the pattern
for i in range(1, num_rows * 2):

    #checks number of rows should be less that or equal to 5
    if i <= num_rows:

       # Print stars in increasing order
       print("*" * i)

    else:

       # Print stars in decreasing order
       print("*" * (num_rows * 2 - i))