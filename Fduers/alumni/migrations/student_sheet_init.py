# Generated by Django 3.2.5 on 2021-07-14 16:45

# Attention!!!!!!
# This module provided an example of student information
# When in real situation, the student sheet should be uploaded through web, and this module should not be activated

from django.db import migrations, models
import django.db.models.deletion
import sqlite3
import os
from functionality.readexcel import decode

dbpath = './generator/data/city_version-4.sqlite'
sheetpath = './generator/data/example.xls'

def student_sheet_init(apps, schema_editor): # import ../generator/data/city_version-4.sqlite into model city and province
    stuList = decode(sheetpath)
    print()
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    Student = apps.get_model('alumni', 'Student')
    Department = apps.get_model('alumni', 'Department')
    for row in stuList:
        tmp = Student(name = row[0], studentID = row[1], department = Department(name = row[2]), grade = row[3])
        print(row[0], row[1], row[2], row[3])
        tmp.save()

class Migration(migrations.Migration):
    dependencies = [
        ('alumni', 'department_init'),
    ]

    operations = [
        migrations.RunPython(student_sheet_init),
    ]
