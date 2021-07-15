# Generated by Django 3.2.5 on 2021-07-14 16:45

from django.db import migrations, models
import django.db.models.deletion
import sqlite3
import os

dbpath = './generator/data/city_version-4.sqlite'

def City_init(apps, schema_editor): # import ../generator/data/city_version-4.sqlite into model city and province
    if not os.path.exists(dbpath):
        print('no database detected')
    else:
        print('database detected!')
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()

    Province = apps.get_model('alumni', 'Province')
    City = apps.get_model('alumni', 'City')
    
    cursor = c.execute('SELECT * FROM province')

    prv = []

    for row in cursor:
        tmp = Province(name = row[0])
        prv.append([row[0], row[1]])

    cursor = c.execute('SELECT name,province_no FROM city')

    for row in cursor:
        # row[0]: city_name, row[1]: province_no
        # print(row[0], row[1])
        
        print(row[0], row[1])

        province = ''
        for p in prv:
            if p[0] == row[1]:
                province = p[1]

        print('result:', row[0], province)
        tmp = City(name = row[0], province = Province(name = province))
        tmp.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumni', 'province_init'),
    ]

    operations = [
        migrations.RunPython(City_init),
    ]
