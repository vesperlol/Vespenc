# btw Idc about pep8 standards, so if you dont like my code, idc and you can go f*ck y0urs3lf
import base64, zlib, pyperclip
from codecs import decode
from tkinter import *
from tkinter import messagebox
window = Tk();window.title("Vespenc || vesper#0003");window.geometry("632x557");window.maxsize(632, 557);window.minsize(632, 557);window.iconbitmap("assets/mylogo.ico")
bg=PhotoImage(file='assets/background.png');copy=PhotoImage(file='assets/img1.png');ENCODE=PhotoImage(file='assets/img0.png');DECODE=PhotoImage(file='assets/img3.png')
class Vespenc:
    def __init__(self):
        bgg = Label(window, image=bg, borderwidth=0);bgg.place(x=0, y=0)
        self.textenc = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#1A0535',width=38,borderwidth=0);self.textenc.place(x=210, y=182)
        self.passenc = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#1A0535',width=46,borderwidth=0);self.passenc.place(x=210, y=219)
        copybutton1 = Button(window, image=copy,bg='#01001B',borderwidth=0, activebackground="#01001B",command=self.copy1);copybutton1.place(x=488,y=180)
        encode = Button(window, image=ENCODE,bg='#01001B',borderwidth=0, activebackground="#01001B",command=self.encoder);encode.place(x=225,y=260)
        self.textdec = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#1A0535',width=38,borderwidth=0);self.textdec.place(x=210, y=387)
        self.passdec = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#1A0535',width=46,borderwidth=0);self.passdec.place(x=210, y=424)
        copybutton2 = Button(window, image=copy,bg='#01001B',borderwidth=0, activebackground="#01001B",command=self.copy2);copybutton2.place(x=488,y=385)
        decodee = Button(window, image=DECODE,bg='#01001B',borderwidth=0, activebackground="#01001B",command=self.decoder);decodee.place(x=225,y=465)
    def copy1(self):pyperclip.copy(self.textenc.get());messagebox.showinfo("Vespenc || vesper#0003", 'Text Copied')
    def encoder(self):
        msg = base64.b16encode(zlib.compress(str(self.textenc.get()+"_()_"+self.passenc.get()).encode())).decode()
        enc = msg.replace('0','_IllIllIlIllIllIlIllllIIlIIIlIIllIIlI').replace('1','_IllIllIlIllIllIlIllllIIlIIIlIIllIIll').replace('2','_lllIllIlIllIllIlIllllIIlIIIlIIllIIll').replace('3','_IIIIllIlIllIllIlIllllIIlIIIlIIllIIll').replace('4','_lllIllIlIllIllIlIlllllllIIIlIIllIIll').replace('5','_lllIlIIlIllIllIlIllIIIIlIIIlIIllIIll').replace('6','_IllIllIlIllIllIlIllllIIlIIIlIlllIlll').replace('7','_lllIlllIIllIllllIllllIIlIIIlIIllIIll').replace('8','_lllIllIlIllIllIlIIIIlIIlIIIlIIllIIll').replace('9','_IIIIllIlIllIllIlIllllIIIIIIlIIllIIll').replace('A','_lllIllllIlllllIlIllllIIlIIIIIIllIlll').replace('B','_lllIllIllllIlllIIlllllIlIIIlIIllIIll').replace('C','_lllIllIlIllIllIIIllllIIlllIIIIllIIll').replace('D','_lllIllIlIllIllIlIllllIIlIIIIllIlllII').replace('E','_IIlIllIlIllIlIIlIlIIIIIlIlIlIIllIlll').replace('F','_lIIlllllIllIllIlIllIIIllIIIlIIllIIII')
        self.textenc.delete(0, END);self.textenc.insert(END,enc)
    def copy2(self):pyperclip.copy(self.textdec.get());messagebox.showinfo("Vespenc || vesper#0003", 'Text Copied')
    def decoder(self):
        try:
            dec = str(self.textdec.get()).replace('_IllIllIlIllIllIlIllllIIlIIIlIIllIIlI','0').replace('_IllIllIlIllIllIlIllllIIlIIIlIIllIIll','1').replace('_lllIllIlIllIllIlIllllIIlIIIlIIllIIll','2').replace('_IIIIllIlIllIllIlIllllIIlIIIlIIllIIll','3').replace('_lllIllIlIllIllIlIlllllllIIIlIIllIIll','4').replace('_lllIlIIlIllIllIlIllIIIIlIIIlIIllIIll','5').replace('_IllIllIlIllIllIlIllllIIlIIIlIlllIlll','6').replace('_lllIlllIIllIllllIllllIIlIIIlIIllIIll','7').replace('_lllIllIlIllIllIlIIIIlIIlIIIlIIllIIll','8').replace('_IIIIllIlIllIllIlIllllIIIIIIlIIllIIll','9').replace('_lllIllllIlllllIlIllllIIlIIIIIIllIlll','A').replace('_lllIllIllllIlllIIlllllIlIIIlIIllIIll','B').replace('_lllIllIlIllIllIIIllllIIlllIIIIllIIll','C').replace('_lllIllIlIllIllIlIllllIIlIIIIllIlllII','D').replace('_IIlIllIlIllIlIIlIlIIIIIlIlIlIIllIlll','E').replace('_lIIlllllIllIllIlIllIIIllIIIlIIllIIII','F')
            msg = zlib.decompress(base64.b16decode(dec)).decode()
            if self.passdec.get() == msg.split("_()_")[1]:self.textdec.delete(0, END);self.textdec.insert(END,msg.split("_()_")[0])
            else:messagebox.showerror("Vespenc || vesper#0003","Invalid Password")
        except:messagebox.showerror("Vespenc || vesper#0003","Invalid Password or Invalid Encoded Text")
Vespenc()
window.mainloop()