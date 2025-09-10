# take marks as input

maths = int(input("Enter marks in Maths: "))
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))
english = int(input("Enter marks in English: "))
computer = int(input("Enter marks in Computer: "))

total=maths+physics+chemistry+english+computer
percentage=(total/500)*100



if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Total : {total}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")