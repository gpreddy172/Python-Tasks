#defining a function
def reverse_string(text): #creating a function with an argument 
    reversed_string = '' #creating an empty string 
    for i in range(len(text)-1, -1, -1): #using for loop to reverse the string
        reversed_string += text[i] #adding the reversed string to the empty string
    return reversed_string #returning the reversed string

#calling the function
print(reverse_string('Malla Reddy University'))


#using built-in-function 
text1="malla reddy university"
print(text1[::-1])