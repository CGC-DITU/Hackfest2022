from re import S
from django.shortcuts import render
from django.contrib import messages
from datetime import *
import pymysql as p
# Create your views here.
def index(request):
    return render(request, 'home.html')
def bret(request):
    return render(request,'bret.html')
def br(request):
    
    return render(request,'bookre.html')
def sub(request):
    if request.method=="POST":
        num=request.POST.get('n')
    con=p.connect(host="localhost", user="root",db="lms",passwd="root",autocommit=True)
    f=con.cursor()
    f.execute("UPDATE `lms`.`new_table` SET `i_date` = CURDATE() WHERE (`book_id` = `%d`);"%(int(num)))
    print(num)
    messages.success(request,"Sucessfully submitted")
    return render(request,'bookre.html')
def ret(request):
    if request.method=="POST":
        num=request.POST.get('name')
    con=p.connect(host="localhost", user="root",db="lms",passwd="root",autocommit=True)
    f=con.cursor()
    f.execute("delete from lms.new_table where book_id=(%d);;"%(int(num)))
    messages.success(request,"Sucessfully submitted")
    return render(request,'bret.html')

def bal(request):
    return render(request,'bal.html')
def bl(request):
    try:
        if request.method=="POST":
            num=request.POST.get('name')
        con=p.connect(host="localhost", user="root",db="lms",passwd="root",autocommit=True)
        f=con.cursor()
        f.execute("select i_date,s_name from lms.new_table where book_id=%d"%(int(num)))
        c=f.fetchall()
        d=date.today()
    
        b=(d-c[0][0]).days
        s=0
        a=7*5
        k=7*10
        if(b<7):
            s+=b*5
        elif(b>7 and b<14):
            s+=a+(b-7)*20
        elif(b>14):
            s+=a+k+(b-14)*50
        context={
            'balance':s,
            'name':c[0][1]
        }
    

        messages.success(request,"Sucessfully submitted")
        return render(request,'disp.html',context)
    except:
        messages.success(request,"Invalid choice")
        return render(request,'bal.html')
