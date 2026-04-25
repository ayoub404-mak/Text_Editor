"""
Text Editor Application

A simple text editor built with Python's tkinter library.
Provides basic file operations: new, open, save, and save as.
"""

from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror

# Global variable to store the current filename
filename = None


def newFile():
    """
    Create a new empty file.

    Sets the filename to 'Untitled' and clears the text area.
    """
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def saveFile():
    """
    Save the current content to the open file.

    Writes the entire text content to the file specified by filename.
    """
    global filename
    t = text.get(0.0, END)
    f = open(filename, "w")
    f.write(t)
    f.close()


def saveAs():
    """
    Save the current content to a new file.

    Opens a file dialog to choose the save location and filename.
    Handles errors if the save operation fails.
    """
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
        f.close()
    except AttributeError:
        # User cancelled the dialog
        pass
    except:
        showerror(title="Oops!", message="Unable to save file...")


def openFile():
    """
    Open an existing file.

    Opens a file dialog to select a file and displays its content.
    """
    f = askopenfile(mode='r')
    if f:
        t = f.read()
        f.close()
        text.delete(0.0, END)
        text.insert(0.0, t)


# Create the main application window
root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

# Create and pack the text widget
text = Text(root, width=400, height=400)
text.pack()

# Create the menu bar
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Configure and display the menu bar
root.config(menu=menubar)

# Start the main event loop
root.mainloop()