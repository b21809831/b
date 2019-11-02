#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        grades_count = int(input().strip())

        grades = []
        grades_split = grades.split()
        for i in grades_split():
            if i < 38:
                print(i)
            elif i % 10 == 0:
                print(i)
            elif i % 10 != 0:
                a = i % 10
                print(i+a)
        for _ in range(grades_count):
            grades_item = int(input().strip())
            grades.append(grades_item)

        result = gradingStudents(grades)

        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
