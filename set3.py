# 1.write a program to find average of numbers in list

number=[4,6,8]
sum_of=0
length=0
for i in number:
    sum_of+=i
    length+=1

print(f"Average of elements in number is : ",sum_of/length)


# 2.Write a program to count how many times a number appears in a list

number=[1,2,2,3,2]
target=2
count=0
for i in number:
    if i==target:
        count+=1

print(f"count of {target}  is {count}")

# 3.Write a program to get numbers greater than 5 in list

number=[2,5,7,8]
new=[]
for i in number :
    if i>5:
        new.append(i)

print("list of element which are greater than 5 is : ",new)


# 4.write a program to replace all 0s with 1 s in a list

numbers=[0,1,0,2]

for i in numbers:
    if i==0:
        numbers[numbers.index(i)]=1
print(numbers)


# 5.write a program to print a list in reverse order

numbers=[1,2,3]
new=[]
for i in range(len(numbers)-1,-1,-1):
    new.append(numbers[i])

print("Reverse of given list is : ",new)


# 6.write a program to merge two dictionaries

d_1={"a":1}
d_2={"b":2}


for i in d_2:
    d_1.setdefault(i,d_2[i])

print("Merge of two dict is :" ,d_1)


# 7.write a program to create a dictionary from two lists


keys=["a","b"]
values=[1,2]
dicti={}
for i in  range(len(keys)):
    dicti[keys[i]]=values[i]

print("dictionary for m two lists : ",dicti)

# 8.write a program to print all values from a dictionary

dictionary={"a":5,"y":10}
values=[]
for i in dictionary:
    values.append(dictionary[i])

print("Values of dictionary is : ",values)

# 9.Write a program to get the length of dictionary

d={'a': 10, 'b': 20, 'c': 30}
length=0
for i in d:
    length+=1

print("Length of a dictionary is : ",length)


# 10.Write program to  list  all items in dictionary as tuples
d= {'a': 1, 'b': 2}
new=[]

for i in d:
    new.append((i,d[i]))

print("Items of dictionary as tuple : ",new)


# 11.Write a program to find the square of a number

number=6
print ("Square of a {} is {}".format(number,number**2))

# 12.write a program to find sum of digits of number

number=123
sum_of=0
while number!=0:
    rem=number%10
    sum_of+=rem
    number//=10

print("Sum of all digits in a number is : ",sum_of)


# 13.write a program to find the smallest divisor of a number greater than  1

number=15

for i in range(1,number+1):
    if i!=1:
       if number%i==0:
           print ("smallest divisor is ",i)
           break



# 14.write a program to print multiplication table of a number up to 10


number=3
i=1
while i<=10:
    print(f"{number}x{i} ={number*i}")
    i+=1

# 15.write a program to count a number of even digits in a number

number=2481
count=0
while number!=0:
    rem =number%10
    if rem%2==0:
        count+=1
    number//=10

print("count of even numbers in a number is : ",count)