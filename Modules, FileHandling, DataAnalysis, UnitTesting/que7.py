original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
#created a dictinary using key value pairs  
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40} 
#using conditionals to print out the values which are not equals to 0 when divided by 2 that are under 40
print(new_dict)