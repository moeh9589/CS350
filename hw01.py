from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser


def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    return color_code


def is_checked():
    return check_box.get()


def clear_textbox():
    text.delete(1.0, "end")


def open_file():
    chosen_file = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/CS350",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    file_name.insert(END, chosen_file)
    chosen_file = open(chosen_file)  # or tf = open(tf, 'r')
    data = chosen_file.read()

    text.insert(END, data)
    chosen_file.close()


# find logic taken from https://www.geeksforgeeks.org/search-string-in-text-using-python-tkinter/
def find():
    text.tag_remove('found', '1.0', END)

    s = find_text.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=is_checked(), stopindex=END)
            if not idx:
                break

            lastidx = '%s+%dc' % (idx, len(s))

            text.tag_add('found', idx, lastidx)
            idx = lastidx

        text.tag_config('found', background='red')
    find_text.focus_set()


win = Tk()
win.title("Finder")
win.geometry("550x550")

frame = Frame(win, pady=10)

file_name = Entry(frame)
file_name.pack(side=LEFT, expand=1)
file_str = file_name.get()
file_name.focus_set()
# print(str(file_str))

file_button = Button(frame, text="Open File")
file_button.pack(side=LEFT)

Label(frame, text='Text to find:').pack(side=LEFT)

find_text = Entry(frame)
find_text.pack(side=LEFT, expand=1)

find_button = Button(frame, text='Find')
find_button.pack(side=LEFT)

frame.pack(side=TOP)

text = Text(win, width=50, height=20)
text.insert('1.0', "")

Button(win, text="Clear", command=clear_textbox).pack(pady=5)

text.pack(side=LEFT, pady=20, expand=True)

sb = Scrollbar(win)
sb.pack(side=RIGHT, fill=Y, padx=5)

text.config(yscrollcommand=sb.set)
sb.config(command=text.yview)

check_box = IntVar()
Checkbutton(win, text="Match Case", variable=check_box, onvalue=0, offvalue=1, command=is_checked)\
    .place(x=225, y=500)

find_button.config(command=find)
file_button.config(command=open_file)


win.mainloop()
