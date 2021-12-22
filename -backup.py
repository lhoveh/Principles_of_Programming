#task2
import math


# SEPARETED BY COMMA, BEFORE WEIGHT

print ('1. Input grades, separated by comma, before weight. \n Trying "40,100,0" should return "F", \n pelase try it.')


marks = input('Enter student\'s assessment marks (separeted by comma): ')
all_marks = marks.split(",")
print(all_marks)

for i in range(len(all_marks)):

    # converting each item to int type

    all_marks[i] = int(all_marks[i])

final_mark = ((all_marks[0] + all_marks[1] + all_marks[2])/3)
final_mark = math.ceil(final_mark)

if final_mark <=100 and final_mark >=85:
     print (' final grade is HD')
elif final_mark <=84 and final_mark >=75:
     print (' final grade is D')
elif final_mark <=74 and final_mark >=65:
    print (' final grade is C')
elif final_mark <=64 and final_mark >=45:
    print (' final grade is F/SE/SE \n')
else:
   print (' final grade is F')

print ('2. Input, separated by comma, before weight. \n "90,100,100" must return HD, \n pelase try it.')

marks = input('Enter student\'s assessment marks (separeted by comma): ')
all_marks = marks.split(",")
print(all_marks)

for i in range(len(all_marks)):

    # converting each item to int type

    all_marks[i] = int(all_marks[i])

final_mark = ((all_marks[0] + all_marks[1] + all_marks[2])/3)
final_mark = math.ceil(final_mark)

if final_mark <=100 and final_mark >=85:
     print (' final grade is HD')
elif final_mark <=84 and final_mark >=75:
     print (' final grade is D')
elif final_mark <=74 and final_mark >=65:
    print (' final grade is C')
elif final_mark <=64 and final_mark >=45:
    print (' final grade is F/SE/SE \n')
else:
   print (' final grade is F')

   print('3. Input, separated by comma, before weight. \n Trying "50,50,40" must return "SE"\n '
         '\n pelase try it.')

marks = input('Enter student\'s assessment marks (separeted by comma): ')
all_marks = marks.split(",")
print(all_marks)

for i in range(len(all_marks)):
    # converting each item to int type

    all_marks[i] = int(all_marks[i])

final_mark = ((all_marks[0] + all_marks[1] + all_marks[2]) / 3)
final_mark = math.ceil(final_mark)

if final_mark <= 100 and final_mark >= 85:
    print(' final grade is HD')
elif final_mark <= 84 and final_mark >= 75:
    print(' final grade is D')
elif final_mark <= 74 and final_mark >= 65:
    print(' final grade is C')
elif final_mark <= 64 and final_mark >= 45:
    print(' final grade is F/SE/SE \n')
else:
    print(' final grade is F')

# SEPARETED BY COMMA, AFTER WEIGHT

print ('\n \n Extra Options. Input values, separated by comma, before weight. \n',
       'The system must calculate the final weighted grade \n')

marks = input('Enter student\'s assessment marks: ')
all_marks = marks.split(",")
print(all_marks)

for i in range(len(all_marks)):

    # converting each item to int type

    all_marks[i] = int(all_marks[i])

weighted_a = (all_marks[0]*0.2)
weighted_b = (all_marks[1]*0.4)
weighted_c = (all_marks[2]*0.4)

final_mark = weighted_a + weighted_b + weighted_c
final_mark = math.ceil(final_mark)

if final_mark <=100 and final_mark >=85:
     print (' final grade is HD')
elif final_mark <=84 and final_mark >=75:
     print (' final grade is D')
elif final_mark <=74 and final_mark >=65:
    print (' final grade is C')
elif final_mark <=64 and final_mark >=45:
    print (' final grade is F/SE/SE \n')
else:
   print (' final grade is F')

#Alternatives


print ('\n\nInput and Output 1 \n')

student_name = input('Enter student name:')

mark_a = float(input('Enter ' + student_name + '\'s assessment A mark: '))
mark_b = float(input('Enter ' + student_name + '\'s assessment B mark: '))
mark_c = float(input('Enter ' + student_name + '\'s assessment C mark: '))

weighted_a = mark_a*0.2
weighted_b = mark_b*0.4
weighted_c = mark_c*0.4

final_mark = weighted_a + weighted_b + weighted_c

print ('\n\n', student_name, '\'s grades: \n\n Assessment A:', round(weighted_a,2), '\n Assessment B:', weighted_b, '\n Assessment C:', weighted_c)

print ('\n', student_name, '\'s final mark: \n', math.ceil(final_mark), '\n')

final_mark = math.ceil(final_mark)

if final_mark <=100 and final_mark >=85:
    print (student_name + ' final grade is HD')
elif final_mark <=84 and final_mark >=75:
    print (student_name + ' final grade is D')
elif final_mark <=74 and final_mark >=65:
    print (student_name + ' final grade is C')
elif final_mark <=64 and final_mark >=45:
    print (student_name + ' final grade is F/SE/SE \n')
else:
    print (student_name + ' final grade is F')

print ('\n\nInput and Output 2 \n')

mark_a = float(input('Enter ' + student_name + '\'s assessment A mark: '))
mark_b = float(input('Enter ' + student_name + '\'s assessment B mark: '))
mark_c = float(input('Enter ' + student_name + '\'s assessment C mark: '))

weighted_a = round(mark_a*0.2,2)
weighted_b = round(mark_b*0.4,2)
weighted_c = round(mark_c*0.4,2)

final_mark = weighted_a + weighted_b + weighted_c
final_mark = math.ceil(final_mark)

print ('\n', student_name, '\'s weighted grades: \n\n Assessment A:', weighted_a, '\n Assessment B:', weighted_b, '\n Assessment C:', weighted_c, '\n')

if final_mark <=100 and final_mark >=85:
    print (student_name + ' final grade is HD')
elif final_mark <=84 and final_mark >=75:
    print (student_name + ' final grade is D')
elif final_mark <=74 and final_mark >=65:
    print (studen_name + ' final grade is C')
elif final_mark <=64 and final_mark >=45:
    print (student_name + ' final grade is F/SE/SE \n')
else:
   print (student_name + ' final grade is F')

