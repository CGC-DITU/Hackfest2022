import datetime
from cryptography.fernet import Fernet
from tkinter import *
window = Tk()
window.title("ENCRYPTION AND DECRYPTION")
window.geometry('398x101')


key = Fernet.generate_key() 
fernet = Fernet(key)
'''
'''
def enc():
    window = Tk()
    window.title("ENCRYPTION WINDOW")
    window.geometry('600x500')

    def sub():
        input_message_encrypt=t1.get("1.0", "end-1c")

        encMessage = fernet.encrypt(input_message_encrypt.encode())
 

        l2 = Label(window, text="Message after encrypt :  ")
        l2.grid(row=3, column=0)
        l2.config(font=('Times new roman', 16))


        T = Text(window, height = 5, width = 57)
        T.grid(row=4,column=0)
        T.config(font=('Times new roman', 15))
        T.insert(END, encMessage)

        l3 = Label(window, text="*copy message for future use")
        l3.grid(row=5, column=0)
        l3.config(font=('Times new roman', 10))

    
    l1 = Label(window, text="Enter message to encrypt :  ")
    l1.grid(row=0, column=0)
    l1.config(font=('Times new roman', 16))
    l1.grid(padx=(0, 0), pady=(20, 0))

    t1 = Text(window, height = 5,width = 57)
    t1.grid(row=1,column=0)
    t1.config(font=('Times new roman', 15))

    b1 = Button(window, text="SUBMIT", command=sub, height = 2, width = 20)
    b1.grid(row=2,column=0)

    

def dec():
    window = Tk()
    window.title("DECRYPTION WINDOW")
    window.geometry('600x500')

    def sub():
        input_message_decrypt=t1.get("1.0", "end-1c")
        key = Fernet.generate_key()

        decMessage = fernet.decrypt(input_message_decrypt).decode()
        #print("decrypted string: ", decMessage)
 
        #print("original string: ", input_message_encrypt)
        #print("encrypted string: ", encMessage)

        l2 = Label(window, text="Message after encrypt :  ")
        l2.grid(row=3, column=0)
        l2.config(font=('Times new roman', 16))


        T = Text(window, height = 5, width = 57)
        T.grid(row=4,column=0)
        T.config(font=('Times new roman', 15))
        T.insert(END, decMessage)

        l3 = Label(window, text="*copy message for future use")
        l3.grid(row=5, column=0)
        l3.config(font=('Times new roman', 10))


    l1 = Label(window, text="Enter encrypted message to decrypt :  ")
    l1.grid(row=0, column=0)
    l1.config(font=('Times new roman', 16))
    l1.grid(padx=(0, 0), pady=(20, 0))

    t1 = Text(window, height = 5,width = 57)
    t1.grid(row=1,column=0)
    t1.config(font=('Times new roman', 15))

    b1 = Button(window, text="SUBMIT", command=sub, height = 2, width = 20)
    b1.grid(row=2,column=0)

v = StringVar()
b1 = Button(window, text="ENCRYPT", command=enc, height = 6, width = 27)
b1.grid(row=0,column=0)

b1 = Button(window, text="DECRYPT", command=dec, height = 6, width = 27)
b1.grid(row=0,column=1)
