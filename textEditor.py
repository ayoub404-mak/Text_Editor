from _tkinter import *
from tkinter import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0,END)

def saveFile():
    global filename
    t= text.get(0.0,END)
    f= open(filename,"w")
    f.write(t)
    f.close()

def saveAs():
    f = asksavesfile(mode= 'w', defaultextention='.txt')
    t= text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")

def openFile():
    f= askopenfile(mode='r')
    t= f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

root = Tk()
root.title("My pythone Text Editor")
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)


text= Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filename = Menu(menubar)
filename.add_commond(label="New", command=newFile)
filename.add_commond(label="Open", commond=openFile)
filename.add_commond(label="Save As...", commond=saveAs)
filename.add_separator()
filename.add_commond(label="Quit", common=root.quit)
menubar.add_cascade(label="File", menu=filename)

root.config(menu=menubar)
root.mainloop()