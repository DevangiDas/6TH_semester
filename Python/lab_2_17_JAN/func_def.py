the_list = ["devangi",322,False,"das",23.90]
print("values outside the function before defining:",the_list)
def my_func(list):
    list.append([3,6,4,2])
    print("values inside the function:",list)
    return
the_list = ["devangi",322,False,"das",23.90]
my_func(the_list)
print("values outside the function after defining:",the_list)
