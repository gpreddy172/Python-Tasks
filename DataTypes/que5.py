A = [5,1,2,3,4,3,5]
B = [9,1,4,5,6,7,2]
print(set(A)) #changes the list to a set 
print (set(B))
print (set(A).intersection(set(B)))  #using interseciton to print the elements presents in both the sets
A = [6, 2,7,6,5,4,1]
print (set(A).intersection(set(B)))
print (set(A).difference(set(B)))
C = (5,4)*10 #prints the tuple 10 times
print (C)



# the output will be a syntax error with the first letter of Print function being capital
# the letter b of the set should be captial as declared in the set function
# in place of differences there should be difference 
# you cant subtract two lists in python using - operator 
#after assigning a value to a tuple you can't change it 
