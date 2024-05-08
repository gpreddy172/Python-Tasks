#the sys.exc_info() function tells about the recently raised exception
import sys
def div(a,b):
    try:  #the try block here executes the code present 
        return a/b
    except ZeroDivisionError:   #except is used for exception handling of the ZeroDivisionError with the sys.exc.info() function
        print(sys.exc_info())
div(10,0)