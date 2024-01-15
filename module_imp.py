'''from module_create import Add
a=10
b=10
c=Add(a,b)
print(c)'''

user_input=input("enter a sentence")
new_list=user_input.split(" ")
for i in range(len(new_list)):
    if i % 2 == 0:
        print(new_list[i].upper())
    else:
        print(new_list[i].lower())    
#print("new_list is:",new_list)        