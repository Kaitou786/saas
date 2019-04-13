#!/usr/bin/python36
import cgi
import cgitb
cgitb.enable()

print("content-type:text/html")


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as db

form=cgi.FieldStorage()
username=form.getvalue("user")
pwd=form.getvalue("password")


con=db.connect(host='localhost',user='root',passwd='123456',db='minor2',port=3306)
cur=con.cursor()

cur.execute("SELECT password from userDetails WHERE emailId='{}'".format(username))
f=cur.fetchall()

if f == () :
	print("location:../../minor2/loginInvalid.html")
	print("\n")

elif f[0][0] == pwd:
	print("location:../../minor2/client/index.html")
	print("\n")

else:
	print("location:../../minor2/loginInvalid.html")
	print("\n")

