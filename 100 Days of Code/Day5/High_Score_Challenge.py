Student_Scores = []
Num_Of_Students = int(input("How Many Students: "))
high_score = 0

for n in range(Num_Of_Students):
    score = int(input("Enter your Score: "))
    Student_Scores.append(score)


print(Student_Scores)

for score in Student_Scores:
    if score > high_score:
        high_score = score

print(high_score)
