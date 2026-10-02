## Basic
#1- Write a Python program to create a list of integers and print its elements.

'''l=[1,2,3,4,5,6]
for i in l:
    print(i)
'''

'''i=0   
while i<len(l):
    print(l[i])
    i+=1
'''

#2- Write a program to find the sum and average of all elements in a list.

'''l=[1,2,3,4,5]

print(sum(l))
print(sum(l)/len(l))
'''
#3- Write a program to find the largest and smallest element in a list.

l=[2,1,4,3,6,5,9,7]

'''l.sort()
print("Largest Element:",l[0])
print("Smallest Element:",l[-1])
'''

'''print("Largest Element:",max(l))
print("Smallest Element:",min(l))'''


'''a=0
for i in l:
    if i>a:
        a=i
    
print("Largest Number: ",a)'''

# 4- Write a Python program to count the number of elements in a list without using len().

'''l=[1,2,3,4,5,6]
count=0
for i in l:
    count+=1
print(count)
'''

# 5- Write a program to reverse a list without using built-in functions.

'''l=[1,2,3,4,5,6,7]
print(l[-1::-1])
'''

# 6- Write a program to check if an element exists in a list.

'''num=3
l=[1,2,3,4,5,6,7,8]

if num in l:
    print("Number is Present")
else:
    print("Number is not Present")
'''

# 7- Write a Python program to remove duplicate elements from a list.

'''l1=[1,2,2,3,5,4,4,8,8,5,1]

l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)
'''

# 8- Write a program to sort a list in ascending and descending order.

'''l=[10,7,3,9,8,5,1,4,2,6]

print(sorted(l))  
'''      

'''
l=[10,7,3,9,8,5,1,4,2,6]
l.sort()
print(l)'''

'''
l=[10,7,3,9,8,5,1,4,2,6]
l.sort(reverse=True)       
print(l) 
        '''
## Intermediate Level

# 9- Write a program to merge two lists and remove duplicates.

'''l1=[1,2,3,4,5,5,2,1]

l2=[5,2,6,6,7,8,9]

li=[]
for i in l1:
    if i not in li:
        li.append(i)
for j in l2:
    if j not in li:
        li.append(j)
print(li)'''

'''l1=[1,2,3,4,5,5,2,1]
l2=[5,2,6,6,7,8,9]

l1.extend(l2)
print(list(set(l1)))
'''

'''l1=[1,2,3,4,5,5,2,1]
l2=[5,2,6,6,7,8,9]

l3=list(set(l1+l2))
print(l3)'''

'''l1=[1,2,3,4,5,5,2,1]
l2=[5,2,6,6,7,8,9]

for i in l2:
    if i not in l1:
        l1.append(i)
print(list(set(l1)))'''

# 10- Write a program to find common elements between two lists.

'''l1=[1,2,3,4,5,5,2,1]
l2=[5,2,6,6,7,8,9]

l1,l2=set(l1),set(l2)
print(list(l1.intersection(l2)))
'''


'''l1=[1,2,3,4,5,5,2,1]
l2=[5,2,6,6,7,8,9]

l3=[]

for i in l1:
    if i in l2: 
        l3.append(i)
  
print(l3)'''

# 11- Write a program to split a list into even and odd numbers.

'''l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even=[]
odd=[]

for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even number list:",even)
print("Odd number lsit:",odd)
'''
# 12- Write a program to rotate a list by n positions.

# Right Rotation
'''l=[1,2,3,4,5,6,7,8]
print(l)
n=int(input("How many Rotation: "))

for i in range(n):
    l.insert(0,l[len(l)-1])
    l.pop(len(l)-1)
print(l)
'''
# Left Rotation
'''l=[1,2,3,4,5,6,7,8]
n=int(input("How many Rotations: "))

for i in range(n):
    l.append(l[0])
    l.pop(0)
print(l)
'''    

# 13- Write a Python program to find the second largest number in a list.

# If A list have no duplicate value
'''l=[6,2,3,4,1,9,8,10]
l.sort()
print(l[-2])'''

# If a list have duplicate values
'''l=[1,21,3,12,2,4,5,5,4,8,9,9,8]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
        
l2.sort()
print(l2[-2])'''

# 14- Write a program to flatten a nested list.

# 15- Write a program to count frequency of each element in a list.

'''l=[1,1,2,2,3,4,5,7,7,2,3,3,3,1,5,5,5]
count=0
n=int(input("Enter a number "))

for i in range(len(l)):
    if l[i]==n:
        count+=1
        
print(count)
'''

# 16-Write a program to replace all negative numbers with zero in a list.

'''l=[1,-3,5,-8,10,0,6]

for i in l:
    if i<=0:
        l.remove(i)
print(l)'''


## Advanced Level
# 17- Write a program to remove all occurrences of a given element from a list.

'''l=[1,2,2,3,3,7,7,1,9,8,9,8]

n=int(input("Enter a number: "))
'''
'''for i in range(len(l)):
    if n in l:
        l.remove(n)
    
print(l)'''

'''for i in l.copy():
    if i==n:
        l.remove(i)
print(l)

'''

#18-  Write a program to check if a list is a palindrome.

'''l=[1,2,1]
if l==l[::-1]:
    print("List is a Palindrome:")
else:
    print("List is not Palindrome:")    
'''    

'''l=[1,2,1,3]
l2=[]

for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
if l==l2:
    print("list is Palindrome") 
else:
    print("list is not Palindrome")   '''
    
# 19- Write a Python program to find missing numbers in a given list of consecutive integers.
# li = [3,4,5,7,8,9,10]



'''li = [3,4,5,7,8,9,10]
for i in range(li[0],li[-1]+1):
    if i not in li:
        print("Missing number",i)
        '''


# 20- Write a program to perform element-wise addition of two lists.
#input- li1 = [1,2,3,4]
#input- li2 = [1,2,3,4]
#output- li  = [2,4,6,8]


'''li1 = [1,2,3,4,81,9,12]
li2 = [1,2,3,4,3,1,11]
add=[]
for i in range(0,len(li1)):
    for j in range(0,len(li2)):
        if i==j:
            sum=li1[i]+li2[j]
            add.append(sum)
print(add)
'''
'''li1 = [1,2,3,4,81,9,12]
li2 = [1,2,3,4,3,1,11]
add=[]
for i in range(len(li1)):
    add.append(li1[i]+li2[i])
    
print(add)
'''    

# 21- Write a Python program to find the longest increasing subsequence in a list.
# li = [23,34,89,32,5,89,23,45,45,56,67,78,89,23,45,24]

'''li = [23,34,89,32,5,89,23,45,45,56,67,78,89,23,45,24]
longest=[]
sequence=[li[0]]
for i in range(1,len(li)):
    if li[i]>li[i-1]:
        sequence.append(li[i])
    else:
        if len(sequence)>len(longest):
            longest=sequence
        sequence=[li[i]]
print(longest)
'''        


# 22- Write a program to group elements based on frequency.
# li = [2,4,6,4,3,2,4,5,5,4,3,2,3,4,5,6,5,3]
# li = [2,2,2,3,3,3,3,etc5]


'''li = [2,4,6,4,3,2,4,5,5,4,3,2,3,4,5,6,5,3]

freq={}
for i in li:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        
group={}

for i in freq:
    if freq[i] not in group:
        
        group[freq[i]]=[]
    group[freq[i]].append(i)
print(group)
'''    

## Tuple

# 23-Write a Python program to create a tuple and print its elements.

'''t=tuple(x for x in range(1,11))
for i in t:
    print(i)'''

# 24- Write a program to find the length of a tuple.

'''
t=(1,2,3,4,5,6,7,8,9,10)
print(len(t))'''


'''t=(1,2,3,4,5,6,7,8,9,10)
count=0
for i in t:
    count+=1
    
print(count)'''

# 25- Write a program to find the maximum and minimum element in a tuple.

'''t=(4,8,1,2,9,5)
print(max(t))
print(min(t))'''

'''t=(3,4,2,7,6,1)
larg=0
for i in t:
    if larg<i:
        larg=i
print(larg)'''
        
'''t=(4,7,2,3,6,9,8,1,5)
smal=t[0]

for i in range(len(t)-1):
    if t[i]<t[i+1] :
        if t[i]<smal:
            smal=t[i]
print(smal)'''
        
'''t=(4,7,2,3,6,9,8,1,5)
smal=t[0]

for i in range(1,len(t)):
    if t[i]<smal:
            smal=t[i]
print(smal)'''
    
'''
t=(5,3,2,7,9,6)
smal=t[0]
for i in t:
    if i<smal:
        smal=t[i]
print(smal)   
'''    

# 26- Write a program to convert a tuple into a list.
    
'''t=(1,2,3,4,5,6)
print(list(t))'''

'''t=(1,2,3,4,5,6)
l=[]
for i in t:
    l.append(i)
print(l)'''

# 27- Write a program to check if an element exists in a tuple.

'''num=int(input("Enter a number: "))
t=(1,2,9,3)
if num in t:
    print("Number is exist in tuple")
else:
    print("Number is not exist in tuple")
    '''
# 28- Write a program to count occurrences of an element in a tuple.

'''t=(1,1,1,4,4,4,2,2,7,7,7)
count=0
num=int(input("Enter a number: "))
for i in t:
    if i==num:
        count+=1
if count>0:
   print(count)
else:
    print("Number is not Present") '''



'''
t=(1,2,1,1,1,3,3,3,5,2,4,6,6,7,7,9,9,9,8,8,3,4,5,6,7,8,9)

freq={}
for i in t:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
'''


## Intermediate Level.

# 29- Write a program to slice a tuple and display the result.

'''t=(1,2,3,4,5,6,7,8)
print(t[2:5])
'''

# 30- Write a program to find repeated elements in a tuple.

'''t=(1,2,3,3,1,5,6,7,7,8,9)

for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i]==t[j]:
            print(t[i])
            break
'''      

'''t=(1,1,4,5,5,8,6,4)
freq={}  
for i in t:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]>1:
        print(i)
'''


# 31- Write a program to merge two tuples.

'''t1=(1,2,3,4)
t2=(5,6,7,8)

t=(t1+t2)
print(t)
'''


# 32- Write a program to unpack elements of a tuple into variables.

'''t=(1,2,3,4)
a,b,c,d=t
print(a)
print(b)
print(c)
print(d)
'''
# 33- Write a Python program to sort a tuple.

"""t=(9,6,2,1,6,5,3,7,8)

'''sorted(): A built-in function that returns a new sorted 
list from an iterable without changing the original.'''

print(tuple(sorted(t)))  
"""


'''t=(5,3,1,6,8,9,7,2)
li=list(t)
for i in range(len(li)):
    for j in range(len(li)-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            
print(tuple(li))'''

'''t=(5,3,1,6,8,9,7,2)
li=list(t)
n=0
for i in li:
    n+=1
for i in range(n):
    for j in range(n-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            
print(tuple(li))
'''

# 34- Write a program to convert a list of tuples into a dictionary.

'''li = [(1, "A"), (2, "B"), (3, "C")]

d={}
for i in li:
   d[i[0]]=i[1]
print(d) 
'''

## Advanced Level.

# 35- Write a program to find the index of an element in a tuple.

'''t=(1,2,3,4,5,6)
print(t.index(4))'''

'''t=(1,2,3,4,5,6,7,2)

num=int(input("Enter an element: "))
count=0
found=False
for i in t:
    
    if num==i:
        print(count)
        found=True
    count+=1
if found==False:
    print("Number is not found")'''
    

# 36- Write a program to remove an element from a tuple (without directly modifying it).

'''t=(1,2,3,4,5,6,6,7)
li=[]
num=int(input("Enter an element: "))
for i in t:
    if i!=num:
        li.append(i)
print(tuple(li))'''

# 37- Write a program to find common elements between two tuples.

'''t1=(1,2,3,4,5,6)
t2=(2,3,5,8,9,7)
li=[]

for i in t1:
    if i in t2:
        
        li.append(i)
print(tuple(li))
'''            

# 38- Write a Python program to check if a tuple is a palindrome.

'''t=(1,2,1)

if t==t[::-1]:
    print("Tuple is palindrome")
else:
    print("Tuple is not palindrome")

'''

# 39- Write a program to find the element with maximum frequency in a tuple.

'''t=(1,1,1,2,2,3,5,5,6,7,8,8,8,8,8,9,99,9,9,9,9,9,3,3,3,3,3,3,3)

freq={}
for i in t:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
maximum=0
element=0

for i in freq:
    if freq[i]>maximum:
        maximum=freq[i]
        element=i
print("Element: ",element)
print("Maximum Frequency: ",maximum)

'''

# 40- Write a program to create a nested tuple and access its elements.

'''t=((1,2,3),(4,5,6))
for i in t:
    for m in i:
        print(m)'''