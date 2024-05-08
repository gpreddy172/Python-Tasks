import unittest #mporting the unit test module 

def add(a, b): # defining the add function
    return a + b

class Testing(unittest.TestCase): #creating a class to run the unit testing 
    def test_add(self): # renaming the method to "test_add"
        self.assertEqual(add(10,5),15) #the add function is used to add the given integers 
        #the assertmethod take the added result value and compares it with the provided value that is 15 here 
