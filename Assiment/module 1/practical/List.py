List1 = ['apple', 'banana', 'mango']


for item in List1:
    if item == 'banana':
    # skip if ther is banana
        continue              
    print(item)

# Write a Python program to stop the loop once 'banana' is found using
# the break statement.

print("Question 2")

List2 = ['apple', 'banana', 'mango']

for items in List2:
    if items =="banana":
        break
    print(items)
