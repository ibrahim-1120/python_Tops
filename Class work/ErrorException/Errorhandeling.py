# print("program start")

# try:
#     a=10
#     b=a/2
#     print(b)
# except Exception as q:
#     print(q)

# else:
#     print("all ok")


# print("program end")    


# f=""

# try:
#     f=open("text.txt","r")
#     data=f.read()
#     print(data)
# except Exception as q:
#     print(q)

# finally:
#     if(f is not found):
#     f.close()


def test():
    try:
        a=int(input("enter number"))
        return 1
    except Exception as a:
        return 0
    finally:
        print("program execced")


a=test()
print(a)