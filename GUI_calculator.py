from tkinter import *

# window section ---------------------------

Window = Tk()
Window.title("Calculator")
Window.geometry("400x380")
Window.configure(bg="#2e76e8")

# window section ---------------------------

# Button click function ----------------------

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

# def btn_back():
#     global expression
#     expression = expression.delete[-1]

expression = ""

# Button click function ----------------------

# text area -----------------------------------

input_text = StringVar()

input_frame = Frame(Window, width=400, height=10, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

text_area = Entry(input_frame, bg="#eee",width="50", font=('arial', 18, 'bold'), textvariable=input_text, justify=RIGHT)
text_area.grid(row=0, column=0)
text_area.pack(ipady=10)


# text area ------------------------------------

# Buttons ---------------------------------------

btn_frame = Frame(Window, width=400, height=348, bg="#2e76e8")
btn_frame.pack()

button7 = Button(btn_frame, text="7", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(7)).grid(row=0, column=0, padx=10, pady=10)

button4 = Button(btn_frame, text="4", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(4)).grid(row=1, column=0, padx=10, pady=10)

button1 = Button(btn_frame, text="1", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(1)).grid(row=2, column=0, padx=10, pady=10)

buttondot = Button(btn_frame, text=".", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                   activebackground="#044d57", command=lambda : btn_click(".")).grid(row=3, column=0, padx=10, pady=10)

button8 = Button(btn_frame, text="8", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(8)).grid(row=0, column=1, padx=10, pady=10)

button5 = Button(btn_frame, text="5", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(5)).grid(row=1, column=1, padx=10, pady=10)

button2 = Button(btn_frame, text="2", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(2)).grid(row=2, column=1, padx=10, pady=10)

button0 = Button(btn_frame, text="0", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(0)).grid(row=3, column=1, padx=10, pady=10)

button9 = Button(btn_frame, text="9", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(9)).grid(row=0, column=2, padx=10, pady=10)

button6 = Button(btn_frame, text="6", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(6)).grid(row=1, column=2, padx=10, pady=10)

button3 = Button(btn_frame, text="3", width=10, height=2, bg="#0dd0d4",activeforeground="white",
                 activebackground="#044d57", command=lambda : btn_click(3)).grid(row=2, column=2, padx=10, pady=10)

button_equal = Button(btn_frame, text="=", width=10, height=2, bg="#0ce80c",activeforeground="white",
                      activebackground="#048c04", command=lambda : btn_equal()).grid(row=3, column=2, padx=10, pady=10)

button_div = Button(btn_frame, text="/", width=10, height=2, bg="#cade1b",activeforeground="white",
                    activebackground="#838a04", command=lambda : btn_click("/")).grid(row=0, column=3, padx=10, pady=10)

button_mul= Button(btn_frame, text="x", width=10, height=2, bg="#cade1b",activeforeground="white",
                   activebackground="#838a04", command=lambda : btn_click("*")).grid(row=1, column=3, padx=10, pady=10)

button_sub = Button(btn_frame, text="-", width=10, height=2, bg="#cade1b",activeforeground="white",
                    activebackground="#838a04", command=lambda : btn_click("-")).grid(row=2, column=3, padx=10, pady=10)

button_add = Button(btn_frame, text="+", width=10, height=2, bg="#cade1b",activeforeground="white",
                    activebackground="#838a04", command=lambda : btn_click("+")).grid(row=3, column=3, padx=10, pady=10)

button_del = Button(btn_frame, text="del", width=25, height=2, bg="#f20905",activeforeground="white",
                    activebackground="#8a0606", command=lambda : btn_clear()).grid(row=4, column=0, columnspan=2, padx=5, pady=10)

button_back = Button(btn_frame, text="back", width=25, height=2, bg="#e8760c",activeforeground="white",
                     activebackground="orange").grid(row=4, column=2, columnspan=2, padx=5, pady=10)

# Buttons ---------------------------------------

Window.mainloop()