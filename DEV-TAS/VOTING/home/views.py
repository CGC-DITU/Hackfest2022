from re import L
from urllib import response
from django.shortcuts import render
from django.shortcuts import HttpResponse
import pymysql as m
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import HttpResponse,render
from datetime import datetime

from django.contrib import messages
# Create your views here.
def index(request):
    
    return render(request,'home.html')


def admin(request):
    con=m.connect(host="localhost",db="vms",user="root",passwd="root",autocommit=True)
    c=con.cursor()
    c.execute("SELECT * FROM vms.admin;")
    l=c.fetchall()
    print(request.method)
    if request.method=="POST":
        sid=request.POST.get('serviceid')
        name=request.POST.get('name')
        passd=request.POST.get('passd')
        
    
    
    
    for i in l:
        if(i[0]==name and int(i[1])== int(sid) and i[2]==passd):
            return render(request,'admin.html')
    
    messages.error(request,"Invalid Passwd")
    
    return render(request,'Invalid.html')


def adminlog(request):
    
    
    return render(request,'adminlog.html')
def cand(request):
    return render(request,'candi.html')
def candreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        pn=request.POST.get('pn')
        yi=request.POST.get('year')
        party=request.POST.get('party')
        
 
    con=m.connect(host="localhost",db="vms",user="root",passwd="root",autocommit=True)
    c=con.cursor()
    c.execute("select party from vms.candidates")
    

    l=c.fetchall()
    for i in l:
            if(party==i[0]):
                return render(request,'already.html')
    c.execute("INSERT INTO `vms`.`candidates` (`name`, `phone_number`, `party`, `yearly_income`) VALUES ('%s', '%s', '%s', '%d');"%(name,pn,party,int(yi)))
    con.commit()
    con.close()
    
       
    
    
    
    return render(request,'home.html')
 

