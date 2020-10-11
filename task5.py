def devide_function(a,b):
    result=[]
    for x in range(a, b):
        if (x%7==0) and (x%5!=0):
            result.append(str(x))
            
    return result

arg_string = input ('provide range:')
arg_array = arg_string.split(' ')
a= int(arg_array[0])
b= int(arg_array[1])

print (devide_function(a,b))


