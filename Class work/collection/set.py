s = {"A","B","C","D","A",100,1,True,0,False}

# print(type(s))

# for x in s:
#     print(x)

# print("abc"in s)

# s.add("abc")
# s.update({"p"},{"q"})
# print(s)

# s.remove("abc")
# s.discard("abc")
# s.pop()
# print(s)



a = {1,2,3,4,5}
b = {4,5,6,7,8,True}

c=a.union(b)
a.update(b)
c=a|b
c = a.intersection(b)
c = a&b
a.intersection_update(b)


c = a.difference(b)
c = a-b
a.difference_update(b)


c = a.symmetric_difference(b)
c = a^b
a.symmetric_difference_update(b)

print(a)
