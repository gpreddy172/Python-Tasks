A = {'mahesh' : 30, 'mahesh' : 59 }   #the second dictionary element overrides the first one because of the same key name
print (A)
A ['mahesh'] = 67 #adding new key to the dictionary
print (A)
A['Ramu'] = 100
print (A)
B = {'Ramu' : 37, 'Mahesh' : 25, 'Sam' : 100}
print(A.update(B)) #adds the elements of B to A
print(A)
print(B.update(A))
print (B)





#errors:
#invalid characters because the key is not in quotes and P in print function is capital
#here all the print functions first letter are capitals
#so many duplicate keys in the dictionary