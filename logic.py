#...................................TASK_9......................
#.......Demonstrating a logical error...........................
#Write a program to calculate the sum of even and odd numbers...

count=0
even_sum = 0
odd_sum=0

while True:

    user_input=input("please enter a number : ")
    number=int(user_input)

    
     
          
    if number == -1:
        break

    if number % 2 == 0:

        count += 1
    
        # Calculate the sum of even numbers

        even_sum += 1   #logical error
        #even_sum +=number  : correct code


    # Calculate the sum of odd numbers
    elif number % 2 != 0:
    
        odd_sum += number   

# Logical error: Displaying the total count of even numbers intead of sum of even numbers and not showing desired output.

print(f"The sum of even numbers is: {even_sum}") 
print(f"The sum of odd numbers is: {odd_sum}")   
             
#Logical Error:code should be "even += number" instead of "even += 1".     