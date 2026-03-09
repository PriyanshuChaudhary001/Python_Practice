##Python IF (Single Condition)

#problem_1[Write a Python program to check if a number is positive.]
'''num=int(input("Enter the number :"))
if num>0:
    print("Number is Positive")'''
    
#problem_2[Print "Eligible to vote" if age is 18 or above.]
''''person_age=int(input("Enter the age : "))
if person_age>=18:
    print("Eligible to vote")'''
    
#problem_3[Check if a number is divisible by 7.]
'''num=int(input("Enter the number :"))
if num%7==0:
    print("Number is divisible by 7")
'''
#problem_4[Print "Pass" if marks are greater than 40.]
'''marks=int(input("Enter the marks : "))
if marks>40:
    print("Pass")'''
    
#problem_5[Check if a number is greater than 100.]
'''num=int(input("Enter the number : "))
if num>100:
    print("NUmber is greater than 100")'''
    
#problem_6[Display a message if temperature exceeds 45°C.]
'''temp = float(input("Enter temperature in °C : "))
if temp > 45:
    print("Warning! Temperature exceeds 45°C")
'''    
#problem_7[Check if a string length is more than 8 characters.]
'''text=input("Enter a string : ")
if len(text)>8:
    print("String length is more than 8 characters")
'''
#problem_8[Print "Logged In" if password matches "admin123".]
'''password=(input("Enyter a password : "))
if password=="admin123":
    print("Logged In ")'''

#problem_9[Check if a number is a multiple of 10.]
'''num = int(input("Enter a number : "))
if num % 10 == 0:
    print("Number is a multiple of 10")'''

#problem_10[Print a warning if balance is below minimum limit.]
'''balance = int(input("Enter account balance : "))
minimum_limit = 1000
if balance < minimum_limit:
    print("Warning! Balance is below minimum limit")'''

##Python IF–ELSE (Two Conditions)

#problem_11[Check whether a number is even or odd.]

'''n=int(input("Enter a number : "))

if n%2==0:
    print(f"Number is Even : {n}")    # f=formatted string
else:
    print(f"Number is odd : {n}")
    '''
#problem_12[Find the largest of two numbers.]

'''n1=int(input("Enter a first number: "))
n2=int(input("Enter a second number : "))

if n1>n2:
    print(f"largest number : {n1}")
else:
    print(f"largest number : {n2}")
'''
#problem_13[Check whether a person is eligible for driving license.]
'''
age=int(input("Enter age : "))
if age>=18:
    print("Eligible for driving license")
else:
    print("No eligible for driving license")'''

#problem_14[Print "Pass" or "Fail" based on marks.]

'''
marks=int(input("Enter marks : "))
if marks>=33:
    print("Pass")
else:
    print("Fail")
'''
#problem_15[Check whether a number is positive or negative.]

'''num=int(input("Enter a number"))

if num>=0:
    print("Positive")
else:
    print("Negative")   '''              
    
#problem_16[Check whether a character is a vowel or consonant.]

'''ch=input("Enter a character")

if ch in "AEIOUaeiou":
    print("vowel")
else:
    print("Consonant")'''
    
#problem_17[Check if a year is leap or not.]

    
'''year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
'''

#problem_18[Print "Valid Password" or "Invalid Password".]

'''password=input("Enter a password : ")

if password =="Priyanshu":
    print("Valid password")

else:
    print("Invalid password")
'''

#problem_19[Determine whether salary is taxable or not.]

'''salary=int(input("Enter your annual salary : "))

if salary<=1200000:     
    print("salary is taxable")

else:
    print("salary is not taxable")'''
    
#problem_20[Check whether a number is greater than 50 or not.]

'''num=int(input("Enter a number : "))

if num>50:
    print("number is greater than 50")
else:
    print("number is not greater than 50")
'''

##Python NESTED IF–ELSE

#problem_21[Find the largest of three numbers.]


'''
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
n3=int(input("Enter third number : "))

if n1>n2:
    if n1>n3:
        print("largest number: ",n1)
    else:
        print("largest number: ",n3)
else:
    if n2>n3:
        print("largest number: ",n2)
    else:
        print("largest number: ",n3)
'''

#problem_22[Check whether a number is positive, negative, or zero.]

'''num=int(input("Enter a number: "))

if num>0:
    print("Positive number")
else:
    if num<0:
        print("Negative number ")
    else:
        print("zero")
'''

'''
problem_23[Assign grades:
                            ● A → marks ≥ 90
                            ● B → marks ≥ 75
                            ● C → marks ≥ 60
                            ● Fail → below 60]
'''
'''
marks=float(input("Enter marks: "))

if marks>=90:
    print("Grade: A")
else:
    if marks>=75:
        print("Grade: B")
    else:
        if marks>=60:
            print("Grade: C")
        else:
            print("fail")
        '''

#problem_24[Check whether a triangle is equilateral, isosceles, or scalene.]
'''
s1=float(input("Enter side 1: "))
s2=float(input("Enter side 2: "))
s3=float(input("Enter side 3: "))

if s1==s2:
    if s2==s3:
        print("Equilateral triangle")
    else:
        print("Isosceles triangle")
else:
    if s1==s3:
        print("Isosceles triangle")
    else:
        if s2==s3:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
'''

#problem_25[Check whether a character is uppercase, lowercase, digit, or special character.]

'''ch=input("Enter a character: ")

if ch>='A' and ch<='Z':
    print("Uppercase")
else:
    if ch>='a' and ch<='z':
        print("Lowercase")
    else:
        if ch>='0' and ch <='9':
            print("Digit")
        else:
            print("Special character")
'''
        
#problem_26[Calculate electricity bill using slab-wise rates.]

#Hint: 0–100 units → ₹5 per unit , 101–200 units → ₹7 per unit and  Above 200 units → ₹10 per unit

'''

units=int(input("Enter electricity units: "))

if units<=100:
    bill=units*5
else:
    if units<=200:
        bill=(100*5)+(units-100)*7
    else:
        bill=(100*5)+(100*7)+ (units-200)*10

print(f'Total Electricity bill: {bill}')

'''

#problem_27[Validate login using username and password.]
'''
username=input("Enter username: ")
password=(input("Enter password: "))

if username=="Priyanshu":
    if password=='priya1234':
        print("Valid login")
    else:
        print("Invalid password")
else:
    print("Invalid username")'''
    
#problem_28[Check student result using marks of 3 subjects.]

'''m1=float(input("Enter maths marks: "))
m2=float(input("Enter Physics marks: "))
m3=float(input("Enter Chemistry marks: "))


if m1>=33:
    if  m2>=33:
        if m3>=33:
            print("Result: Pass")
        else:
            print("Result: Fail")
    else:
        print("Result: Fail")   
else:
    print("Result: Fail")

'''

#problem_29[Find the second largest number among three numbers.]


'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        if b > c:
            print("Second largest:", b)
        else:
            print("Second largest:", c)
    else:
        print("Second largest:", a)
else:
    if b > c:
        if a > c:
            print("Second largest:", a)
        else:
            print("Second largest:", c)
    else:
        print("Second largest:", b)
'''

#problem_30[Check loan eligibility using age, salary, and credit score.]

'''
age=int(input("Enter age: "))
salary=int(input("Enter salary: "))
credit_score=int(input("Enter credit score: "))


if age>=21 and age<=60:
    if salary>=25000:
        if credit_score>750:
            print("Loan approved")
    
        else:
            print("Low crdit score")
    else:
        print("Low salary")
else:
    print("Age not eligible")'''



##Python ELIF (Multiple Conditions)

#problem_31[Print day name using day number (1–7).]

'''
day_num=int(input("Enter day number: "))

if day_num==1:
    print("Sunday")
elif day_num==2:
    print("Monday")
elif day_num==3:
    print("Tuesday")
elif day_num==4:
    print("Wednesday")
elif day_num==5:
    print("Thursday")
elif day_num==6:
    print("Friday")
elif day_num==7:
    print("Saturday")
else:    
    print("Wrong Day number")
    '''
#problem_32[Print month name using month number.]

'''
month_num=int(input("Enter the month number(1-12): "))

if month_num==1:
    print("January")
elif month_num==2:
    print("February")
elif month_num==3:
    print("March")
elif month_num==4:
    print("April")
elif month_num==5:
    print("May")
elif month_num==6:
    print("June")
elif month_num==7:
    print("July")
elif month_num==8:
    print("August")
elif month_num==9:
    print("September")
elif month_num==10:
    print("October")
elif month_num==11:
    print("November")
elif month_num==12:
    print("December")
    
else :
    print("Invalid month number")'''
    
    
#problem_33[Display grade based on percentage.]
#Hint : Total_max_marks=500  and m1,m2,m3,m4,m5=100 .
'''

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

if m1 >= 33 and m2 >= 33 and m3 >= 33 and m4 >= 33 and m5 >= 33:
    if percentage >= 70:
        print("PASS :  Grade A")
    elif percentage >= 60:
        print("PASS :  Grade B")
    elif percentage >= 50:
        print("PASS :  Grade C")
    elif percentage >= 40:
        print("PASS :  Grade D")
    else:
        print("FAIL")
else:
    print("FAIL : One or more subjects below 33 marks ")
'''

#problem_34[Display bonus percentage based on experience years.]
#Hint: Less than 1 year → No Bonus, 1 to 3 years → 5% bonus,  3 to 5 years → 10% bonus and More than 5 years → 20% bonus. 
'''exp=int(input("Enter the experience in years: "))

if exp<1:
    print("No Bonus")
elif exp>=1 and exp<3:
    print("5% Bonus ")
    
elif exp>=3 and exp<5:
    print("10% Bonus")
else:
    print("20% Bonus")
'''    
    
#problem_35[Identify traffic signal meaning.]
'''
signal=input("Enter traffic signal color: ")


if signal=="Red": 
    print("stop")
elif signal=="Green":
    print("Go")
elif signal=="yellow":
    print("Get ready")
else:
    print("Invalid signal ")'''
    
#problem_36[Categorize temperature as Cold / Warm / Hot.]
#Hint: Below 15°C → Cold, 15°C to 30°C → Warm and Above 30°C → Hot

'''temp=float(input("Enter the temperature in °C "))

if temp <15:
    print("Cold")
elif temp <=30:
    print("Warm")

else:
    print("Hot")'''

#problem_37[Categorize employee based on salary range.]

'''salary = int(input("Enter monthly salary: "))

if salary < 20000:
    print("Low Income")
elif salary <= 50000:
    print("Middle Income")
else:
    print("High Income")
    
'''

#problem_38[Print discount percentage based on purchase amount.]

'''amount = int(input("Enter purchase amount: "))

if amount < 1000:
    print("Discount: 0%")
elif amount < 5000:
    print("Discount: 5%")
elif amount < 10000:
    print("Discount: 10%")
else:
    print("Discount: 20%")
'''
#problem_39[Identify number type: single-digit / double-digit / multi-digit.]

'''num = int(input("Enter a number: "))

if num >= -9 and num <= 9:
    print("Single-digit number")
elif num >= -99 and num <= 99:
    print("Double-digit number")
else:
    print("Multi-digit number")
'''

#problem_40[Assign performance rating: Poor / Average / Good / Excellent.]

'''score = int(input("Enter performance score: "))

if score < 40:
    print("Poor")
elif score < 60:
    print("Average")
elif score < 80:
    print("Good")
else:
    print("Excellent")
'''

##Python COMPLEX CONDITIONS (AND / OR / NOT)

#problem_41[Check whether a number is divisible by 5 and 11.]
'''
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11")
else:
    print("Number is not divisible by both 5 and 11")
'''

#problem_42[Check if a person is eligible for loan:]
#HINT: age ≥ 21, salary ≥ 25,000 and credit score ≥ 700

'''age=int(input("Enter age: "))
salary=int(input("Enter salary: "))
credit_score=int(input("Enter credit score: "))

if age>=21 and salary>=25000 and credit_score>=700:
    print("Person is eligible for loan")
else:
    print("Person is not eligible for loan")
    
'''

#problem_43[Validate login using username AND password.]
'''
username =input("Enter username: ")
password=input("Enter password: ")

if username=="Aman" and password=="Aman@123":
    print("Login successful")
    
elif username!="Aman" and password!="Aman@123":
    print("In valid username and password")
elif username!="Aman":
    print("Invalid username")
else:
    print("In valid password")'''
    
#problem_44[Check student pass condition: All subjects ≥ 40 and  Average ≥ 50]
'''
m1=int(input("Enter marks sub1: "))

m2=int(input("Enter marks sub2: "))

m3=int(input("Enter marks sub3: "))

m4=int(input("Enter marks sub4: "))

m5=int(input("Enter marks sub5: "))


total=m1+m2+m3+m4+m5
average=total/5

if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40 and average>=50:
    print("Studdent: PAss")
    
else: print("Student: Fail")
    '''
    
#problem_45[Check if a number lies between 10 and 100.]

'''num=int(input("Enter number: "))

if num>10 and num<100:
    print("Number is lies between 10 and 100")

else:
    print("Number is not lies between 10 and 100")
    
'''

#problem_46[Check exam eligibility: attendance ≥ 75% OR , medical certificate available]

'''
attendance=int(input("Enter attendance Percentage: "))
medical=input("MEdical certificate available (yes/no): ")


if attendance>=75 or medical=="yes":
    print("Eligible for exam ")
else:
    print("Not eligible for exam")'''
    
#problem_47[Validate a date using conditions.]



'''day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year <= 0:
    print("Invalid year")

elif month < 1 or month > 12:
    print("Invalid month")

elif day < 1 or day > 31:
    print("Invalid day")

else:
    print("Valid date")
'''
#problem_48[Check whether an email format is valid.]

'''
email=input("Enter email address: ")

if ( "@" in email and
    "." in email and 
    email.count("@")==1 and 
    email[0]!="@" and  
    email[-1]!="@" and 
    email.split("@")[0][-1]!="." and 
    email.split("@")[-1][-1]!="."):
    
    print("Valid email")
    
    
else: 
    print("Invalid email")

'''

#problem_49[Determine insurance eligibility using age, health status, and income.]
#health insurance

"""age = int(input("Enter age: "))
health = input("Enter health status (Good/Excellent/Poor): ")
income = int(input("Enter income: "))

if (18 <= age <= 60 and health == "Good" and income >= 25000) or (age > 60 and health == "Excellent"):
    print("Eligible for Health Insurance")
else:
    print("Not eligible for Health Insurance")

"""
#problem_50[Check leap year using complete leap year logic]

'''year=int(input("Enter year: "))

if (year%400==0) or (year%4==0 and year%100!=0):
    print("leap year") 
else:
    print("Not leap year")
'''





