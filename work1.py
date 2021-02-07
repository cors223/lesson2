my_list = [3, NameError, -3, 'Python', True, 3.14]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)