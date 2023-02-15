print("Hello, Python!")
counter = 100
miles = 1000.0
name="Devangi"
print(counter)
print(miles)
print(name)
print(type(miles))
print(type(name))
print(type(counter))
#arithemetic problem
sum = 10+12
print(sum)
sub = 12-2
print(sub)
multiply = 2*5
print(multiply)
div = 12/2
print(div)
#val1 = input("enter your value:")
#val2 = input("enter your value:")
#print(val1)
#print(val2)
number = int(miles)
print(number)
#llists are heterogenous group og elements
list1 = ['abcd', 786, 2.23, "john", 70.2]
tinylist =['egf',5098]
print(list1)
print(list1[0])
print(list1[1:3])
print(list1[2:])
print(tinylist*2)
print(len(list1))
print([1,2,3]+[4,5,6])
print(["Hi"]*4)
print(3 in list1)
for x in list1:
    print(x)
#for x in [1,2,3]: print(x)
#list2 = []
list1.append(2.23)
print(list1)
print(list1.count(2.23))
list2= [56,78]
list1.extend(list2)
list1.index(2.23)
list1.insert(2,"ram")
print(list1)
# rem = list1.pop(1)
# print(rem)
print(list1.pop(1))
print(list1)
list1.remove("ram")
#print(list1.remove("ram"))
#print(list1.reverse())
print(list1)
list1.reverse()
print(list1)
vowel= ['a','e','u','i','o']
#print(list1.sort())
vowel.sort()
print(vowel)

# Dictionary(key value clear) the key acts as index an dictionary can contain another dictionary
#dict{key,value}
dict = {}
dict['one'] = "this is one"
dict[2] = "This is two"
tinydict = {'name':'john','code':6734,'dept':'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(type(dict))
Dict = { 'Dict1': {'name': 'Ali', 'age': '19','code':2345,'dept':'manager'},
         'Dict2': {'name': 'Bob', 'age': '25','code':4675,'dept':'assistat'}}
#dictionary = {'name':'Devangi','code':'7896','dept':'manager'}
print(Dict)

#ques-create an employ record using dictionary after that use tuples are immutable

tuple = ('abcd', 786, 2.23, "john", 70.2)
print(tuple)
tinytuple = (123,'john')
print(tinytuple)
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple + tinytuple)
# tup = list(tuple)
# print(tup)
# tup.append('rajeev')
# print(tup)
# tuple = tuple(tup)
