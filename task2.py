import math
arg_string = input ('provide a b c with space beetween:')
arg_array = arg_string.split(' ')
a= int(arg_array[0])
b= int(arg_array[1])
c= int(arg_array[2])
if (a+b>c and b+c>a and c+a>b):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print ("area is: ", area)
else: 
    print ('It is not a triangle!')


