#!/usr/bin/python

def is_palindrome(x):
	if str(x) == str(x)[::-1]: return True
	else: return False

def is_lychrel(x):
    for i in range(50):
        y=x+int(str(x)[::-1])
        if is_palindrome(y): return False
        x=y
    return True
    
count = 0
for i in range(1, 10001):
    if is_lychrel(i): count += 1
    
print count