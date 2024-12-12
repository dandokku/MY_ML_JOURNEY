# numerator = 10
# denominator = 0

# result = numerator / denominator #! this will return an error 


try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter Denominator: "))
    
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Denominator cannot be 0, please try again")
finally: #always executed
    print("welp")
        

'''
FileNotFound - When a file that doesn't exist is accessed
IndexError - When the index of a sequence is out of range
FloatingPointError - When a floating point operation fails
'''