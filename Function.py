# difference between print and return

def odd_even(num):
    """
    This function is printing the output against returning in below example. Run both the example to understand
    the difference between print and return
    """
    if type(num) == int:
        if num % 2== 0:
            print("Number is even")
            #return "Even"
        else:
            print("Number is odd")
            #return "Odd"
    else:
        return "Enter correct datatype!!"

odd_even(22)




def odd_even(num):
    """
    This function is returning the outout but while the function is called, we need to store the returned value
    and print the output. This is the difference between print and return
    """
    if type(num) == int:
        if num % 2== 0:
            #print("Number is even")
            return "Even"
        else:
            #print("Number is odd")
            return "Odd"
    else:
        return "Enter correct datatype!!"
    

#out = odd_even(22)
#print(out)