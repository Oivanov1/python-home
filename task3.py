from random import randrange
target_number=randrange(100)
input_digit = int(input('Enter your digit: '))
    

while input_digit != target_number: 
    if input_digit>target_number:
        print ("Too mach")
    else:
        print ("Too low")
    input_digit = int(input('Enter your digit: '))

print("Nostardamus xD")
