"""
not satisfactory according to me. different letters when arranged such that
their asii values match
"""

count1, count2 = 0,0

s1,s2=input("Enter str 1 : "), input("Enter str 2 : ")
count1=sum([ord(i) for i in s1])
count2=sum([ord(i) for i in s2])

if count1==count2:
    print("They are anagrams")
else:
    print("They are not anagrams")
