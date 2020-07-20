#!/usr/local/bin/python3
# return flat list from input list

import json

user_input = input('Enter a list with json format ...\n>')

try:
    my_list = json.loads(user_input)
except json.decoder.JSONDecodeError: 
    print('invalid json input. unable to convert inout json to list !!!')

if not isinstance(my_list, list):
    print('only list(array) are allowed !!!')
    exit(1)

def flat(input_list):
    result_list = []
    for item in input_list:
        if isinstance(item, list):
            result_list.extend(flat(item))
        else:
            result_list.append(item)
    return result_list

result = flat(my_list)
print('Input:', my_list)
print('Result:', result)
    