import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import Crypto
from Crypto.Util import Counter
from Crypto import Random
from Crypto.Util.number import *
import libnum

root = Tk()
auth_user = ["Ravi", "Bob",  "Ram", "Ayush", "John", "Kelly"]
uwu = {"Ravi":390314650276167803, "Bob":483710515075373321,  "Ram":860209867719162361, "Ayush":581633013168578947, "John":640621416611553599, "Kelly":488455929614637841}
candidate = ["Bob Ross", "Van Gogh"]
candidate_res = {"Bob Ross":0, "Van Gogh":0}
msg = StringVar()
msg2 = StringVar()
bits = 30

'''f = open("voterauth.txt","r")

for i in f:
    auth_user.append(i)

f.close()'''

# Function to generate key which will be stored in a separate txt file
def keygenerate():
    p = Crypto.Util.number.getPrime(bits,randfunc = Crypto.Random.get_random_bytes)
    q = Crypto.Util.number.getPrime(bits,randfunc= Crypto.Random.get_random_bytes)

    phi = (p-1)*(q-1)
    n = p*q

    e = 65537
    d = (libnum.invmod(e,phi))
    return ((e,n),(d,n))

def encrypt(privkkey,plaintext):
    key,n = privkkey
    cipher = [pow(ord(char),key,n) for char in plaintext]
    return cipher

def decrypt(pubkkey,ciphertext):
    key,n = pubkkey
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

def public_enc(privkkey,data):
    key,n = privkkey
    S = [pow(i,key,n) for i in data]
    return S

def public_dec(pubkkey,data):
    key,n = pubkkey
    D = [pow(i,key,n) for i in data]
    return D

CTFpub,CTFpriv = keygenerate()
user_priv = (0,0)
user_pub = (0,0)

def check(oof,name):
    for i in oof:
        if i == name:
            return True
    return False

def getkey():
    msg2 = ip1.get("1.0",'end-1c')
    msg = ip3.get("1.0",'end-1c')
    msg = int(msg)
    pub = (65537,uwu[msg2])
    priv = (msg,uwu[msg2])
    return (pub,priv)


def BR():
    global  user_priv
    global user_pub
    msg = ip1.get("1.0",'end-1c')
    if check(auth_user,msg):
        if check(existing_user,msg) == False:
            user_pub,user_priv = getkey()
            pt = "Bob Ross"
            user_sign = encrypt(user_priv,pt)
            ct_enc = public_enc(CTFpub,user_sign)
            ct_dec = public_dec(CTFpriv,ct_enc)
            user_dec = decrypt(user_pub,ct_dec)
            if user_dec == pt:
                candidate_res["Bob Ross"]+=1
                existing_user.append(msg)

def VG():
    global user_priv
    global user_pub
    msg = ip1.get("1.0",'end-1c')
    if check(auth_user,msg):
        if check(existing_user,msg) == False:
            user_pub, user_priv = getkey()
            pt = "Van Gogh"
            user_sign = encrypt(user_priv,pt)
            ct_enc = public_enc(CTFpub,user_sign)
            ct_dec = public_dec(CTFpriv,ct_enc)
            user_dec = decrypt(user_pub,ct_dec)
            if user_dec == pt:
                candidate_res["Van Gogh"]+=1
                existing_user.append(msg)



def get_result():
    ip2.delete("1.0",'end-1c')
    for i in candidate:
        upd = i + " " + str(candidate_res[i])
        ip2.insert(END,upd + '\n')


root.geometry("1000x600")
root.title('Vote')

frame1 = Frame(root)
frame2 = Frame(root)

frame1.grid(row=0,column=0,sticky=W)
frame2.grid(row=0,column=1,sticky=E)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

ip1 = Text(frame1,height=5,width=60,wrap=WORD)
ip1.grid(sticky=N)

ip3 = Text(frame1, height = 5, width=60, wrap = WORD)
ip3.grid(sticky=N)

br = tk.Button(frame1, text = "Bob Ross",bg="purple",fg="white", command = BR)
br.grid(sticky = S)
vg = tk.Button(frame1,text = "Van Gogh",bg="green",fg="white",command = VG)
vg.grid(sticky = S)

ip2 = Text(frame2, height = 4, width = 60, wrap = WORD)
ip2.grid(sticky=N)
result = tk.Button(frame2, text = "RANKING",bg="orange",fg="white",command = get_result)
result.grid(sticky = S)
root.mainloop()
