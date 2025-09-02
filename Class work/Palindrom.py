number=151151
temp=number
sum=0

while number!=0:
    rem=number%10
    sum=number*10 +rem
    number= number//10

if sum==temp:
    print("Palindrom")
else:
    print("Not palindrom")    