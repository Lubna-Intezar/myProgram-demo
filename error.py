#.....................TASK 9.......................................................
#.....................Practical Task1(errors.py)...................................


# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


print("Welcome to the error program !")       #Missing parentheses (error_1),syntax error
print("\n")   #Missing parentheses (error_2) and (error_3)should be indented,syntax error


# Variables declaring the user's age, casting the str to an int, and printing the result
   
age_Str = "24"          #Should be indented(error_4) , we can't use logical operator(==) to assign a value (error_5)
age = int(age_Str)        
print("I'm {} year's old".format(age))  #we can't concatenate string with integer(error_6),Runtime error


# Variables declaring additional years and printing the total years of age

years_from_now = "3"             
years_now=int(years_from_now)   #We can't add string and integer value (error_7),converting string into integer
total_years = age + years_now   #Runtime Error

print("The total number of years : {} years'old".format(total_years))  # Missing parentheses,we can't contenate string with integer(error_8)


# Variable to calculate the total amount of months from the total amount of years and printing the result
#total(variable) is not declared (syntax error), correction is total_years(error_9)
#logical errors because its not showing desired output so correction is" total_months = (total_years * 12)+6 "(error_10)

total_months = (total_years * 12)+6   

print ("In 3 years and 6 months, I'll be {} months old".format(total_months))    #Missing parentheses(error_11),syntax error

#HINT, 330 months is the correct answer

