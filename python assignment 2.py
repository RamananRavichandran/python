
n=int(input("Enter the number of students"))
roll=[]
marks=[]
m=""
dict={}
for i in range(0,n):
    r=input("Enter the roll number")
    roll.append(r)
    r1=input("Enter the student name")
    r2=input("Enter the class name")
    s=int(input("Enter the number of subjects"))
    marks.append([])
    for j in range(0,s):
        m=input("Enter the mark for subject:")
        marks[i].append(m)
    dict[roll[i]]={"name":r1,"classname":r2,"mark":marks[i]}

print(dict)

#2nd question

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#add key and value
inventory["pocket"]=['seashell','strange berry','lint']

#sort the dict of key 'backpack'
print(sorted(inventory['backpack']))
print(inventory)

#remove dagger
inventory['backpack'].remove('dagger')
print(inventory['backpack'])

#add 50 to value of gold
inventory['gold']=inventory['gold']+50
print(inventory['gold'])

#2nd question part b

dict={'ramanan':[99,100,98],'logi':[94,90,89]}
avgdict={}
def sum(marks):
    sum=0
    for i in marks:
        sum+=i
    return sum


for k,v in dict.items():
    avgdict[k] = sum(v) / (len(v))
print(avgdict)

#2rd question part c

import re
sum=0
f=open("marks.txt","w+")
f.writelines("science = 50,maths = 90,english = 85,tamil = 92")
f.close()
f=open("marks.txt","r+")
str=f.readlines()
for i in str:
    str1=re.findall(r'[0-9]+',i)
str1=map(int,str1)
for i in str1:
    sum+=i
print(sum)
f.close()

#calculator

def add(a,b):
    try:
        sum=a+b
        return sum
    except Exception as e:
        print(e)
def sub(a,b):
    try:
        c=a-b
        return c
    except Exception as e:
        print(e)
def mul(a,b):
    try:
        m=a*b
        return m
    except Exception as e:
        print(e)
def div(a,b):
    try:
        d=a/b
        return d
    except Exception as e:
        print(e)
try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=int(input("1.Addition\n 2.Subtraction \n 3.Multiplication \n 4.Division"))
    if c==1:
        d=add(a,b)
        print("Sum :",d)
    elif c==2:
        d1=sub(a,b)
        print("Sub :",d1)
    elif c==3:
        d2=mul(a,b)
        print("Mul :",d2)
    elif c==4:
        d3=div(a,b)
        print("Div :",d3)
except Exception as e:
    print(e)

#concatenation of 2 inputs in function

def conc(a,b):
    c=a+b
    return c
a=input("Enter the first word")
b=input("Enter the second word")
c=conc(a,b)
print(c)

#  write a python script having functions defined to perfrom - sum_digits(1738)
# output should be 1+7+3+8 = 18

def sum_digit(n):
    sum=0
    while n!=0:
        sum=sum+int(n%10)
        n=int(n/10)
    return sum

n=int(input("Enter the input:"))
sum=sum_digit(n)
print(sum)

#read and write using function

import re
def write_file():
    f=open("marks1.txt","w+")
    f.writelines("science = 50,maths = 90,english = 85,tamil = 92")
    print("File successfully written")
    f.close()
def read_file():
    sum=0
    f=open("marks1.txt","r+")
    str = f.readlines()
    for i in str:
        str1 = re.findall(r'[0-9]+', i)
    str1 = map(int, str1)
    for i in str1:
        sum += i
    print("Total:",sum)
    print("File successfully read")
    f.close()
try:
    n=int(input("To read press 1 :\nTo Write press 2 :\nTo stop press 0:"))
    while n!=0:
        if n==1:
            read_file()
        elif n==2:
            write_file()
        else:
            print("Invalid input")
        n=int(input("To read press 1 :\nTo Write press 2 :\nTo stop press 0:"))
except Exception as e:
    print(e)










