def divide_nums(a,b):
    if a==0 or b==0:
        return "you can't divide by 0"
    else:
        return a/b

arg_string = input ('provide a b : ')
arg_array = arg_string.strip().split(' ')
a= int(arg_array[0])
b= int(arg_array[1])

print (divide_nums(a,b))

