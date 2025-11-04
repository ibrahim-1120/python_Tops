
with open('test.txt','r') as f:
    print(f.tell())
    f.seek(10)
    print(f.tell())
    data = f.read()
    print(f.tell())
    print(data)