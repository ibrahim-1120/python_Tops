for i in range(100,1000):

    number = i
    temp = number
    sum=0


    while number!=0:
        rem = number%10
        sum+=rem**3
        number = number//10


    if(sum==temp):
        print(f"{temp},Armstrong")
    else:
        # print("not")
        pass


