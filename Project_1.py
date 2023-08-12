#---------------------
# Name: Summer Davis
# COSC 1336
# Project 1
# ---------------------
# Objective
# This program will find the average grade of a student.
# The program will calculate the average exam score (sum of scores divided by 3).
# Then, it will display the student's average grade.
# ---------------------

# This function will collect and organize the program tasks
def main():
    
    # Displays the header of the project
    header()

    # Gets data from users
    studentName = input('Student Name: ')
    examOne = float(input('Enter score for Exam 1 '))
    examTwo = float(input('Enter score for Exam 2 '))
    examThree = float(input('Enter score for Exam 3 '))

    # Finds the average grade
    averageGrade = (examOne + examTwo + examThree) / 3

    # Displays the result
    print('\n')
    print('-' * 70)
    print('Grade Summary')
    print('-' * 70)
    print(f'     {studentName}\'s average of grade is: {averageGrade:.2f}')

    # Displays the end of the project
    footer()

# This function will display the header of the project
def header():
    print('Instructor\'s Entry')
    print('-' * 70)

# This function will display the end of the project
def footer():
    print('\n')
    print('-' * 70)
    print('End of Project 1')
    

# Calls the main function
main()


# Trace: 52>15>18>40>41>42>21>22>23>24>27>22>23>24>
#        30>31>32>33>34>21>27>37>45>46>47>48>53

