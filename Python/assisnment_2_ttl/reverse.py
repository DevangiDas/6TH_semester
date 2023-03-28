#Reverse words in a given String in Python
str= input("Enter the string:")
count = 0
new_str = ""
i = len(str)-1
while(i>=0):
    #print("hey")
    count = count + 1
    if(str[i]==" "):
        start = str.index(str[i])+1
        for j in range(start,count):
            new_str = new_str + str[j]
        count = 0
        new_str =  new_str + " "
    i = i- 1
print(new_str)
    