count=9
for i in range(0,10):
    print(count)
    count = count -1

for num in range(10,20):
    for i in range(2,num):
        if(num%i==0):
            j=num/i
            print(num,i,j)
            break
        else:
            print("num is a prime number")        
        
