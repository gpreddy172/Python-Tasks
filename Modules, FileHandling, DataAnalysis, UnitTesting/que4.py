def count_char(input_str):
    #created a function and passed a argument 
    char_count = {} #this is an empty string

    for char in input_str: 
        if char in char_count:
            char_count[char] += 1
            return char_count
#using loops and conditionals 
#this checks if the character in the dictionary contains one or more string it iterates and check the other repeated characters

        else:
            char_count[char] = 1
            return char_count
#if the character appears only once then it returns only one 
        
        
input_str="Hello World" #this is the input string that will be checked by the function
print(count_char(input_str))

