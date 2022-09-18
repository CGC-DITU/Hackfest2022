from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def bill(request):
    return render(request,'inpput.html')
def lodu(request):
    if request.method=="POST":
        u=request.POST.get('u')
        name=request.POST.get('n')
        cid=request.POST.get('cid')
    if(u=='None' or u==None):
        context={
            'name':'Invalid input',
            'bijli': 'Invalid Input',
            'cid': 'Invalid Input',

        }
        return render(request,'output.html',context)
    try:
        p=int(u)
        s=0
        a=50*2
        b=150*2.5
        c=200*3
        d=100*3.5
    
        s=0
        if(p<=50):
            s=s+p*2
        elif(p>50 and p<=200):
            s=s+a+(p-50)*2.5
        elif(p>200 and p<=400):
            s=s+a+b+(p-200)*3.0
        elif(p>400 and p<=500):
            s=s+a+b+c+(p-400)*3.5
        else:
            s=s+a+b+c+d+(p-500)*4
        context={
            'name':name,
            'bijli': s,
            'cid': cid,
        }

        return render(request,'output.html',context)
    except:
        context={
            'name':'Invalid input',
            'bijli': 'Invalid Input',
            'cid': 'Invalid Input',

        }
        return render(request,'output.html',context)
