#Basic datatype questions
#q1
x = 10
print(x)
#q2
name = "Alice"
print(len(name))
#q3
is_active = True
print(is_active)
#q4
a = 5
b = 3
print(a+b)
#q5
for i in range(0,5):
    print(i)
#q6
n = int(input())
if(n%2==0):
    print("Even")
else:
    print("Odd")
#q7
nums = [1,2,3,4]
print(nums[i])
#q8
s = "hello"
f = "world"
g = s + " " +f
print(g)
#q9
s1 = "123" 
s2 = int(s1)
s3 = s2 + 7
print(s3) 
#q10
sum = 0
for i in range(11):
    sum = sum + i
print(sum)
#q11
nums = [1,2,3,4]
for i in range(nums):
    if(nums[i]%2==0):
        print("Even")
    else:
        print("Odd")
#q12
score = int(input())
if(score>=90):
    print("A")
elif(score>=75):
    print("B")
elif(score>=60):
    print("C")
else:
    print("F")
#q13
x = 4
y = 5
print("Before swapping value of x : ",x)
print("Before swapping value of y:",y)
x = 5
y = 4
print("After swapping value of x:",x)
print("After swapping value of y:",y)
#q14
text = "python"
for i in range(len(text)):
    print(text[i])
#q15
items = [5,7,5,2]
print(len(items))
print(items[0])
print(items[3])
#q16
l = [1,'Ashish',4,6.7]
print(len(l))
#q17
sum = 0
n = int(input())
for i in range(n+1):
    sum = sum + i
print(sum)
#q18
s = input()
if(s==""):
    print("Its an empty string")
else:
    print("Its not an empty string")
#q21
max = l[0]
l = [1,2,3,4,5,6,7]
for i in range(len(l)):
    if(l[i]>max):
        print("Maximum")
    else:
        print("Invalid")
#q24
n = int(input())
for i in range(n,1,-1):
    print(i)
#q26
l = [1,2,4,5,6,7]
for i in range(len(l)):
    print(l[i]**2)
