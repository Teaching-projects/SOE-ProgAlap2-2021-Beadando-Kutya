from tkinter import *
from tkinter import filedialog

window = Tk()
window.title('Text Editor')

global nickel
nickel = False

global ezvan
ezvan = False


def new_file():
    szoveg.delete("1.0", END)
    window.title("New File")
    sb.config(text="New File        ")
    global nickel
    nickel = False


def open_file():
    szoveg.delete("1.0", END)
    bevesz = filedialog.askopenfile(
        filetypes=(("Text Files", "*.txt"), ("JSON Files", "*.json"), ("All Files", "*.*")))
    name = bevesz
    if bevesz:
        global nickel
        nickel = bevesz
    sb.config(text=f'{name}        ')
    window.title(f'{name}')
    x = bevesz.read()
    szoveg.insert(END, x)
    bevesz.close()


def save_as():
    szoveg2 = filedialog.asksaveasfilename(
        defaultextension=".*", title="Save File",
        filetypes=(("Text Files", "*.txt"), ("JSON Files", "*.json"), ("All Files", "*.*")))

    name = szoveg2
    sb.config(text=f'Saved: {name}        ')
    window.title(f'{name}')
    szoveg2 = open(szoveg2, "w")
    szoveg2.write(szoveg.get("1.0", END))
    szoveg2.close()


def save_file():
    global nickel
    if nickel:
        szoveg3 = open(nickel.name, "w")
        szoveg3.write(szoveg.get("1.0", END))
        szoveg3.close()
        sb.config(text=f'Saved: {nickel}        ')
    else:
        save_as()


def cut(e):
    global ezvan
    if szoveg.selection_get():
        ezvan = szoveg.selection_get()
        szoveg.delete("sel.first", "sel.last")
        window.clipboard_clear()
        window.clipboard_append(ezvan)


def copy(e):
    global ezvan
    if szoveg.selection_get():
        ezvan = szoveg.selection_get()
        window.clipboard_clear()
        window.clipboard_append(ezvan)


def paste(e):
    global ezvan

    if ezvan:
        position = szoveg.index(INSERT)
        szoveg.insert(position, ezvan)


keret = Frame(window)
keret.pack(pady=5)

text_scroll = Scrollbar(keret)
text_scroll.pack(side=RIGHT, fill=Y)

szoveg = Text(keret, width=97, font=("Helvetica", 16), selectbackground="blue",
              selectforeground="white", undo=True, yscrollcommand=text_scroll.set)
szoveg.pack()

text_scroll.config(command=szoveg.yview)

my_menu = Menu(window)
window.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut(1))
edit_menu.add_command(label="Copy", command=lambda: copy(1))
edit_menu.add_command(label="Paste", command=lambda: paste(1))
edit_menu.add_command(label="Undo", command=szoveg.edit_undo)
edit_menu.add_command(label="Redo", command=szoveg.edit_redo)

sb = Label(window, text="Ready        ")
sb.pack(fill=X, side=BOTTOM, ipady=5)

window.mainloop()
