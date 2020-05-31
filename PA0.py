from tkinter import *

#This Function will be executed when Encrypt Button is clicked
def Encrypt():
    dec.delete(1.0,END)          #Empty the text present in dec text box
    s = enc.get("1.0",'end-1c')  #Take the input from enc text box
    ans = ""
    for i in s:                  #Iterate through every character in the input
        if i>='a' and i<='z':
            i = chr(ord('z')+ord('a')-ord(i))
        elif i>='A' and i<='Z':
            i = chr(ord('A')+ord('Z')-ord(i))
        ans = ans + str(i)
    dec.insert(0.0,ans)

#This Function will be executed when Decrypt Button is clicked
def Decrypt():
    enc.delete(1.0,END)          #Empty the text present inn enc text box
    s = dec.get("1.0",'end-1c')  #Take the input from dec text box
    ans = ""
    for i in s:                  #Iterate through every character in the input
        if i>='a' and i<='z':
            i = chr(219-ord(i))
        elif i>='A' and i<='Z':
            i = chr(155-ord(i))
        ans = ans + str(i)
    enc.insert(0.0,ans)

# Used tkinter for creating the UI

root = Tk()
root.geometry("1000x600")
root.title('EncodeIt')

#Creating the Frames in which we will insert Text Boxes and Buttons
frame1 = Frame(root)
frame2 = Frame(root)

frame1.grid(row=0,column=0,sticky=W)
frame2.grid(row=0,column=1,sticky=E)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

#Creating the Text Boxes
enc = Text(frame1,height=30,width=75,wrap=WORD)
dec = Text(frame2,height=30,width=75,wrap=WORD)
enc.grid(sticky=W)
dec.grid(sticky=E)

#Creating the Buttons
btn1 = Button(frame1,text='Encrypt',bg="purple",fg="white",command=Encrypt)
btn2 = Button(frame2,text='Decrypt',bg="green",fg="white",command=Decrypt)
btn1.grid(sticky=S)
btn2.grid(sticky=S)

root.mainloop()
