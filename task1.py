# task1
import math

# TASK REQUIRES USER INPUT OF 3 GRADES, SEPARATED BY COMMA.


print('1. Input grades, separated by comma.')

marks = input('Enter student\'s assessment marks (separated by comma): ')

# MARKS.SPLIT WILL CREATE A LIST OUT OF THE INPUT, USING THE COMMA AS SEPARATOR, AS REQUIRED.

all_marks = marks.split(",")

print('Assessment A: {}\nAssessment B: {}\nAssessment C: {}'.format(all_marks[0], all_marks[1], all_marks[2]))

# Now we convert the list of all marks into int, so we can calculate averages and/or percentages.

for i in range(len(all_marks)):
    all_marks[i] = int(all_marks[i])

# Then we apply the percentage/weight for each assessment, essential for obtaining the weighted final mark.

weighted_a = (all_marks[0] * 0.2)
weighted_b = (all_marks[1] * 0.4)
weighted_c = (all_marks[2] * 0.4)

final_mark = weighted_a + weighted_b + weighted_c

# Rounding up to nearest higher value.

final_mark = math.ceil(final_mark)

# Now the conditionals, which will give the corresponding letter grade.


if 100 >= final_mark >= 85:
    print('\nFinal grade is {}: HD'.format(final_mark))
elif 84 >= final_mark >= 75:
    print('\nFinal grade is {}: D'.format(final_mark))
elif 74 >= final_mark >= 65:
    print('\nFinal grade is {}:  C'.format(final_mark))
elif 64 >= final_mark >= 45:
    print('\nFinal grade is {}: F/SE/Sa'.format(final_mark))
else:
    print('\nFinal grade is {}: F'.format(final_mark))
