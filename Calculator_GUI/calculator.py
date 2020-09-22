from tkinter import *
import parser
import math

# Parser help us to solve mathematical operation

root = Tk()
root.title('CALCULATOR')
root.geometry('670x450')
root.configure(bg='Blue')

# get the user input and place it in the text field
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)

    except EXCEPTION:
        clear_all()
        display.insert(0, "ERROR")


def factorial():
    n = int(display.get())
    fact = math.factorial(n)
    clear_all()
    display.insert(0, fact)


# adding functionality
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# deleting entire elements on the screen
def clear_all():
    display.delete(0, END)


# deleting single element on the screen
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "ERROR")


# adding the input field

display = Entry(root, font=('Helvetica', '40'))
display.grid(row=1, columnspan=6, padx=45, pady=35, sticky=W + E)

# adding buttons to calculator
Button(root, text="1", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(1)).grid(row=2, column=0)
Button(root, text="2", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(2)).grid(row=2, column=1)
Button(root, text="3", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(3)).grid(row=2, column=2)

Button(root, text="4", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="5", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="6", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(6)).grid(row=3, column=2)

Button(root, text="7", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(7)).grid(row=4, column=0)
Button(root, text="8", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(8)).grid(row=4, column=1)
Button(root, text="9", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(9)).grid(row=4, column=2)

# adding other buttons to the calculator
Button(root, text="AC", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text="=", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("+")).grid(row=2,
                                                column=3)
Button(root, text="-", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("-")).grid(row=3,
                                                column=3)
Button(root, text="*", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("*")).grid(row=4,
                                                column=3)
Button(root, text="/", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("/")).grid(row=5,
                                                column=3)

# adding new operations
Button(root, text="pi", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("*3.14")).grid(row=2,
                                                    column=4)
Button(root, text="%", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("%")).grid(row=3,
                                                column=4)
Button(root, text="(", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("(")).grid(row=4,
                                                column=4)
Button(root, text="exp", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("**")).grid(row=5,
                                                 column=4)

Button(root, text=">-", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: undo()).grid(row=2, column=5)
Button(root, text="!", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: factorial()).grid(row=3, column=5)
Button(root, text=")", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation(")")).grid(row=4,
                                                column=5)
Button(root, text="^2", bg="Black", fg="White", padx=25, pady=13, font=('Helvetica', '20'),
       command=lambda: get_operation("**2")).grid(row=5,
                                                  column=5)

root.mainloop()