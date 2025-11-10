f=open("My.txt","w")
f.write("My name is ibrahim")
f.close()

f=open("My.txt","a")
f.write("\t Burhanpurwala")
f.close()

f=open("My.txt","a")
f.write("\n This is python")
f.close()

f=open("My.txt","r")
data=f.read()
print(data)

f=open("My.txt","r")
while True:
    data=f.readline()
    print(len(data))
    if 'Burhanpurwala'in data:
        print(data)
    if not data:
        break    

f=open("My.txt",'r')
data=f.readlines()
print(data)

