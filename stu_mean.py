#!/usr/bin/python

"""
Khyber Sen and Irene Lam
SoftDev1 pd7
HW10 -- Average
2017-10-16
"""

from __future__ import print_function

__authors__ = ['Khyber Sen', 'Irene Lam']
__date__ = '2017-10-16'

from collections import namedtuple

from csv2db import Database

Student = namedtuple('Student', ['id', 'name', 'average'])  # type: (int, str, list[int] | int)


def group_students(db):
    # type: (Database) -> dict[int, Student]
    """Return dict[id, Student] where Student contains the id, name, and list[grade]."""
    query = 'SELECT name, id, grade FROM students, courses WHERE id = student_id'

    students = {}  # type: dict[int, (int, str, int)]
    for name, id, grade in db.cursor.execute(query):
        if id in students:
            students[id].average.append(grade)
        else:
            students[id] = Student(id, name, [grade])

    return students


def compute_student_averages(students):
    # type: (dict[int, Student]) -> list[Student]
    """Return list[Student] where Student contains id, name, and floated average of grades."""
    return [Student(id, student.name, float(sum(student.average)) / len(student.average)) for
            id, student in students.viewitems()]


def print_student_averages(students):
    # type: (list[Student]) -> None
    # map(print, students)

    # Printing, table format
    # for student in students:
    #     if len(student.name) < 7:
    #         print(student.name, "\t\t|| ID: ", student.id, "\t|| Average: ", student.average)
    #     else:
    #         print(student.name, "\t|| ID: ", student.id, "\t|| Average: ", student.average)

    # For tighter table formatting:
    for student in students:
        print("{0:11} || ID: {1:2} || Average: {2}".format(
            student.name, student.id, student.average))


def main():
    with Database('students.db', debug=True) as db:
        db.add_csv('students.csv', types=('TEXT', 'INT', 'INT PRIMARY KEY'))
        db.add_csv('courses.csv', types=('TEXT', 'INT', 'INT'))

        students = compute_student_averages(group_students(db))
        print_student_averages(students)


if __name__ == '__main__':
    main()
