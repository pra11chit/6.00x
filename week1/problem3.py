#Write a program that prints the longest substring of s in which the 
#letters occur in alphabetical order. For example, if s = 'azcbobobegghakl',
#then your program should print                            0123456789
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', 
#then your program should print
#
#Longest substring in alphabetical order is: abc
s = 'ybxqojwld'
longest=s[0]
current=s[0]
for i in range(len(s)-1):
    if s[i+1]>=s[i]:
        current+=s[i+1]
        if len(current)>len(longest):
            longest=current
        if len(longest)==len(current):
            longest=longest
    else:
        current=s[i+1]
print("Longest substring in alphabetical order is: "+longest)        