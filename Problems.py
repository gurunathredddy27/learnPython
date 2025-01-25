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


#sum of ARRAY

def sum(arr):
    sum = 0

    for i in arr:
        sum = sum + i

        return (sum)
if __name__ == "__main__":
    arr = [12, 3, 4, 15]
    n = len(arr)
    ans = sum(arr)
    print("sum of the array is ", ans)



#BUBBLE SORT IN PYTHON
def bubble_sort(arr):
     n = len(arr)

     for i in range(n):
         for j in range(0, n-i-1):
             if arr[j]> arr[j+1]:
                 arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    sample_list =[63,34,23,12,22,11,90]

    print("original list:", sample_list)

    bubble_sort(sample_list)
    print("sorted list:", sample_list)



#CALENDER
import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

print(calendar.month(yy, mm))



#NUMBER IS POSITIVE OR NEGATIVE

def CheckNumber(n):
    if n>0:
        print("It is positive")
    elif n<0:
        print("It is Negative")
    else:
        print("give valid number not zero")

n = int(input("Enter number: "))
CheckNumber(n)


#EVEN OR ODD
num = int(input("enter a Number: "))
if (num%2) == 0:
    print("the number is even")
else:
    print("the number is odd")




#CHECK THE NUMBER IS PRIME NUMBER
def primecheck(a):
    if a>1:
        for i in range(2,int(a/2)+1):
            if(a%i) == 0:
                print(a, "is not a prime number")
                break
        else:
            print(a, "is a prime number")
    else:
        print(a, "is not a prime number")

a = int(input("Enter an imput number: "))

primecheck(a)
#AREA OF TRIANGLE

height = float(input("enter height: "))
base = float(input("enter base"))
area = (1/2) *base *height

print("the area of the triange is ", area)


#MILES TO KM 1mile is 1.6km

km = float(input("enter km: "))
miles = km * 0.621371

print(km, " km in miles ", miles)


#LEAP year

year = int(input("enter a year: "))

if (year % 400 ==0) and (year % 100== 0):
    print(year, "is a learp year")
elif(year % 4 ==0 ) and (year % 100 != 0):
    print((year, " is a leap year"))
else:
   print(year, " is not a leap year")

#RANDOM NUMBER

import random
print(random.randint(1,9))

#SWAP TWO NUMBER

x = 5
y = 10

temp = x
x = y
y = temp

print('the value of x after swaping: {}'.format(x))
print('the value of x after swaping: {}'.format(y))


#FIND THE LARGEST NUMBER
num1 = int(input("enter number1: "))
num2 = int(input("enter numebr2: "))
num3 = int(input("enter number3: "))

if(num1>= num2) and (num1 >= num3):
    print(num1, " largest")
elif(num2 >= num1) and (num2>= num3):
    print(num2, " largest")
else:
    print(num3, " largest")

#FACTORIAL

num = int(input("enter a number: "))

factorial = 1
if num > 0:
    for i in range(1, num+1):
        factorial = factorial * i
print("the factorial of number is ", factorial)

#TABLE

num = int(input("enter number: "))
for i in range(1,11):
    print(num, "*", i, "=",num*i)

#FIBOBACCI SEQUENCE

a = 0
b = 1
num = int(input("enter number mowa: "))

for i in range (1, num+1):
     c = a+b
     a = b
     b = c
     print(c)


#FIND SUM OF NATURAL NUMBERS

num = int(input("enter a number: "))

sum = 0
while num > 0:
    sum = sum + num
    num = num -1
print(sum)


import calendar

year = int(input("select year"))
month = int(input("select month"))
cal = calendar.month(year, month)
print(cal)

#ADD 3DIGIT NUMBER

num = int(input("enter only 3digit number: "))
while num > 999 or num <99:
    print("choose 3digit number only")
    break
else:
    print("you choose correct number:)")

ALPHABET ORDER

a = "Harry Potter and the Goblet of Fire"
w = a.split()
#print(w)
for i in range (len(w)):
    w[i] = w[i].lower()

#print(w)
w.sort()
#print(w)

for i in w:
    print(i)

#PATTERNS

row = int(input('enter number of rows mama: '))

for i in range(row):
    for j in range(i+1):
        print(j+1, end= " ")
    print()


using multiple inputs

a,b,c = input("Enter three number: ").split()
print("the adddition of the numbers is: ")
print(int(a)+int(b)+int(c))


palindrom

text = input("enter: ")
text_repl = text.replace(" ", "").lower()

if text == text_repl[::-1]:
    print("palindrome")
else:
    print("not palindrome")


data = input("enter name: ")
res = data.replace("a", "*", 5)
print(res)