# function can take unspecified number of variables and process it
def total(*names, **numbers):

    #iterate through all the items in tuple
    for single_item in names:
        print('TUPLE// his name is: ', single_item)

    for first_part, second_part in numbers.items():
        print('DICTIONARY// ',first_part,second_part)

print(total('tom','bob','rob', John=1, Jack=5))
