import math

student_heights = []
num_of_height = int(input("How Many Students: "))
sum_height = 0
avg = 0

for n in range(num_of_height):
    height = int(input("Enter your height: "))
    student_heights.append(height)
    sum_height += height
    avg = sum_height/len(student_heights)

print(student_heights)
print(sum_height)
print(round(avg))
