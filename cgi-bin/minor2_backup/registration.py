#!/usr/bin/python36

import cgi
import cgitb
cgitb.enable()


print("content-type:text/html")
print("\n")

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as db

form=cgi.FieldStorage()
name=form.getvalue("fullname")
email=form.getvalue("email")
phoneno=form.getvalue("phoneno")
password=form.getvalue("password")


con=db.connect(host='localhost',user='root',passwd='123456',db='minor2',port=3306)
cur=con.cursor()
cur.execute("SELECT * from userDetails where emailId='{}'".format(email))
res=cur.fetchall()

if res == ():
	cur.execute("INSERT into userDetails (name, emailId, phoneNo, password) values ('{0}','{1}','{2}', '{3}')".format(name,email,phoneno,password))
	con.commit()
	print("Successfully Registered!!")
	print("<br/>For logging in, <a href='../../minor2/index.html'> Click Here! </a>")
else:
	print("Email Id already exists! <br/> Please use a new one. <br/>")
	print("<br/>Register Again: <a href='../../minor2/index.html'> Click Here! </a>")


con.close()

