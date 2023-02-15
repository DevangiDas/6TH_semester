the_list = ["Devangi",21,False,"das",23.6]
print(the_list)
for i in the_list:
    if i:
         print("exp is true")
    else:
         print("exp is false")


another_list=["School",34,False,"house",21.9]
print(another_list)
def my_func(list):
     list_type=[]
     list_string=[]
     list_number=[]
     list_float=[]
     list_bool=[]
     list_type=[list_string,list_number,list_float,list_bool]
     ele1=type(list[0])
     print(ele1)
     for i in list:
          element=type(list[i])
          print(element)
          # print(list) 
          # if(element=)
my_func(another_list)
