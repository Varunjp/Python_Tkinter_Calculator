from tkinter import *

# window section ---------------------------

Window = Tk()
Window.title("Calculator")
Window.geometry("400x500")
Window.configure(bg="#2e76e8")

# window section ---------------------------

# text area -----------------------------------

text_area = Label(Window,bg="#b4c2a9",width="55",height="4")
text_area.grid(row=0,column=0, columnspan=4,padx=5,pady=10)


# text area ------------------------------------

# Buttons ---------------------------------------

button7 = Button(Window, text="7", width=10, height=2)
button7.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(Window, text="4", width=10, height=2)
button4.grid(row=2, column=0, padx=10, pady=10)

button1 = Button(Window, text="1", width=10, height=2)
button1.grid(row=3, column=0, padx=10, pady=10)

buttondot = Button(Window, text=".", width=10, height=2)
buttondot.grid(row=4, column=0, padx=10, pady=10)

button8 = Button(Window, text="8", width=10, height=2)
button8.grid(row=1, column=1, padx=10, pady=10)

button5 = Button(Window, text="5", width=10, height=2)
button5.grid(row=2, column=1, padx=10, pady=10)

button2 = Button(Window, text="2", width=10, height=2)
button2.grid(row=3, column=1, padx=10, pady=10)

button0 = Button(Window, text="0", width=10, height=2)
button0.grid(row=4, column=1, padx=10, pady=10)

button9 = Button(Window, text="9", width=10, height=2)
button9.grid(row=1, column=2, padx=10, pady=10)

button6 = Button(Window, text="6", width=10, height=2)
button6.grid(row=2, column=2, padx=10, pady=10)

button3 = Button(Window, text="3", width=10, height=2)
button3.grid(row=3, column=2, padx=10, pady=10)

button_del = Button(Window, text="del", width=10, height=2)
button_del.grid(row=4, column=2, padx=10, pady=10)

button_div = Button(Window, text="/", width=10, height=2)
button_div.grid(row=1, column=3, padx=10, pady=10)

button_mul= Button(Window, text="x", width=10, height=2)
button_mul.grid(row=2, column=3, padx=10, pady=10)

button_sub = Button(Window, text="-", width=10, height=2)
button_sub.grid(row=3, column=3, padx=10, pady=10)

button_add = Button(Window, text="+", width=10, height=2)
button_add.grid(row=4, column=3, padx=10, pady=10)

# Buttons ---------------------------------------

Window.mainloop()