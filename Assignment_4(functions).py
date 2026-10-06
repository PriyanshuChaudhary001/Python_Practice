## Questions on def (Functions)
## Basic

# 1- Write a function to add two numbers.

'''def add(a,b):
    return a+b
print(add(2,3))'''

# 2- Write a function to find square of a number.

'''def sqr(num):
    return num**2
print(sqr(5))'''

# 3- Write a function to check even or odd.

'''def check_even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(6))'''

# 4- Write a function to find maximum of two numbers.

'''def maximum(n1,n2):
    if n1>n2:
        return f"n1 is maximum: {n1}"
    else:
        return f"n2 is maximum: {n2}"
print(maximum(6,4))'''

# 5- Write a function to count vowels in a string.

'''def count_vowels(string):
    count=0
    for i in string:
        if i in "AEIOUaeiou":
            count+=1
    return count
print(count_vowels("Amit"))
'''

## Medium

# 6- Write a function to check palindrome string.


'''def check_palindrome(string):
    result=""
    for i in string:
        result=i+result
    return result
string=input("Enter a string: ")
z=check_palindrome(string)
if z==string:
    print("This string is Palindrome")
else:
    print("This string is not Palindrome")'''
    
# 7- Write a function to find factorial of a number.

# By using for loop
'''num=int(input("Enter a number: "))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)'''

# By using while loop
'''num=int(input("Enter a number: "))
i=1
fac=1
while i<=num:
    fac=fac*i
    i+=1
print(fac)'''

# BY using Recursion
'''def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
num = int(input("Enter a number: "))

print("Factorial: ", fact(num))
'''

# By using function
'''def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("Enter a number: "))
print("Factorial: ",fact(num))'''

# 8- Write a function to return second largest number from a list.

# By using sort method
'''def sort_li(l):
    l.sort()

l=[2,9,7,5,4,8,10,14,25,21,22]
sort_li(l)
print(l[-2])'''

'''sort()-
            1- Modifies the original list directly.
            2- Returns None.
            3- Only works on lists.
            4- my_list.sort()'''
'''sorted() 
            1- Creates a new list:
            2- Leaves the original data unchanged.
            3- Returns the new, sorted list.
            4- Works on any iterable (lists, tuples, dictionaries, sets, strings).
            5- new_list = sorted(my_iterable)'''

# By using sorted function
'''def sort_li(l):
    return sorted(l)[-2]


l=[2,9,7,5,4,8,10,14,25,21,22]
print(sort_li(l))    '''

# by using bubble sort method
'''def sort_li(l):
    
    num=0
    for i in l:
        num+=1
    for i in range(num):
        for j in range(num-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l=[2,9,7,5,4,8,10,14,25,21,22]
sort_li(l)
print(l[-2])
'''
# 9- Write a function to remove duplicates from a list.

'''def rem_ele(l):
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2
l=[1,3,3,2,2,7,7,4,4,9,1]
l2=[]
print(rem_ele(l))'''


# 10- Write a function to calculate Fibonacci series.

# fib - 0 1 1 2 3 5 8 13 21...
'''def fib(num):
    
    a=0
    b=1
    for i in range(num):
        print(a)
        temp=a
        a=b
        b=temp+b

num=10 
fib(num)'''   

# Advanced

# 11- Write a recursive function for factorial.

'''def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("Enter a number: "))
print(fact(num))   
'''

# 12- Write a function to check prime number.

'''def check_prime(num):
    for i in range(2,num):
        if num%i!=0:
            return "Prime Number"
        else:
            return "Not Prime Number"
num=int(input("Enter a number: "))
print(check_prime(num))'''

# 13- Write a function to find GCD of two numbers.

# Divisors + Set Intersection
'''n1=12
n2=18
c1=set()
c2=set()
for i in range(1,n1+1):
    if n1%i==0:
        c1.add(i)
for j in range(1,n2+1):
    if n2%j==0:
        c2.add(j)
print(c1,c2)

print(max(c1.intersection(c2)))
'''

# Common divisor loop
'''def gcd_of_num(n1,n2):
    for i in range(1,min(n1,n2)):
        if n1%i==0 and n2%i==0:
            temp.append(i)
    gcd=0
    for i in temp:
        if i>gcd:
            gcd=i
    return gcd

n1,n2=12,18
temp=list()

n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print(gcd_of_num(n1,n2))'''

# By Euclidean Algorithm.


'''def gcd(n1,n2):
    while n2!=0:
        rem=n1 % n2
        n1=n2
        n2=rem
    return n1
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print(gcd(n1,n2))
'''
    
# Python built-in math.gcd()

'''import math 

def gcd_of_num(n1,n2):

    return math.gcd(n1,n2)
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print(gcd_of_num(n1,n2))'''

# 14- Write a function to count frequency of characters in a string.

'''def FOC(text,char):
    count=0
    for i in text:
        if i==char:
            count+=1
    return count
text=input("Enter a text: ")
char=input("Enter a char: ")

print(FOC(text,char))'''

# 15- Write a function that accepts any number of arguments and returns sum.

'''def sum_of_num(num):
    total=0
    for i in range(1,num+1):
        total=total+i
    return total

print(sum_of_num(num=int(input("Enter a number: "))))'''
 
# Questions on lambda

# 16- Write a lambda function to add two numbers.

'''Add=lambda a,b:a+b
print(Add(2,4))    ''' 

# 17- Write a lambda function to check even number.

'''check_even=lambda num: "Even" if num%2==0 else "Odd"

num=int(input("Enter a number: "))

print(check_even(num))'''

# 18- Write a lambda function to find maximum of two numbers.

# Ternary operator is a one-line way to write an if-else condition in Python.
# Ternary operator is a conditional expression used to write if-else in a single line.

'''maximum=lambda a,b: "a is max" if a>b  else "b is max" if b>a else "a is equal to b"
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print(maximum(n1,n2))'''

# 19- Write a lambda to return square of a number.

'''sqr=lambda num:num**2
num=int(input("Enter a number: "))
print(sqr(num)) 
'''

# 20- Write a lambda to return "Pass" if marks > 40 else "Fail".

'''check_pass_fail=lambda val: "Pass" if val>40 else "Fail"
marks=int(input("Enter a marks: "))
print(check_pass_fail(marks))'''

'''check_pass_fail=lambda marks: "Pass" if marks>40 else "Fail"
print(check_pass_fail(marks=45))'''

# Questions on map()

# 21- Use map() to square all elements in a list.

'''sqr=lambda val:val**2
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(sqr,l)))'''

# 22- Use map() to convert list of strings into uppercase.

'''String_up=lambda val:val.upper()
l=["aman",'priyanshu','amit','Sumit']
print(list(map(String_up,l)))'''

# 23- Use map() to convert list of strings into integers.

'''string_int=lambda val:int(val)

l=["10","12","15","17","18","21"]

print(list(map(string_int,l)))'''

# 24- Use map() to add elements of two lists.

'''add=lambda val1,val2:val1+val2
l1=[1,2,3,4]
l2=[5,6,7,8]
print(list(map(add,l1,l2)))'''  # map() can take multiple collection
    
# 25- Use map() to find length of each word in a list.

'''length=lambda val:len(val)
l=["10",'aman','sumit','prashant']
print(list(map(length,l)))  '''  
   
# Questions on filter()

# 26- Use filter() to get even numbers from a list.

'''get_even=lambda val:val%2==0

l=[1,2,3,4,5,6,7,8,9,10]

print(list(filter(get_even,l)))'''

# 27- Use filter() to get odd numbers from a list.

'''get_odd=lambda val:val%2!=0
l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(get_odd,l)))'''

# 28- Use filter() to get numbers greater than 50.

'''get_greater=lambda val: val>50

l=[22,99,88,55,23,57,50,12,13]
print(list(filter(get_greater,l)))'''

# 29- Use filter() to get words starting with vowel.

'''get_word=lambda val: val[0] in "aeiouAEIOU"

l=["sumit","amit","Prashant","Kshitiz","ilu","aman","umesh"]
print(list(filter(get_word,l)))'''

# 30- Use filter() to get prime numbers from a list.

'''
all() is a built-in Python function that returns True if all elements
in an iterable are true; otherwise, it returns False.
'''

'''get_prime=lambda val:val>2 and all(val%i!=0 for i in range(2,val))
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list(filter(get_prime,l)))'''

# Questions on reduce().

# It needs to be imported from the functools module.
'''from functools import reduce
'''
# 31- Use reduce() to find sum of elements in a list.

'''add=lambda a,b:a+b
l=[1,2,3,4,5,6,7,8,9,10]
print(reduce(add,l))'''

# 32- Use reduce() to find product of elements in a list.

'''product=lambda a,b:a*b
l=[1,2,3,4,5,6,7,8]
print(reduce(product,l))'''

# 33- Use reduce() to find maximum element in a list.

'''maximum=lambda a,b: a if a>b else b
l=[12,14,77,55,99,44,102]
print(reduce(maximum,l))'''

# 34- Use reduce() to concatenate a list of strings.

'''words=lambda a,b:a+b
l=["My"," name"," is"," Priyanshu"]
print(reduce(words,l))
'''

# 35- Use reduce() to flatten a list of lists.

'''num=lambda a,b:a+b
l=[[1,2],[3,4],[5,6]]
print(reduce(num,l))'''

# Mixed Practice Questions.

# 36- Use map() and lambda to square all numbers in a list.

'''sqr=lambda val:val**2
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(sqr,l)))'''

# 37- Use filter() and lambda to get numbers greater than 10.

'''get_num=lambda val:val>10
l=[12,3,11,10,25,16]
print(list(filter(get_num,l)))'''

# 38- Use map() and filter() to square only even numbers.

'''even=lambda val:val%2==0
l=[1,2,3,4,5,6,7,8,9,10,11,12]
even_num=list(filter(even,l))

sqr=lambda val: val**2
sqr_num=list(map(sqr,even_num))

add=lambda a,b:a+b
print(reduce(add,sqr_num))'''

# 39- Use reduce() to find factorial of a number.

'''fact=lambda a,b:a*b
num=int(input("Enter a number: "))
print(reduce(fact,range(1,num+1)))'''

# 40- From a list, remove duplicates and return only even numbers.

'''num=[1,2,1,4,4,5,5,2,6,6,7,7,3,3,3,3,3]
unique=set(num)

even=lambda val: val%2==0
print(list(filter(even,unique)))'''

