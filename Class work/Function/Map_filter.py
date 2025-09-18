

m=[10,20,30,40,50,60,70,80,90]


# def square(a):
#     return a*a

# using simple 
# s=[]
# for i in m:
#     k=square(i)
#     s.append(k)
# print(s)

# using map
# s=map(square,m)

# map without creating function using lamda
s=map(lambda a: a*a,m)
print(list(s))