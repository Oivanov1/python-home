def string_filter(input_string,input_length):
    result=[]
    text=input_string.split(' ')
    for x in text:
        if len(x)>input_length:
            result.append(x)
    return result


arg_string = input ('provide strin:')
arg_length = int(input('provide length:'))

print (string_filter(arg_string,arg_length))

