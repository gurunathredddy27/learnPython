#simple Interst PTR/100

def simple_interse(p,t,r):
    print("the princple is ", p)
    print("the time is ", t)
    print("the rate of interest is ", r)

    si = (p * t * r)/100

    print("the simple_interst is ", si)
    return si

P = int(input("enter the priciple amount "))
T = int(input("enter the time period "))
R = int(input("enter the rate of interest"))
simple_interse(P,T,R)