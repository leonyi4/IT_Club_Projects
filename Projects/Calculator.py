# Instructions from this website: https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

import tkinter as tk

expression = ""

# Function to update expression
# in the text entry box
# pressing each number
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

# Clearing the calculator
def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Calculating the expression
def equalpress():

    # Try and except statement is used for handling the errors like zero division error etc.
    # Put that code inside the try block which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Code to set the driver to main. More info here: https://towardsdatascience.com/python-main-b729fab7a8c3#:~:text=Before%20executing%20a%20program%2C%20the,__name__%20will%20vary.
if __name__ == "__main__":

    root = tk.Tk()  # start the Tk class
    root.configure(background="black")  # configure background to black,
    root.title("Calculator GUI")  # set the title
    root.geometry("265x150")  # set it to 265x150 dimensions

    # Initiates the tk.StringVar object
    equation = tk.StringVar()
    # Makes a new text field - 1st row
    expression_field = tk.Entry(root, textvariable=equation)
    # four column, ipadx for the size of the text field
    expression_field.grid(columnspan=4, ipadx=70)

    # Define the buttons

    # ( ) %
    button_left_bracket = tk.Button(root, text='(', fg='black', bg='white', command=lambda: press('('), height=1, width=7)
    button_right_bracket = tk.Button(root, text=')', fg='black', bg='white', command=lambda: press(')'), height=1, width=7)
    button_clear = tk.Button(root, text='Clear', fg='black', bg='white', command=clear, height=1, width=7)
    # 9 8 7 6 5 4 3 2 1 0 . =
    button9 = tk.Button(root, text='9', fg='black', bg='white',command=lambda: press(9), height=1, width=7)
    button8 = tk.Button(root, text='8', fg='black', bg='white',command=lambda: press(8), height=1, width=7)
    button7 = tk.Button(root, text='7', fg='black', bg='white',command=lambda: press(7), height=1, width=7)
    button6 = tk.Button(root, text='6', fg='black', bg='white',command=lambda: press(6), height=1, width=7)
    button5 = tk.Button(root, text='5', fg='black', bg='white',command=lambda: press(5), height=1, width=7)
    button4 = tk.Button(root, text='4', fg='black', bg='white',command=lambda: press(4), height=1, width=7)
    button3 = tk.Button(root, text='3', fg='black', bg='white',command=lambda: press(3), height=1, width=7)
    button2 = tk.Button(root, text='2', fg='black', bg='white',command=lambda: press(2), height=1, width=7)
    button1 = tk.Button(root, text='1', fg='black', bg='white',command=lambda: press(1), height=1, width=7)
    button0 = tk.Button(root, text='0', fg='black', bg='white',command=lambda: press(0), height=1, width=7)
    button_decimal = tk.Button(root, text='.', fg='black', bg='white', command=lambda: press('.'), height=1, width=7)
    button_calculate = tk.Button(root, text='=', fg='black', bg='white', command=equalpress, height=1, width=7)
    # clear / * - +
    button_backspace = tk.Button(root, text='CE', fg='black', bg='white', command=backspace, height=1, width=7)
    button_divide = tk.Button(root, text='/', fg='black',bg='white', command=lambda: press('/'), height=1, width=7)
    button_multiply = tk.Button(root, text='*', fg='black', bg='white', command=lambda: press('*'), height=1, width=7)
    button_subtract = tk.Button(root, text='-', fg='black', bg='white', command=lambda: press('-'), height=1, width=7)
    button_add = tk.Button(root, text='+', fg='black', bg='white', command=lambda: press('+'), height=1, width=7)


    ## place the buttons on the grid
    # 2nd row
    button_left_bracket.grid(row=2, column=0)
    button_right_bracket.grid(row=2, column=1)
    button_clear.grid(row=2, column=2)
    # 3rd row
    button9.grid(row=3, column=0)
    button8.grid(row=3, column=1)
    button7.grid(row=3, column=2)
    # 4th row
    button6.grid(row=4, column=0)
    button5.grid(row=4, column=1)
    button4.grid(row=4, column=2)
    # 5th row
    button3.grid(row=5, column=2)
    button2.grid(row=5, column=1)
    button1.grid(row=5, column=0)
    # 6th row
    button0.grid(row=6, column=0)
    button_decimal.grid(row=6, column=1)
    button_calculate.grid(row=6, column=2)
    # operations
    button_backspace.grid(row=2, column=3)
    button_divide.grid(row=3, column=3)
    button_multiply.grid(row=4, column=3)
    button_subtract.grid(row=5, column=3)
    button_add.grid(row=6, column=3)
    

    root.mainloop()
