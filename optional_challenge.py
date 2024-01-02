#.................Task 9...........................
#.....Performing Arithematic operation..............
#..Implementation of Syntax,Logical or Runtime Error

#define function
#Compilation Error(1),colon is missing
#def Add(x,y):
def Add(x,y) 
    return x + y
def subtract(x,y):
    return x-y
def multiply(x,y):
    #logical Error(1),expecting multiplication but the ** operator is used for exponentiation in Python.
    #return x * y ,correction 
    return x ** y
def divide(x,y): 
    #Logical Error(2),because expecting division(x/y) but showing remainder(x%y) as a result .
    # return x / y 
    return x % y 

print("1:Add")
print("2:Subtraction")
print("3:multiplication")
print("4:division")

while True:
   
    try:
        #Compilation Error(2),Parentheses is missing
        choice=input("Enter your choice(1,2,3,4):" 
        
        #Runtime Error(1), choice 1 doesn't have single qoutes
        #if choice in('1','2','3','4'):
        if choice in (1,'2','3','4'):   
                    

        #Runtime Error(2)  
        #ZeroDivisionError: division by zero
        
            num1=int(input("Enter the First number: "))     
            num2=int(input("Enter the second number: "))  
               
                            
        if choice == '1' :
            print(num1," + ",num2,"=",Add(num1,num2))
        elif choice == '2':
            print(num1," - ",num2,"=",subtract(num1,num2))   
        elif choice == '3':
            print(num1," * ",num2,"=",multiply(num1,num2))   
        elif choice == '4':
            print(num1," / ",num2,"=",divide(num1,num2))
        else:
            print("invalid choice")  

    except ValueError:
           print("please:try only valid number!")    
                     
                    

    
                
                     
      
    
    
         
    
         

    
