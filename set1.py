# 1.Sum of elements in a list

numbers=[4,7,2]
sum=0
for i in numbers:
    sum+=i
print("sum of elements in a list is : ",sum)


# 2.Find the largest number in list

number=[3,10,6]

max_num=number[0]

for i in number:
    if max_num <i:
        max_num=i

print("Maximum number in a list is :",max_num)


# 3.count the even numbers in a list

number=[1,2,3,4,5]

count_even=0
for i in number:
    if i%2==0:
        count_even+=1

print("number of even number present in the list is : ",count_even)

# 4.remove duplicates from list

number=[1,2,2,3,1]
new=[]
for i in number:
    if i not in new:
        new.append(i)
print("new list : ",new)

# 5.Find the second largest number

number=[5,1,9,6]

print("largest second number is :",sorted(number)[-2])

# 6.Count word occurences in a sentence

fruits="apple banana apple"
new=fruits.split(" ")
new_fruits={}

for i in new:
    new_fruits.setdefault(i,new.count(i))
print(new_fruits)


# 7.update value of key in dictionary

d_y={"a":1,"b":2}
d_y["a"]=10
print(d_y)

# 8.check id key exists in dictionary

dict_y={"x",5}

if "x" in dict_y:
    print("True")
else:
    print("False")


# 9.Print only dictionary keys

d_tionary={"name":"Ava","age":21}

keys=[]
for i in d_tionary:
    keys.append(i)

print(keys)

# 10.Add new key-value if key doesn't exist

d={"x":1}
d.setdefault("y",2)
print(d)


# 11.Check if a number is even or odd

number=9
if number%2==0:
  print("its an even number ")
else:
    print("its an odd number")

# 12.Find factorial of a number

num=5
fact=1
for i in range(1,num+1):
    fact*=i

print(f"Factorial of {num} is {fact}")

# 13.Check if a number is prime

number=7
fact=0
for i in range(2,number):
    if number%i==0:
        fact+=1
if fact==0:
    print("its a prime number ")
else:
    print("Its not a prime number")

# 14.Reverse digits of number

number=1234
temp=number
rev=""
while number!=0:
    rem=number%10
    rev+=str(rem)
    number//=10

print(f"Reverse of {temp} is {rev}" )

# 15.Count digits in a number
number=789
count=0

while number!=0:
    number//=10
    count+=1

print("count of digits in a  number is :",count)