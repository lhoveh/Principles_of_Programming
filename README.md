# Principles_of_Programming
Assessment 2 for Python classes

Assessment 2 – Business Case Study

Case Scenario
COMP101 Foundations of Computer Systems is a first-year introductory subject in both the Bachelor
of Information Technology and Diploma of Information Technology course at ABC University. The
Subject Coordinator of COMP101 has engaged you to help her to code a few Python programs as
handy tools to solve a number of problems at hand.

Task 1 - Determine Interim Grade Letter (30%)

In this task, you will write a Python program to help the Subject Coordinator of COMP101 to calculate
an interim grade letter for a student given their assessments results.
COMP101 Foundations of Computer Systems has three assessments with the following weightings.


1 Lab exercise 20%
2 Report 40%
3 Final examination 40%

Each assessment has been marked out of 100 and the mark for each assessment may be a decimal
number with at most two decimal points (e.g., 68, or 68.5, or 68.45). The final mark for COMP101 is
the weighted sum of all three assessments, rounded up 1
to the nearest integer. For example, Student
A received 75.67/100, 45.8/100, 32/100 for Assessment 1, 2 and 3 respectively. Their final mark for
COMP101 is 47 (46.254 rounded up to the nearest integer).

75.67 × 20% + 45.8 × 40% + 32 × 40% = 46.254

For simplicity, in this Task, we will use a bracket that consists of three numbers to denote the marks
of a student’s three assignments in order. For example, (75.67, 45.8, 32) denote a student who
received 75.67/100 for the first assessment, 45.8/100 for the second, and 32/100 for the third.

The final mark is used to determine the interim grade letter for a student. The Assessment Policy and
Procedures of ABC University stipulates the following rules for determining the interim grade letter.
The range in the Final mark column includes the numbers on both ends.

Final mark Interim grade letter Description
85 - 100 HD High Distinction
75 - 84 D Distinction
65 - 74 C Credit
50 - 64 P Pass
45 - 49 F or SE or SA Fail or Supplementary Assessment or Supplementary Exam
0 - 44 F or AF Fail or Absent Fail

1 No students like their marks rounded down, so always round up their marks. Even if the weighted sum is 90.001, their
final mark should be recorded as 91. 

2
Students whose final mark is between 0 and 44 (inclusive) may be awarded an F (Fail) or an AF (Absent
Fail). If two or more assessments are awarded zero and the final mark is between 0 and 44 (inclusive),
the student will be awarded an AF (Absent Fail), otherwise they are awarded an F (Fail).
For example, students with (0, 100, 0) should be awarded an AF because their final mark is 40, and
two assessments are marked zero. However, students with (100, 50, 0) should be awarded an F
because although their final mark is 40, they only have one assessment awarded zero.
Students who have marginally failed, that is, their final mark is between 45 – 49 (inclusive), may be
awarded an F (Fail) or Supplementary Exam (SE) or Supplementary Assessment (SA). 

If a student’s final
mark is between 45 – 49, they will receive an F (Fail) unless they satisfy all the following conditions:

o Their final mark is between 45 – 49 (inclusive).
o They do not have any assessment marked zero.
o They only failed (i.e., less than 50) one assessment.

Students whose final mark is between 45 – 49 will receive an SE or SA if they satisfy all the conditions
above. If the assessment they failed is Assessment 1 or Assessment 2, they will receive an SA and they
will be given an opportunity to attempt a supplementary assessment. If the assessment they failed is
Assessment 3, they will receive an SE and they will be given an opportunity to sit a supplementary
exam.

For example, students with (40, 100, 0) will receive an F (Fail) because although their final mark is 48
(i.e., between 45 – 49), they have one assessment marked zero (Assessment 3). Students with (10,
100, 10) will equally be awarded an F (Fail) because although their final mark is 46 (i.e., between 45 –
49), they have failed more than one assessment (Assessment 1 and Assessment 3). Students with (50,
50, 40) will be awarded an SE because their final mark is 46 (i.e., between 45 – 49) and satisfy all the
three conditions above. The only failed assessment is Assessment 3, and they will be given an
opportunity to sit a supplementary exam.

The Subject Coordinator has asked you to develop a Python program that can calculate the interim
grade letter for a student given the marks for all the assessments based on the business rules
described above.

Your program should allow the Subject Coordinator to type in a student’s assessment marks separated
by a comma. Your program will then output the correct interim grade letter for that student. In this
task, you do not need to allow the Subject Coordinator to type in the assessment marks for another
student. Your program can terminate after it have calculated and output the interim grade letter for
the first student.

Here are some sample inputs and outputs the Subject Coordinator expected to see when she runs
your program. All the green lines are your program outputs, all the red lines are users’ input.

Sample input and output 1:
>>> Enter a student’s assessment marks (separated by comma):
>>> 40,100,0
>>> F
>>> 
Sample input and output 2:
>>> Enter a student’s assessment marks (separated by comma):
>>> 90,100,100
>>> HD
>>> 
Sample input and output 3:
>>> Enter a student’s assessment marks (separated by comma):
>>> 50,50,40
>>> SE
>>> 
Implement your program in a Python script file and name it task1.py. You need to submit this file
as part of the Assessment 2 submission.

Task 2 – Finalising grades and class performance statistics (40%)

This task is built upon Task 1. You may want to make a copy of task1.py, and name it task2.py,
and you may want to use the logic you implemented for Task 1. DO NOT override task1.py.
A couple of weeks after the Release of Grade date, all supplementary assessments and exams have
been finalised. All the interim grade letters now need to be converted to a final grade letter, that is,
the grade letter that appear on students’ transcript.

For HD (High distinction), D (Distinction), C (Credit), P (Pass) and F (Fail), they will not be converted as
they themselves are final grade letters. For SA and SE, they will be converted to either a SP
(Supplementary Pass) or F (Fail). If the student who have been awarded an SA or SE, passed the
supplementary assessment or supplementary exam (that is, they achieved no less than 50/100), their
grade letter will be converted to SP (Supplementary Pass), otherwise it will be converted to F (Fail).
For AF (Absent Fail), it will be converted to F (Fail).

Each final grade letter carries some grade point value as detailed in the table below.

HD 4.0
D 3.0
C 2.0
P 1.0
SP 0.5
F 0

The Subject Coordinator would like you to implement a Python program that helps her to read in all
students’ marks and generate some high-level statistic about the class performance.

Input
In contrast with Task 1, the program in Task 2 will prompt to the Subject Coordinator (the user) and
allow her type in all students’ assessment marks. This is achieved by repeatedly asking the Subject
Coordinator to type in students’ three assessment marks until she types in the letter “N”. 

For example,
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 40,100,0
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 90,100,100
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> N
(input finishes)

The Subject Coordinator (the user) may type in as many students’ assessment marks as she wishes.
Each line of input represents a student’s three assessment marks. The only way she signals to the
program that she has done with inputting is to type in a letter N.

Your program should use an appropriate data structure to store students’ marks.

As you read in students’ assessment marks, if your program detects that the student would have been
given an SE or SA, your program should then ask for their supplementary assessment or
supplementary exam mark. 

For example,
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 40,100,0
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 50,50,40
>>> What is this student’s supplementary exam mark:
>>> 67
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 90,100,100
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> N
(input finishes)

Output
After input finishes, your program will then output the following class performance statistics:

o Number of students: This number shows the total number of students that the user typed in.

o Student pass rate: The percentage of students who received a final grade letter of HD, D, C, P
or SP, that is,
#𝐻𝐷 + #𝐷 + #𝐶 + #𝑃 + #𝑆𝑃
#𝑠𝑡𝑢𝑑𝑒𝑛𝑡
#HD represents the number of students who received HD. #student represents the total
number of students. Rounded to two decimal points.

o Student pass rate (adjusted): The percentage of students who received a final grade letter of
HD, D, C, P or SP. This percentage excludes students who received an AF from the total number
of students, that is,
#𝐻𝐷 + #𝐷 + #𝐶 + #𝑃 + #𝑆𝑃
#𝑠𝑡𝑢𝑑𝑒𝑛𝑡 − #𝐴𝐹
Rounded to two decimal points.

o Average mark for Assessment 1: the average mark for Assessment 1 with two decimal points.

o Average mark for Assessment 2: the average mark for Assessment 2 with two decimal points.

o Average mark for Assessment 3: the average mark for Assessment 3 with two decimal points.

o Average final mark: the average mark for final mark with two decimal points.

o Average grade point: the average grade point for all students in COMP101 with one decimal
point.

o Number of HDs: the number of students who received a final grade letter HD.

o Number of Ds: the number of students who received a final grade letter D.

o Number of Cs: the number of students who received a final grade letter C.

o Number of Ps: the number of students who received a final grade letter P.

o Number of SPs: the number of students who received a final grade letter SP.

o Number of Fs: the number of students who received a final grade letter F.

For example,
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 40,100,0
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 50,50,40
>>> What is this student’s supplementary exam mark:
>>> 67
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> 90,100,100
>>> Enter a student’s assessment marks (separated by comma), type in letter N to finish:
>>> N
>>> Number of students: 3
>>> Student pass rate: 66.67%
>>> Student pass rate (adjusted): 66.67%
>>> Average mark for Assessment 1: 60.00
>>> Average mark for Assessment 2: 83.33
>>> Average mark for Assessment 3: 46.67
>>> Average final mark: 64.00
>>> Average grade point: 1.5
>>> Number of HDs: 1
>>> Number of Ds: 0
>>> Number of Cs: 0
>>> Number of Ps: 0
>>> Number of SPs: 1
>>> Number of Fs: 1
>>> 
Implement your program in a Python script file and name it task2.py. You need to submit this file
as part of the Assessment 2 submission.


Task 3 – Naïve similarity detector (30%)

This task is independent of the first two tasks. You can create a new file and name it task3.py.
The Subject Coordinator of COMP101 has now asked you to implement a naïve similarity detector that
she can use to identify collusion between students in their assessments. Your program will read in two
assessment submissions (two strings) in turn and output a similarity score for them.
You can assume that the input submissions have been “cleaned” with all punctuations removed. Each
submission is a sequence of words separated by a space. 

For example,
“COMP101 is an interesting subject and it has been easy”
“COMP101 and COMP301 have always been interesting and easy”
The similarity of two submissions is defined as the ratio between the number of common words in
both submissions and the number of unique words in both submissions.


For example,
“COMP101 is an interesting subject and it has been easy”
“COMP101 and COMP301 have always been interesting and easy”
The common words between these two submissions are COMP101, and, interesting, been, easy. A
total of 5 common words.
The unique words in both submissions are COMP101, and, interesting, been, easy, is, an, subject, it,
has, COMP301, have, always. A total of 13 common words.
The similarity of both submissions is 5/13 = 38.46%.

Implement a Python program that takes in two submissions (strings) and output the similarity
between them with two decimal points. For example:
>>> Enter the first submission:
>>> COMP101 is an interesting subject and it has been easy
>>> Enter the second submission:
>>> COMP101 and COMP301 have always been interesting and easy
>>> The similarity score between the two is: 38.46%.
>>> 
You should ignore the letter cases, that is, “Interesting” and “interesting” should be treated as the
same word. You do not need to lemmatise the words, that is, the words “going”, “go”, “went”, “gone”
are treated as different words. 
