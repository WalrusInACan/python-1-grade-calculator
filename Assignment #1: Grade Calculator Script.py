#taking inputs from the user
number_of_labs = int(input("Enter the number of labs completed: "))
number_of_quizzes = int(input("Enter the number of quizzes completed: "))
assignment_1_grade = int(input("Enter the grade for Assignment 1: "))
assignment_2_grade = int(input("Enter the grade for Assignment 2: "))
assignment_3_grade = int(input("Enter the grade for Assignment 3: "))
assignment_4_grade = int(input("Enter the grade for Assignment 4: "))
midterm_1_grade = int(input("Enter the grade for Midterm 1: "))
midterm_2_grade = int(input("Enter the grade for Midterm 2: "))
final_exam_grade = int(input("Enter the grade for Final Exam: "))
preparations_grade = int(input("Enter the grade for Midterm and Final Preparations: "))

#calculating the weight of the labs completed
if number_of_labs > 6:
    labs_percentage = 20
else:
    labs_percentage = (number_of_labs / 6) * 20

#calculating the weight of the quizzes completed
if number_of_quizzes > 6:
    quizzes_percentage = 15
else:
    quizzes_percentage = (number_of_quizzes / 6) * 15

#calculating the weight of the assignments
assignment_percentage = ((assignment_1_grade * 0.04) + (assignment_2_grade * 0.04)
                         + (assignment_3_grade * 0.04) + (assignment_4_grade * 0.04))

#calculating the weight of the midterms
midterm_percentage = (midterm_1_grade * 0.125) + (midterm_2_grade * 0.125)

#calculating the weight of the final exam
final_exam_percentage = final_exam_grade * 0.18

#calculating the weight of the preparations
preparations_percentage = preparations_grade * 0.06

#calculating the weighted average
weighted_average = round(labs_percentage + quizzes_percentage + assignment_percentage + midterm_percentage
                         + final_exam_percentage + preparations_percentage,2)

print(f"Your grade is: {weighted_average}")
