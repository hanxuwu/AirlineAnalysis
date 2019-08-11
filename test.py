

num=['零','一','二','三','四','五','六','七','八','九','十']

k=['零','十','百','千','万','十','百','千','亿']



    
def turn(x,y):
    if y>=1:
        a=x//pow(10,y)
        b=x%pow(10,y)
        c=num[a]+k[y]
        if y>4 and b<pow(10,4):
            c+=k[4]
        if (len(str(x))-len(str(b)))>=2 and b!=0:
            c+=k[0]
    else:
        a=x
        b=0
        c=num[a]
    return (c,b)

def tstr(x):
    c=turn(x,(len(str(x))-1))
    a=c[0]
    b=c[1]
    while b!=0:
        a+=turn(b,len(str(b))-1)[0]
        b=turn(b,len(str(b))-1)[1]
    return a


print(tstr(111100138))
    