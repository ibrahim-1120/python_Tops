# Write a Python program to print a formatted string using print() and f-string.


name = "Ibrahim"
age = 20
city = "Surat"
temperature = 50

print(f"Hello, my name is {name} and I am {age} years old.")


# Using the input() function to read user input from the keyboard.

print(input("Enter your name"))

user = int(input("Enter an integer: "))
print(f"You entered: {user}, Type: {type(user)}")

# Write a Python program to open a file in write mode, write some text, and then close it.

f=open("My.txt","w")
f.write("My name is ibrahim")
f.close()

# Write a Python program to read the contents of a file and print them on the console.

f=open("My.txt","w")
f.write("Burhanpurwala")
f.close()

f=open("My.txt","r")
while True:
    data=f.readline()
    if "Burhanpurwala" in data:
        print(data)
    else:
        break


# Write a Python program to write multiple strings into a file        


f=open("Demo.txt","w")
f.write("This is")
f.close()

f=open("Demo.txt","a")
f.write("Python")
f.close()

