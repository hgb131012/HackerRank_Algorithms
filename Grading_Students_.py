import os

def gradingStudents(grades):
    for index, grade in enumerate(grades):
        if grade < 38:
            pass
        else:
            if grade + (5 - (grade % 5)) - grade < 3:
                grades[index] = grade + (5 - (grade % 5))
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
