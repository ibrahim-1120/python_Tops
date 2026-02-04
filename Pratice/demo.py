# st="my name is Ibrahim  (Ibu)  ß"

# print(len(st))
# print(st.lower())
# print(st.casefold())
# print(st.upper())
# print(st.capitalize())
# print(st.title())
# print(st.strip())
# # print(st.replace('my name is Ibrahim  (Ibu)','hello',2))
# print(st.find('my'))
# print(st.startswith('my'))
# print(st.endswith(' ß'))
# print(st.split(','))
# print('my'.join('is'))
# print("abc".join("XYZ"))
# print("abc".isalpha())
# print("123dfd".isdigit())
# print("ssas12".isalnum())
# print("abc".zfill(10))
# print("abc".center(21,"*"))

k = "hello python hello 4545 ddds 545454"

a = 0
b = 0
for i in k:
    if str(i).isalpha():
        a+=1
    elif str(i).isdigit():
        b+=1
print("alpha : ",a)
print("numbers : ",b)

print(k[5:])
print(k[:5])
print(k[5:9])
print(k[-8:-1])
print(k[::-1])

s = ""
for i in range(len(k)-1,-1,-1):
    s+=k[i]

print(s)