# 1.Multiply all elements in a list

number=[2,3,4]
mul=1
for i in number:
    mul*=i

print("Multiply of all elements is :",mul)


# 2.Find minimum value in a list

numbers=[8,3,5]
minimum=numbers[0]
for i in numbers:
    if minimum>i:
        minimum=i

print("Minimum number is :",minimum)


# 3.Count of odd numbers in list

numbers=[2,7,5,8]

count=0
for i in numbers:
    if i%2!=0:
        count+=1

print("count of odd in list is : ",count)

# 4.Find differnce between max and min

numbers=[4,7,2,9]
print("difference between max and min number is :",max(numbers)-min(numbers))


# 5.sum of only positive numbers

#
number=[-1,3,5,-2]
sum=0
for i in number:
    if i>0:
        sum+=i

print("sum of positive numbers in list : ",sum)


# 6.get keys with even values from dict

d={"a":2,"b":3,"c":4}
new=[]
for i in d:
    if d[i]%2==0:
        new.append(i)

print("list of keys : ",new)


# 7.invert dictionary
#
d={"x":1,"y":2}

n={}
for i,j in d.items():
   n[j]=i
print("invert of dictionary : ",n)

# 8.Check if two dictionaries are equal
#
dict_1={"x":1,"y":2}
dict_2={"u":1,"x":2}
is_true=True
if len(dict_1)!=len(dict_1):
    print("not equal")
else:
   for i in dict_1:
       if i  in dict_2 :
           if dict_1[i]!=dict_2[i]:
               is_true =False
       else:
            is_true=False
if is_true:
    print("Both dictionaries are equal!")
else:
    print("Not Equal")
#


# 9.sum of all values in dict
#
dict_1={"a":5,"b":10}
sum=0

for i in dict_1:
    sum+=dict_1[i]

print("Sum of values in dictionary is : ",sum)


dictionary={"a":8,"b":12,"c":15}
new=[]
for i in dictionary:
    if dictionary[i]>10:
        new.append(dictionary[i])

print(new)

# 11.Check if a number is positive ,negative,zero

num=-4

if num>0:
    print("Its a positive number")
elif num<0:
    print("Its a negative number ")
else:
    print("Its a zero")


# 12.Generate first 5 even number

count=0
number=1
numbers=[]
while count<5:
    if number%2==0:
        numbers.append(number)
        count+=1
    number+=1
print(numbers)


# 13.Find cube number

number=3

print(f"cube of {number} is {number**3}")


# 14.Check if a number is multiple of 7

number=21
if number%7==0:
    print("yes is multiple of 7")
else:
    print("NO,its not a multiple of 7")


# 15.Convert number to string and reverse it

number =123
rev=''
while number!=0:
    rem=number%10
    rev+=str(rem)
    number//=10

print (f"reverse of a 123 is {rev} and type is {type (rev)}")