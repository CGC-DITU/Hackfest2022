from tkinter import *
import mysql.connector
window = Tk()
window.title("CALCULATOR")
window.geometry('600x500')
frame = Frame(window)
#frame.pack(side="top", expand=True, fill="both")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="voting"
)

mycursor = mydb.cursor()

'''
'''

def cands():
    #print(1)
    window = Tk()
    window.title("CANDIDATES")
    window.geometry('700x500')

    mycursor.execute("select * from candidates;")
    i=0
    for x in mycursor:
        l2 = Label(window, text=str(x[0]))
        l2.grid(row=i, column=0)
        l2.config(font=('Times new roman', 12))
        l2 = Label(window, text="  Party Name:  ")
        l2.grid(row=i, column=1)
        l2.config(font=('Times new roman', 12))
        l2 = Label(window, text=str(x[1]))
        l2.grid(row=i, column=2)
        l2.config(font=('Times new roman', 12))
        l2 = Label(window, text=" Candidate name : ")
        l2.grid(row=i, column=3)
        l2.config(font=('Times new roman', 12))
        l2 = Label(window, text=str(x[2]))
        l2.grid(row=i, column=4)
        l2.config(font=('Times new roman', 12))
        i=i+1

def vp():
    print(2)
    window1 = Tk()
    window1.title("VOTING PORTAL")
    window1.geometry('600x500')
    frame = Frame(window1)

    def aap():
        #print("aap")
        mycursor.execute("insert into votingPortal(votedTo) values ('aap')")
        mydb.commit()
        window1.destroy()
        window = Tk()
        window.title("SUCCESS")
        window.geometry('500x50')
        l2 = Label(window, text="VOTE REGISTERED SUCCESSFULLY!")
        l2.grid(row=0, column=0)
        l2.config(font=('Times new roman', 12))
        

    def bjp():
        #print("bjp")
        mycursor.execute("insert into votingPortal values ('bjp')")
        mydb.commit()
        window1.destroy()
        window = Tk()
        window.title("SUCCESS")
        window.geometry('500x50')
        l2 = Label(window, text="VOTE REGISTERED SUCCESSFULLY!")
        l2.grid(row=0, column=0)
        l2.config(font=('Times new roman', 12))

    def tmc():
        #print("tmc")
        mycursor.execute("insert into votingPortal values ('tmc')")
        mydb.commit()
        window1.destroy()
        window = Tk()
        window.title("SUCCESS")
        window.geometry('500x50')
        l2 = Label(window, text="VOTE REGISTERED SUCCESSFULLY!")
        l2.grid(row=0, column=0)
        l2.config(font=('Times new roman', 12))

    def nota():
        #print("nota")
        mycursor.execute("insert into votingPortal values ('nota')")
        mydb.commit()
        window1.destroy()
        window = Tk()
        window.title("SUCCESS")
        window.geometry('500x50')
        l2 = Label(window, text="VOTE REGISTERED SUCCESSFULLY!")
        l2.grid(row=0, column=0)
        l2.config(font=('Times new roman', 12))
    

    def ok1():
        #print("vote")
        a=int(t2.get())
        mycursor.execute("select voterDetail.voter_id,candidates.party_name from voterDetail,candidates")
        for x in mycursor:
            #print(x)
            if(x[0]==a):
                l2 = Label(window1, text="select party :")
                l2.grid(row=1, column=0)
                l2.config(font=('Times new roman', 12))

                b1 = Button(window1, text="AAM AADMI PARTY", command=aap, height = 1, width = 20)
                b1.grid(row=5,column=1)
                b2 = Button(window1, text="BHARTIYA JANATA PARTY", command=bjp, height = 1, width = 20)
                b2.grid(row=6,column=1)
                b3 = Button(window1, text="TRINUMUL CONGRESS", command=tmc, height = 1, width = 20)
                b3.grid(row=7,column=1)
                b4 = Button(window1, text="NOTA", command=nota, height = 1, width = 20)
                b4.grid(row=8,column=1)
                
                

    l2 = Label(window1, text="Enter Voter Id :")
    l2.grid(row=0, column=0)
    l2.config(font=('Times new roman', 12))
    t2 = Entry(window1,width=20)
    t2.grid(row=0,column=1)
    b1 = Button(window1, text="OK", command=ok1, height = 1, width = 6)
    b1.grid(row=0,column=2)

    
def res():
    #print(3)
    window = Tk()
    window.title("RESULT")
    window.geometry('600x500')
    l2 = Label(window, text="Total Votes : ")
    l2.grid(row=0, column=0)
    l2.config(font=('Times new roman', 12))
    mycursor.execute("select count(*) from votingPortal;")
    for x in mycursor:
        #print(x[0])
        l2 = Label(window, text=str(x[0]))
        l2.grid(row=0, column=1)
        l2.config(font=('Times new roman', 12))
        
    l3 = Label(window, text="AAM AADMI PARTY Votes : ")
    l3.grid(row=1, column=0)
    l3.config(font=('Times new roman', 12))
    mycursor.execute("select count(*) from votingPortal WHERE votedTo like 'aap';")
    for x in mycursor:
        #print(x[0])
        l4 = Label(window, text=str(x[0]))
        l4.grid(row=1, column=1)
        l4.config(font=('Times new roman', 12))

    l5 = Label(window, text="BHARTIYA JANATA PARTY Votes : ")
    l5.grid(row=2, column=0)
    l5.config(font=('Times new roman', 12))
    mycursor.execute("select count(*) from votingPortal WHERE votedTo like 'bjp';")
    for x in mycursor:
        #print(x[0])
        l6 = Label(window, text=str(x[0]))
        l6.grid(row=2, column=1)
        l6.config(font=('Times new roman', 12))

    l7 = Label(window, text="TRINUMUL CONGRESS Votes : ")
    l7.grid(row=3, column=0)
    l7.config(font=('Times new roman', 12))
    mycursor.execute("select count(*) from votingPortal WHERE votedTo like 'tmc';")
    for x in mycursor:
        #print(x[0])
        l8 = Label(window, text=str(x[0]))
        l8.grid(row=3, column=1)
        l8.config(font=('Times new roman', 12))

    l9 = Label(window, text="NOTA Votes : ")
    l9.grid(row=4, column=0)
    l9.config(font=('Times new roman', 12))
    mycursor.execute("select count(*) from votingPortal WHERE votedTo like 'nota';")
    for x in mycursor:
        #print(x[0])
        l10 = Label(window, text=str(x[0]))
        l10.grid(row=4, column=1)
        l10.config(font=('Times new roman', 12))

        
'''
'''
    
def sub():
    def vote_option():
        #print(0)
        b1 = Button(window, text="CANDIDATES", command=cands, height = 1, width = 20)
        b1.grid(row=4,column=0)

        b1 = Button(window, text="VOTING PORTAL", command=vp, height = 1, width = 20)
        b1.grid(row=4,column=1)

        b1 = Button(window, text="RESULT", command=res, height = 1, width = 20)
        b1.grid(row=4,column=2)

        
    user_id=t1.get()
    pssd=t2.get()
    if(user_id=='1000013899' and pssd=='8250'):
        vote_option()
    else:
        window1 = Tk()
        window1.title("TRY AGAIN")
        window1.geometry('200x50')
        l1 = Label(window1, text="INCORRECT PASSWORD")
        l1.grid(row=1, column=0)
        l1.config(font=('Times new roman', 12))
        window.destroy()

l1 = Label(window, text="VOTING MACHINE")
l1.grid(row=0, column=0)

l1 = Label(window, text="Enter admin id : ")
l1.grid(row=1, column=0)
l1.config(font=('Times new roman', 12))

t1 = Entry(window,width=20)
t1.grid(row=1,column=1)


l2 = Label(window, text="Enter password : ")
l2.grid(row=2, column=0)
l2.config(font=('Times new roman', 12))

t2 = Entry(window,width=20,show="*")
t2.grid(row=2,column=1)

b1 = Button(window, text="SUBMIT", command=sub, height = 1, width = 6)
b1.grid(row=3,column=2)
