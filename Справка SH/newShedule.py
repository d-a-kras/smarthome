#!/usr/bin/python3
import psycopg2
import sys


connect = psycopg2.connect(database='local', host='localhost',port='5432',user='postgres', password='kras')
cursor=connect.cursor()


sql = "SELECT * FROM shedules"
    
cursor.execute(sql)
data = cursor.fetchall()
    
print(data)

