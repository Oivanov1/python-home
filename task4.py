def contains_number (input_dict,input_value):
    return input_value in input_dict.values()

input_string = input ('provide dictionary following rules for eval() : ')
Dict = eval(input_string)
input_digit = int(input ('Provide number your looking for: '))

print(contains_number (Dict,input_digit))
