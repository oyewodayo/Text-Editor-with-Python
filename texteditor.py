from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.filedialog import asksaveasfile 

filename = None

root = Tk()
root.title('Penpad by Temidayo')
root.iconbitmap('C:/Users/HP/Desktop/python/TextEditor/temidayo.ico')

editor_height = root.winfo_screenwidth()
editor_width =root.winfo_screenheight()
root.geometry(f'{editor_width}x{editor_height}')



def newFile():
    global filename
    filename = "untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save files...")

def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create SCrollbar for the TextBox
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame,width=97, height=25, font=("Helvetical", 14), selectbackground="yellow", selectforeground= "black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure SCrollBar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New" command=newFile)
file_menu.add_command(label="Open",command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_command(label="Save As", command=saveAs)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Find")


# Add Status Bar To Bottom of Editor
status_bar = Label(root, text='Ready  ',  anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)




root.mainloop()




