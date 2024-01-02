#.............PRACTICAL TASK 11.......................................

#[Part1: Alternate Case for Character ]

# Read input from the user
user_input=input("Enter the string : ")
#Initialize empty string to store modified string:
result_chars=""
#Iterate through characters:  
for i,char in enumerate(user_input):
    # Check if the index is even  ,char converts into uppercase :
    if i % 2 == 0:
        result_chars +=char.upper()  

    #if the index is even  ,char converts into lowercase       
    else:
        result_chars +=char.lower()   

#Disply the result for character:              
                
print(result_chars)

# [ Part 2: Alternate Case for Words ]

# Split the input string into words:
words=user_input.split()
result_words=""

#Iterate through words:
for i,word in enumerate(words):

    #check if index is even or odd    
    if i % 2 == 0:
         result_words += word.upper()
    else:
        result_words += word.lower()
    result_words +="  "

#Disply the result for Words:    
print(result_words.strip())    
        



