
#problem_1[ What is the output of the following code?]

a = 5
b = 10
print(a < b < 20)   # or print((a < b) and (b < 20))

#problem_2[Predict the output:]

x = True                # True = 1 
y = False               # False = 0
print(x + y * x)        # 1+0*1=1+0=1   

#problem_3[What does this expression evaluate to?]

print(4 ** 0 ** 2)      #  or 4 ** (0 ** 2)

#problem_4[Find the result of this bitwise operation:]
"""a = 12
b = 5
print(a ^ b)
"""
#problem_5[Guess the output:]

print((3 and 0) or (0 and 3))   # or print((1 and 0) or (0 and 1)), non-zero numbers , non-empty string-> True 

#problem_6[What's the output of this tricky comparison?]

print(256 is 256)
print(257 is 257)

#problem_7[Evaluate this expression:]

a = 7
print(~a + 1)   # or print(-(a+1) + 1) ,formula ~x = -(x + 1)

#problem_8[What will this print?]

a = True
b = False
print((a or b) and not (a and b))

#problem_9[What's the output?]

print(10 > 5 == True)   # (10 > 5) and (5 == True)

#problem_10[Evaluate this expression:]

print(2 + 3 * 4 ** 2 // 8 % 3)

#problem_11[What does this expression evaluate to?]
"""
print(1 << 2 + 1)"""

#problem_12[Predict the output:]

a = 3
b = 2
a *= b + 1
print(a)


#problem_13[Evaluate this chained comparison:]

print(3 < 5 > 2 == 2)

#problem_14[Guess the result:]

print(10 // 3 * 3 + 1 % 3)

#probelm_15[What is the result of this?]
"""
x = 10
y = 20
print(x & y | x ^ y)"""

#problem_16[Trick with boolean and bitwise:]

a = True
b = False
print(a & b or a ^ b)

#problem_17[Evaluate this:]
"""
x = 8
print(x >> 1 << 2)"""

#problem_18[What does this produce?]

print(5 + True * False + (not False))

#problem_19[Operator confusion:]

print((not 0) * (False or 1))

#problem_20[Mix of precedence and associativity:]

print(4 + 3 * 2 ** 2 // 2 - 1)

