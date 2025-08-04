marks=int(input("enter any number"))

if( marks >= 90):
    grade = "A"
elif(marks>=80 and marks >70):
    grade = "B"
elif(marks>=70 and marks>60):
    grade = "C"
elif (marks>=60 and  marks>50):
    grade = "D"
else:
    grade = "F"

print("grade of the syudent :" , grade)