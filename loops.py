

row = int(input("enter number of rows"))

for i in range(row):
    for j in range(i+1):
        print(j+1, end= " ")
    print()




rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()




#break statement

my_list = [1,2,3,4,5,6]
count = 1
for i in my_list:
    if i == 6:
        print("item found")
        break
    count +=1

print("found at location", count)




for x in range(6):
    if x==4: break
    print(x)
else:
    print("finally finished")

x = 41

if x > 10:
    print("above ten, ")
    if x> 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


i = 1
while i < 6:
    print(i)
    i += 1

a = 39
b = 36
if b > a:
    print("b is greater than a")
elif a == b:
    print("b is equal to a")
else:
    print("b is less than a ")


i = 1
while i < 6:
    print(i)
    i += 1
else:
    ("i is no longer less than 6")


i = 0
while i < 6:
    i+=1
    if i ==4:
        continue
    print(i)





a = 200
b = 33
c = 500
if a > b and c > b:
    print("both conditios are true")





d ={1: "ram", 2: "krishna", 3: "sita", 4:"radha"}
for i,j in d.items():   #keys=1,2,3,4
    print(i,j)          #values = a,b,c,d





n = int(input("gie n valur: "))
i = 1
while i<=10:
    print(f"{n} * {i} = {n*i}")
    i+=1


n = int(input("given n value"))
i = 1
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")



n = int(input("give n value: "))
i = 1
while i <=n:
    if not( i % 2 == 0):
        print(i)
    i += 1


candy = 10

for i in range(0, candy):
    print("giving a candy to friend")








candies= 10

while candies > 0:
    print("given to friend")
    candies -=1