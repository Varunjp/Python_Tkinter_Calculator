from tkinter import *

# window section ---------------------------

Window = Tk()
Window.title("Calculator")
Window.geometry("400x400")
Window.configure(bg="#2e76e8")

# window section ---------------------------

# text area -----------------------------------

text_area = Label(Window,bg="#b4c2a9",width="55",height="4")
text_area.grid(row=0,column=0, columnspan=4,padx=5,pady=10)


# text area ------------------------------------

# Buttons ---------------------------------------

button7 = Button(Window, text="7", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button7.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(Window, text="4", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button4.grid(row=2, column=0, padx=10, pady=10)

button1 = Button(Window, text="1", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button1.grid(row=3, column=0, padx=10, pady=10)

buttondot = Button(Window, text=".", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
buttondot.grid(row=4, column=0, padx=10, pady=10)

button8 = Button(Window, text="8", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button8.grid(row=1, column=1, padx=10, pady=10)

button5 = Button(Window, text="5", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button5.grid(row=2, column=1, padx=10, pady=10)

button2 = Button(Window, text="2", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button2.grid(row=3, column=1, padx=10, pady=10)

button0 = Button(Window, text="0", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button0.grid(row=4, column=1, padx=10, pady=10)

button9 = Button(Window, text="9", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button9.grid(row=1, column=2, padx=10, pady=10)

button6 = Button(Window, text="6", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button6.grid(row=2, column=2, padx=10, pady=10)

button3 = Button(Window, text="3", width=10, height=2, bg="#0dd0d4",activeforeground="white", activebackground="#044d57")
button3.grid(row=3, column=2, padx=10, pady=10)

button_equal = Button(Window, text="=", width=10, height=2, bg="#0ce80c",activeforeground="white", activebackground="#048c04")
button_equal.grid(row=4, column=2, padx=10, pady=10)

button_div = Button(Window, text="/", width=10, height=2, bg="#cade1b",activeforeground="white", activebackground="#838a04")
button_div.grid(row=1, column=3, padx=10, pady=10)

button_mul= Button(Window, text="x", width=10, height=2, bg="#cade1b",activeforeground="white", activebackground="#838a04")
button_mul.grid(row=2, column=3, padx=10, pady=10)

button_sub = Button(Window, text="-", width=10, height=2, bg="#cade1b",activeforeground="white", activebackground="#838a04")
button_sub.grid(row=3, column=3, padx=10, pady=10)

button_add = Button(Window, text="+", width=10, height=2, bg="#cade1b",activeforeground="white", activebackground="#838a04")
button_add.grid(row=4, column=3, padx=10, pady=10)

button_del = Button(Window, text="del", width=25, height=2, bg="#f20905",activeforeground="white", activebackground="#8a0606")
button_del.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

button_back = Button(Window, text="back", width=25, height=2, bg="#e8760c",activeforeground="white", activebackground="orange")
button_back.grid(row=5, column=2, columnspan=2, padx=5, pady=10)

# Buttons ---------------------------------------

Window.mainloop()