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

from csv2db import Database

if __name__ == '__main__':
    with Database('students.db', debug=True) as db:
        db.add_csv('students.csv', types=('TEXT', 'INT', 'INT PRIMARY KEY'))

        db.add_csv('courses.csv', types=('TEXT', 'INT', 'INT'))

        q = 'SELECT name, students.id, mark FROM students, courses ' \
            'WHERE students.id = courses.id'
        map(print, db.cursor.execute(q))