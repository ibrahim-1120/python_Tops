# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

print("Program started")
try :
    a = 10
    b = a/0
    print(b)
except Exception as e:
    print(e)
print("Program ended")

# Write a Python program to demonstrate handling multiple exceptions.


    
    

   
try:
    user_input = input("Enter a number or a string: ")
    num = int(user_input)
    result = 10 / num
    print(f"Result of 10 / {num} is: {result}")
except (ValueError, ZeroDivisionError) as e:
     print(f"An error occurred (single except block): {e}")

   

    
try:
    data = [1, 2, 3]
    index = int(input("Enter an index for the list (0-2): "))
    print(f"Value at index {index} is: {data[index]}")
except ValueError as ve:
    print(f"Invalid input: Please enter an integer. Error: {ve}")
except IndexError as ie:
    print(f"Index out of bounds: Please enter an index between 0 and 2. Error: {ie}")
except Exception as ex: 
    print(f"An unexpected error occurred: {ex}")

print("\n--- Program finished ---")


