my_list = ["geeks", "geeg", "keek", "practice", "aa"] 
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))
#the lamda function take x arguments one by one 
#reversed function reverses the given string 
#the join method joins the characters of the string 
#if the result containing string is equal to original string it prints it into a list
# printing the result
print(result) 