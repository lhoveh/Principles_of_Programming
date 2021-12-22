# TASK2 BELOW
import math

# We create a variable that will be identified as the loop terminator, as per assessment requirements.

loop_terminator = "n"

# We also create a variable that will contain the assessment marks for A,B,C

marks = ''

# And we create the lists for the grades, grade point and grade letter respectively.
# Below a list for inclusion of grades for each assessment, A,B and C, as we are going to use them later.

students_list = []
students_list_letter = []
grade_point_list = []

Assessment_A = []
Assessment_B = []
Assessment_C = []

# The while loop, which will continue until the user applies the loop terminator "n", as per assessment.

while loop_terminator != marks:

    marks = (input('Enter student\'s assessment marks (separeted by comma):'))
    all_marks = marks.split(",")

    # the lists start after the first input, then we convert to int. It keeps occurring while inputs are different from "n"

    if marks != loop_terminator:
        for i in range(len(all_marks)):
            all_marks[i] = int(all_marks[i])

        # now we have a list "all_marks" with all marks, for this first input, then we calculate the weighted mark.
        # in other words, we have a list of A, B, C grades for this student, so we record the weighted and final mark as well.

        weighted_a = (all_marks[0] * 0.2)
        weighted_b = (all_marks[1] * 0.4)
        weighted_c = (all_marks[2] * 0.4)

        final_mark = weighted_a + weighted_b + weighted_c

        # rounding the final mark

        final_mark = math.ceil(final_mark)

        final_mark = ((all_marks[0] + all_marks[1] + all_marks[2]) / 3)
        final_mark = math.ceil(final_mark)

        # now that we have final mark, we can calculate the grade point, and grade letter.
        # the conditions below will define grade_point, which will de recorded as a variable and saved in the respective list.

        if 100 >= final_mark >= 85:
            grade_point = 4
            final_grade_letter = "HD"
        elif 84 >= final_mark >= 75:
            grade_point = 3
            final_grade_letter = "D"
        elif 74 >= final_mark >= 65:
            grade_point = 2
            final_grade_letter = "C"
        elif 64 >= final_mark >= 50:
            grade_point = 1
            final_grade_letter = "P"
        elif 49 >= final_mark >= 45:

            # in this case, there is a another conditional. If the student hasn't taken the s-test, he is "AF" ans 0.
            # if the student has taken the s-test, another conditional, for his s-test result. Below 50 will be 0 and F.
            # for students with grade >50, a grade-point of 0.5 is recorded, plus grade letter "SP"

            choice = input("Have the student taken the supplementary exam? (y/n) ").lower()
            yesChoice = ['yes', 'y']
            noChoice = ['no', 'n']

            if choice in yesChoice:

                s_grade = int(input("SA/SE/F. Please insert supplementary exam grade: "))
                if s_grade < 50:
                    grade_point = 0
                    final_grade_letter = "F"

                else:
                    grade_point = 0.5
                    final_grade_letter = "SP"

            elif choice in noChoice:
                grade_point = 0
                final_grade_letter = "AF"

        else:
            grade_point = 0
            final_grade_letter = "F"

        mark_A = (all_marks[0])
        mark_B = (all_marks[1])
        mark_C = (all_marks[2])


        # here we are just printing the parcials, their assessment's grades and final grade. using format method.

        print('\nAssessment A: {} \nAssessment B: {} \nAssessment C: {}'.format(mark_A, mark_B, mark_C))
        # print('Assessment A: { }, Assessment B: {}, Assessment C {}.'.format, all_marks)
        print('Weighted final mark: ', final_mark, '\n')

        # now these student's grades are going to be included in their respective lists.
        # below the lists of final marks, grade letter and grade point.

        students_list.append(final_mark)
        students_list_letter.append(final_grade_letter)
        grade_point_list.append(grade_point)

        # below the lists of assessment A, B and C grades.

        Assessment_A.append(mark_A)
        Assessment_B.append(mark_B)
        Assessment_C.append(mark_C)

# Outside the loop the commands that will be triggered after leaving the looping, after pressing "n".

print('\nPERFORMANCE STATISTICS')

# 1. TOTAL OF STUDENTS. COULD BE THE LEN OF LIST OF GRADES, GRADE POINT, GRADE POINT LETTER. THEY HAVE THE SAME LEN.
# For each event of grade inclusion, 1 final grade, which is = 1 student, was included in these lists.

total = len(grade_point_list)
print('\nNumber of students: ', total)


# 2. TOTAL OF APPROVED STUDENTS. We simply count the total of non-approved, which are the "0" in the grade point list.

non_approved = grade_point_list.count(0)

print('\nTotal of failed students: {}'.format(non_approved))

approved = total - non_approved

print('Total of approved students: {}'.format(approved))

student_pass_rate = approved / total

print('\nStudent pass rate: {:2.2%}'.format(student_pass_rate))


# 3. TOTAL, BUT REMOVING THE AF. SO WE WILL COUNT THE LEN OF THE AF INSIDE THE LIST.
# THEN REMOVE THE AF COUNT FROM THE NUMBER OF NON-APPROVED.


af = students_list_letter.count("AF")
print("\nStatistics excluding the absent students: \n\nTotal of absent fail: {}".format(af))

total_2 = total - af
non_approved_2 = non_approved - af

print('Total of failed students excluding the absents: {}'.format(non_approved_2))

student_pass_rate_2 = approved / total_2

print('\nStudent pass rate: {:2.2%}'.format(student_pass_rate_2), '\n(Not considering the absents)')

# 4 AVERGAES

average_A = sum(Assessment_A) / len(Assessment_A)
average_B = sum(Assessment_B) / len(Assessment_B)
average_C = sum(Assessment_C) / len(Assessment_C)

average_total = sum(students_list) / len(students_list)

average_grade_point = sum(grade_point_list) / len(grade_point_list)

print('\n Average Assessment A grade (before weight): ', round(average_A, 2))
print('\n Average Assessment B grade (before weight): ', round(average_B, 2))
print('\n Average Assessment C grade (before weight): ', round(average_C, 2))

print('\n Average final weighted mark: ', round(average_total, 2))

print('\n Average grade point list: ', round(average_grade_point, 2))

each_grade_letter = {i: students_list_letter.count(i) for i in students_list_letter}

print('\n How many results for each grade letter: \n', each_grade_letter)
