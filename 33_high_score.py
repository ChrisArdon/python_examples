# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maximun = 0
for number in student_scores:
    if(number > maximun):
        maximun = number

print("The highest score in the class is: " + str(maximun))


