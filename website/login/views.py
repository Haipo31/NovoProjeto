from django.shortcuts import render
import mysql.connector as sql

em = '' # Email
pwd = '' # Senha

def loginaction(request):

    global em, pwd

    if request.method=="POST":
        m = sql.connect(host="localhost", user="root", passwd="1234", database="website")   #SE DER ERRADO VERIFICAR AQUI !!!!
        
        cursor = m.cursor()
        
        d = request.POST

        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        
        c = "select * from users where email='{}' and password ='{}'".format(em,pwd)

        cursor.execute(c)
        t = tuple(cursor.fetchall())
        m.commit()

        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, 'twitter.html')

    return render(request, 'login_page.html')


