nums = [5, 3, 6, 1, 7, 2]
nums_1=list(filter(lambda n: n % 2 == 1, nums))
#the filter function is used to filter out the elements here based on the given lambda function
# [5, 3, 1, 7] #this is what the output is 
print(nums_1)


#errors:
#in the second line we have not assigned it to a new variable so it we cannot print the new result