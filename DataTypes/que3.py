List1 = ['BTech', 'MTech', 'MBA', 'MCA']
List1.append('MS') #adds the MS string to List1
List2 = List1
print('List1 = ', List1) 
print('List2 = ', List2)
List2.extend('CIVIL')  #extend is used to divide the string into each seperate string 
print('List2 = ', List2)
List1.sort() #used to sort the list according to the A-Z order
print(List1)

       
       
       
       
       
       
       
       
#errors:      
#the output will be an syntax error because of the quotes are not proper and diff characters are used in place of quotes
# here in the print statement the P is capital as the python is case sensitive this should be small


