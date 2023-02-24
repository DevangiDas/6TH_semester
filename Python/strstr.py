def strstr(s,x):
    res = s.find(x)
    return res


def strstr(s,x):
    #code here
    res=-1
    if(len(x)>len(s)):
        return res
    for i in range(0,(len(s)-len(x)+1)):
        boolean = 1
        for j in range(0,len(x)):
            if(s[i+j]!=x[j]):
                boolean = 0
        if(boolean):
            res = i
    return res   

# abcabcabcd abcd 

# ffbefbdbacbccecaceddcbcaeaebfedfcfdbeecffdbbf cb