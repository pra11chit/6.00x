# Problem 2
# 10/10 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

count=0
for i in range(len(s)):
    if s[i]=='b':
        if (i+1)<len(s) and (i+2)<len(s):
            if s[i+1]=='o' and s[i+2]=='b':
                count+=1
print("Number of times bob occurs is: "+str(count))   

#Solved it after 10 attempts because of "index error : string out of range"
#so added if statement "if (i+1)<len(s) and (i+2)<len(s):"