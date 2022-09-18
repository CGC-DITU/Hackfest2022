from asyncio.windows_events import NULL
from contextlib import nullcontext
from email import message
from urllib import response
from django.shortcuts import render
import pymysql as p
from django.contrib import messages
from django.shortcuts import HttpResponse
import random

# Create your views here.
def index(request):
    return render(request,'home.html')
def con(request):
    return render(request,'Contact.html')
def log(request):
    return render(request,'loginpage.html')
     
    
     
def op(request):
    
    
        name=request.POST.get('username')
        passd=request.POST.get('password')
        print(passd)
        con=p.connect(host="localhost",db="banking",user="root",passwd="root",autocommit=True)
        c=con.cursor()
        c.execute("select pass from banking.accounts where username='%s'"%(name))
        l=c.fetchall()
        
        try:
            q=l[0][0]
            if(passd==q):
                return render(request,'option.html')
        except:
            return render(request,'loginpage.html')
        messages.success(request,"Invalid login id pass")
        return render(request,'loginpage.html')
       
            

    
    
def ab(request):
    return render(request,'about.html')
def reg(request):
    global name
    name=request.POST.get('username')
    passwd=request.POST.get('password')
    try:
        con=p.connect(host="localhost",db="banking",user="root",passwd="root",autocommit=True)
        c=con.cursor()
        c.execute("CREATE TABLE `banking`.`%s` (`Date` DATE NOT NULL,`Withdrawal Amount` INT NULL DEFAULT 0,`Deposit Amount` INT NULL DEFAULT 0,`Account Number` INT NULL);"%(name))
        c.execute("Select AccountNumber from `banking`.`accounts` order by `AccountNumber` DESC")
        l=c.fetchone()
        print(l)
        q=int(l[0])
        q+=1
    
        c.execute("Insert into `banking`.`accounts`(`username`,`pass`,`AccountNumber`) values('%s','%s','%s')"%(name,passwd,str(q)))
    except:
        messages.success(request,'User Already exists')
        return render(request,'home.html')

    
    
    return render(request,'home.html')
def dep(request):
    try:
        con=p.connect(host="localhost",db="banking",user="root",passwd="root",autocommit=True)
        c=con.cursor()
        name=request.POST.get('name')
        amt=request.POST.get('amt')
        c.execute("select AccountNumber from banking.accounts where username='%s' "%(name))
        l=c.fetchone()
        c.execute("Insert into `banking`.`%s`(`Date`,`Withdrawal`,`Deposit`,`Account`) values(CURDATE(),0,%d,'%s')"%(name,int(amt),l[0]))
    
        message.success(request,"Sucessfully updated record")
        return render(request,'option.html')
    except:
        messages.success(request,'Please Enter Valid Username and Amount')
        return render(request,'wd.html')

def wth(request):
    return render(request,'wd.html')
def dp(request):
    return render(request,'Deposit.html')
def withd(request):
    try:
        con=p.connect(host="localhost",db="banking",user="root",passwd="root",autocommit=True)
        c=con.cursor()
        name=request.POST.get('name')
        amt=request.POST.get('amt')
        c.execute("select AccountNumber from banking.accounts where username='%s' "%(name))
        l=c.fetchone()
        c.execute("Insert into `banking`.`%s`(`Date`,`Withdrawal`,`Deposit`,`Account`) values(CURDATE(),%d,0,'%s')"%(name,int(amt),l[0]))
    

        return render(request,'option.html')
    except:
        messages.success(request,'Please Enter Valid Username and Amount')
        return render(request,'wd.html')

def all(request):
    return render(request,'all.html')
def bal(request):
    try:
        con=p.connect(host="localhost",db="banking",user="root",passwd="root",autocommit=True)
        c=con.cursor()
        name=request.POST.get('name')
    
        c.execute("select `withdrawal`,`deposit` from `%s`"%(name))
        l=c.fetchall()
        w=0
        d=0
        for i in l:
            w+=i[0]
            d+=i[1]
        b=d-w
        context={
            'balance':b
        }
        return render(request,'bal.html',context)
    except:
        messages.success(request,'Please Enter valid Username')
        return render(request,'all.html')

    
