# first question
'''
s=input("Enter the sequence")
sb=input("enter the substring")
results = 0
sub_len = len(sb)
for i in range(len(s)):
    if s[i:i+sub_len] == sb:
        results += 1
print(results)
'''
#second question
'''
mat=[[3,8,7],[8,7,9],[1,6,0]]
first = 0
second = 0
for i in range(0, 3):
    for j in range(0, 3):
        if (i == j):
            first += mat[i][j]

        if ((i + j) == 2):
            second += mat[i][j]

print("1st Diagonal:", first)
print("2nd Diagonal:", second)
'''
#third question
'''
mat=[[3,8,7],[8,7,9],[1,6,0]]
transpose=[]
col1=[]
col2=[]
col3=[]
for i in range(0,3):
    for j in range(0,3):
        if i==0:
            col1=mat[i][j]
        elif i==1:
            col2=mat[i][j]
        elif i==2:
            col3=mat[i][j]
transpose=[col1,col2,col3]
print(mat)
print(transpose)
'''
'''
mat=[[3,8,7],[8,7,9],[1,6,0]]
transpose=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        transpose[j][i] = mat[i][j]
print(mat)
print(transpose)
'''
#fourth question
'''
s=''
s1=''
count=0
for i in range(0,1111):
    s=s+'abc'
s1='ca'
for i in range(len(s)):
    if s[i:i+len(s1)]==s1:
        count+=1
print("The number of occurances of word ca is ",count)
'''
#fifth question
'''
word=input("Enter the word")
list=[]
word1=""
for i in range(len(word)):
    list+=word[i]
for i in range(len(word)):
    if word[i].isupper():
        list[i]=word[i].lower()
    elif word[i].islower():
        list[i]=word[i].upper()
for i in list:
    word1=word1+i
print(word1)
'''

#sixth question

word=input("Enter the sequence:")
alpha="abcdefghijklmnopqrstuvwxyx"
alphalist=[]
substr=""
for i in range(len(alpha)):
    alphalist+=alpha[i]
for i in range(len(word)):
    if word[i]==alphalist[i]:
        count+=1
        substr=substr+word[i]
        continue
    else
        break

#seventh question
'''
sum=0
for i in range(0,1000):
    if i%3==0 and i%5==0:
        sum=sum+i
print(sum)
'''
#eighth question
'''
num=input("Enter the phone number")
numlist=[]
num1=""
for i in range(len(num)):
    if i==3:
        numlist+='-'
        numlist+=num[i]
    elif i==6:
        numlist+='-'
        numlist += num[i]
    else:
        numlist+=num[i]
for i in numlist:
    num1+=i
print("before sorting",num1)
numlist1=numlist[0:len(numlist)-4:]
rev=num1[::-1]
num2=""
list1=[]
for i in range(len(rev)):
    if i<4:
        list1+=rev[i]
    elif i==4:
        list1.sort()
    else:
        continue
numlist1+=list1
for i in numlist1:
    num2+=i
print("after sorting",num2)
'''
#ninth question
'''
import re
str1="There are 26 alphabets in English out of which 5 are vowels and 21 are consonants"
sum=sum(map(int,re.findall('\d+',str1)))
print("The sum of numbers :",sum)
'''
#tenth question
'''
str=input("Enter a word:")
str1=input("Enter another word:")

if sorted(str)==sorted(str1):
    print("The 2 words are anagrams")
else:
    print("The 2 words are not anagrams")
'''
#eleventh question
'''
n=int(input("Enter the number:"))
dict={}
for i in range(0,n+1):
    dict[i]=i*i*i
print(dict)
'''

#twelvth question

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")









