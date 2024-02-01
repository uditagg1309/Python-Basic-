# Step 1 Import Module
from tkinter import *
from translate import Translator

# Step 2 Create display window

window = Tk()
window.title("Language Translator")
window.geometry("500x500")
window.resizable(0,0)
window.config(bg = "aqua")

# Step 3 define options menu
#Input Widget
inputchoice = StringVar()
inputchoice.set("English")
langchoices1 = OptionMenu(window,inputchoice,"Hindi", "English", "French", "German", "Spanish")
langchoices1.config(bg = "yellow", fg = "black")
langchoices1["menu"].config(bg = "Red")
langchoices1.grid(row = 2, column = 1, pady = 10, ipadx = 15)

#Output Widget
outputchoice = StringVar()
outputchoice.set("Choose here")
langchoices2 = OptionMenu(window,outputchoice,"Hindi", "English", "French", "German", "Spanish")
langchoices2.config(bg = "yellow", fg = "black")
langchoices2["menu"].config(bg = "Red")
langchoices2.grid(row = 2, column = 3, ipadx = 15)

# Step 4 Create input and output
#input
Label(window, text = "Enter text Here ").grid(row = 3, column = 0)
TextVar = StringVar()
Textbox = Entry(window, textvariable=TextVar).grid(row = 3, column = 1, ipadx=15, ipady=20)
#output
Label(window, text = "Output text ").grid(row = 3, column = 2)
OutVar = StringVar()
Textbox = Entry(window, textvariable=OutVar).grid(row = 3, column = 3, ipadx=15, ipady=20)

# Step 5 Define function
def Translate():
    translator = Translator(from_lang = inputchoice.get(), to_lang = outputchoice.get())
    translation = translator.translate(TextVar.get())
    OutVar.set(translation)


# Step 6 create translation button
# Button for calling function
B = Button(window, text = "translate", command = Translate, relief=GROOVE).grid(row = 4, column = 2)

window.mainloop()
