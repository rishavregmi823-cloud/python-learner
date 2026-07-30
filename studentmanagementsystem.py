students= ["Ram", "Santosh" ,"Dyneal" ,"Micel"]
subjects= ("Maths", "Account","Economics", "English")
marks=     [ 
    [35, 56, 70 ,65],
[ 30, 40, 34 ,8],
[ 55, 68, 67 ,45],
[ 20, 64, 44 ,59],
]

total_marks= []
percentages= []
for student_marks in marks :
    total= sum(student_marks)
    percentage= (total/300) *100
    total_marks.append(total)
    percentages.append(percentage)
    highest= max(percentages)
    lowest= min(percentages)
    topper_index = percentages.index(highest)
lowest_index = percentages.index(lowest)

print(f"The topper is {students [2]} with highest {highest} ")
print(f"Congratulations!! {students [2]} for excellent result\n")

print(f"Your perfermence is so poor {students [1]} out of four students with lowest {lowest}")