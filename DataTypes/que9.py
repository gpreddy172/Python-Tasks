A = [1,2,3,5]
A.insert(4,6)  #inserts 6 at index 4 
print(A)
A[4] = 5 
print(A)  
del A[-1] #deletes the last element 
print(A)  
del A[:1] #deletes the first element
print(A)  
A = [1,2,3,5, 10,20, 55,3]
print("Sum of items in A:", sum(A)) 
print("Max item in A:", max(A))  
print("Min item in A:", min(A))  
print("Avg item in A:", sum(A)/len(A))  

#print statements should be lowercase 
#we are tying to insert a elements in a invalid index 
#the del cannot be used with print statement 
