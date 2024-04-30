A = [
    {"Name" : "RAMU", "Telugu" : 37, "Hindi" : 70, "English" : 65, "Math" : 87, "Science" : 81, "Social" : 99},
    {"Name": "Kiran", "Telugu" : 70, "Hindi" : 60, "English" : 89, "Math" : 76, "Science" : 71, "Social" : 92},
    {"Name": "Ventat", "Telugu" : 100, "Hindi" : 37, "English" : 39, "Math" : 56, "Science" : 31, "Social" : 42},
    {"Name": "Mahesh", "Telugu" : 37, "Hindi" : 47, "English" : 69, "Math" : 98, "Science" : 99, "Social" : 98},
    {"Name": "Akhil", "Telugu" : 58, "Hindi" : 87, "English" : 77, "Math" : 95, "Science" : 100, "Social" : 58}
]
def ascending_order(student): #defining a function having an arguments student 
    return student["Name"] #retuns the name of thr student 
sorted_A = sorted(A, key=ascending_order) #sorting the list A in ascending order
print(sorted_A)