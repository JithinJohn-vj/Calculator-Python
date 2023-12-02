from tkinter import *
from subprocess import call
import  math
import tkinter as tk

root = tk.Tk()
class Calculator:
    def click_button(self, symbol):
        global operator
        global var
        if symbol in {'sin', 'cos', 'tan', 'deg', '2pi', '%', '**'}:
            if symbol == 'deg':
                self.operator = self.operator + '°'
            elif symbol == '2pi':
                self.operator = self.operator + '2*pi'
            elif symbol == '%':
                self.operator = self.operator + '%'
            elif symbol == '**':
                self.operator = self.operator + '**'
            else:
                self.operator = f"{symbol}("
        else:
            self.operator = self.operator + str(symbol)
        self.var.set(self.operator)

    def create_circle_button(self, canvas, x, y, radius, text, command):
        circle_id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='#808080', outline='#808080')
        canvas.tag_bind(circle_id, '<Button-1>', command)
        canvas.create_text(x, y, text=text, font=('Helvetica', '16'), fill='white')

    def clear(self):
        self.entry.delete(0,END)
        self.operator =""

    def delete_last(self):
        current_text = self.var.get()
        if current_text:
            new_text = current_text[:-1]
            self.var.set(new_text)
            self.operator = new_text

    ''' def delete(self):
        self.operator = str(self.entry.delete(len(self.entry.get())-1))
    '''
    def evaluate(self):
        expression = self.entry.get()
        expression = expression.replace('°', '*pi/180')
        expression = expression.replace('pi', 'math.pi').replace('2*math.pi', '2*math.pi')
        try:
            if 'sin(' in expression or 'cos(' in expression or 'tan(' in expression:
                if expression.endswith(')'):
                    angle_str = expression[expression.index('(') + 1:expression.index(')')]
                    angle = eval(angle_str)
                    if 'sin(' in expression:
                        result = math.sin(angle)
                    elif 'cos(' in expression:
                        result = math.cos(angle)
                    elif 'tan(' in expression:
                        result = math.tan(angle)
                else:
                    raise ValueError("Invalid expression for trigonometric function")
            elif 'sqrt' in expression:
                if '(' in expression and expression.endswith(')'):
                    value_str = expression[expression.index('(') + 1:expression.index(')')]
                    value = eval(value_str)
                    result = math.sqrt(value)
                else:
                    raise ValueError("Invalid expression for square root")
            elif 'log(' in expression:
                if expression.endswith(')'):
                    value_str = expression[expression.index('(') + 1:expression.index(')')]
                    value = eval(value_str)
                    result = math.log10(value)
                else:
                    raise ValueError("Invalid expression for logarithm")
            else:
                result = eval(expression)

            self.var.set(result)
            self.operator = str(result)
        except Exception as e:
            self.var.set("Error")

    def __init__(self,master):
        button_width = 30
        button_height = 30
        self.operator = ""
        self.var = StringVar()
        frame_s = Frame(master, height=300, width=30 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg='#808080',width=12,bd=5,insertwidth=3,justify='right',font=('arial',50,'bold'))
        self.entry.pack()
        self.t = Text(self.entry,height=80)

        label_key = Label(root, height=15, width=30,bd=5,bg='#0C7478')
        label_key.pack(side=LEFT, fill=BOTH, expand=True)

        label_7 = Label(label_key,bg='#0C7478')
        label_7.grid(row=0, column=0)
        canvas_7 = Canvas(label_7, width=button_width * 2, height=button_height * 2, highlightthickness=0, bg='#0C7478')
        canvas_7.grid(row=0, column=0, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_7, button_width, button_height, button_width, '7',lambda event: self.click_button(7))

        label_8 = Label(label_key, bg='#0C7478')
        label_8.grid(row=0, column=1)
        canvas_8 = Canvas(label_8, width=button_width * 2, height=button_height * 2, highlightthickness=0, bg='#0C7478')
        canvas_8.grid(row=0, column=1, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_8, button_width, button_height, button_width, '8',lambda event: self.click_button(8))

        label_9 = Label(label_key, bg='#0C7478')
        label_9.grid(row=0, column=2)
        canvas_9 = Canvas(label_9, width=button_width * 2, height=button_height * 2, highlightthickness=0, bg='#0C7478')
        canvas_9.grid(row=0, column=2, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_9, button_width, button_height, button_width, '9',lambda event: self.click_button(9))

        label_div = Label(label_key, bg='#0C7478')
        label_div.grid(row=0, column=3)
        canvas_div = Canvas(label_div, width=button_width * 2, height=button_height * 2, highlightthickness=0, bg='#0C7478')
        canvas_div.grid(row=0, column=3, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_div, button_width, button_height, button_width, '/',lambda event: self.click_button('/'))

        label_sin = Label(label_key, bg='#0C7478')
        label_sin.grid(row=0, column=4)
        canvas_sin = Canvas(label_sin, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_sin.grid(row=0, column=4, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_sin, button_width, button_height, button_width, 'sin',lambda event: self.click_button('sin'))

        label_4 = Label(label_key, bg='#0C7478')
        label_4.grid(row=1, column=0)
        canvas_4 = Canvas(label_4, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_4.grid(row=1, column=0, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_4, button_width, button_height, button_width, '4',lambda event: self.click_button(4))

        label_5 = Label(label_key, bg='#0C7478')
        label_5.grid(row=1, column=1)
        canvas_5 = Canvas(label_5, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_5.grid(row=1, column=1, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_5, button_width, button_height, button_width, '5',lambda event: self.click_button('5'))

        label_6 = Label(label_key, bg='#0C7478')
        label_6.grid(row=1, column=2)
        canvas_6 = Canvas(label_6, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_6.grid(row=1, column=2, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_6, button_width, button_height, button_width, '6',lambda event: self.click_button('6'))

        label_mul = Label(label_key, bg='#0C7478')
        label_mul.grid(row=1, column=3)
        canvas_mul = Canvas(label_mul, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_mul.grid(row=1, column=3, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_mul, button_width, button_height, button_width, 'X',lambda event: self.click_button('*'))

        label_cos = Label(label_key, bg='#0C7478')
        label_cos.grid(row=1, column=4)
        canvas_cos = Canvas(label_cos, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_cos.grid(row=1, column=4, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_cos, button_width, button_height, button_width, 'cos',lambda event: self.click_button('cos'))

        label_1 = Label(label_key, bg='#0C7478')
        label_1.grid(row=2, column=0)
        canvas_1 = Canvas(label_1, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_1.grid(row=2, column=0, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_1, button_width, button_height, button_width, '1',lambda event: self.click_button('1'))

        label_2 = Label(label_key, bg='#0C7478')
        label_2.grid(row=2, column=1)
        canvas_2 = Canvas(label_2, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_2.grid(row=2, column=1, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_2, button_width, button_height, button_width, '2',lambda event: self.click_button('2'))

        label_3 = Label(label_key, bg='#0C7478')
        label_3.grid(row=2, column=2)
        canvas_3 = Canvas(label_3, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_3.grid(row=2, column=2, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_3, button_width, button_height, button_width, '3',lambda event: self.click_button('3'))

        label_sub = Label(label_key, bg='#0C7478')
        label_sub.grid(row=2, column=3)
        canvas_sub = Canvas(label_sub, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_sub.grid(row=2, column=3, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_sub, button_width, button_height, button_width, '-',lambda event: self.click_button('-'))

        label_tan = Label(label_key, bg='#0C7478')
        label_tan.grid(row=2, column=4)
        canvas_tan = Canvas(label_tan, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_tan.grid(row=2, column=4, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_tan, button_width, button_height, button_width, 'tan',lambda event: self.click_button('tan'))

        label_0 = Label(label_key, bg='#0C7478')
        label_0.grid(row=3, column=0)
        canvas_0 = Canvas(label_0, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_0.grid(row=3, column=0, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_0, button_width, button_height, button_width, '0',lambda event: self.click_button('0'))

        label_deci = Label(label_key, bg='#0C7478')
        label_deci.grid(row=3, column=1)
        canvas_deci = Canvas(label_deci, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_deci.grid(row=3, column=1, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_deci, button_width, button_height, button_width, '.',lambda event: self.click_button('.'))

        label_equal = Label(label_key, bg='#0C7478')
        label_equal.grid(row=3, column=2)
        canvas_equal = Canvas(label_equal, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_equal.grid(row=3, column=2, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_equal, button_width, button_height, button_width, '=',lambda event: self.evaluate())

        label_add = Label(label_key, bg='#0C7478')
        label_add.grid(row=3, column=3)
        canvas_add = Canvas(label_add, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_add.grid(row=3, column=3, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_add, button_width, button_height, button_width, '+',lambda event: self.click_button('+'))

        label_log = Label(label_key, bg='#0C7478')
        label_log.grid(row=3, column=4)
        canvas_log = Canvas(label_log, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_log.grid(row=3, column=4, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_log, button_width, button_height, button_width, 'log',lambda event: self.click_button('log'))

        label_lbrace = Label(label_key, bg='#0C7478')
        label_lbrace.grid(row=4, column=0)
        canvas_lbrace = Canvas(label_lbrace, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_lbrace.grid(row=4, column=0, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_lbrace, button_width, button_height, button_width, '(',lambda event: self.click_button('('))

        label_rbrace = Label(label_key, bg='#0C7478')
        label_rbrace.grid(row=4, column=1)
        canvas_rbarce = Canvas(label_rbrace, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_rbarce.grid(row=4, column=1, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_rbarce, button_width, button_height, button_width, ')',lambda event: self.click_button(')'))

        label_sqrt = Label(label_key, bg='#0C7478')
        label_sqrt.grid(row=4, column=2)
        canvas_sqrt = Canvas(label_sqrt, width=button_width * 2, height=button_height * 2, highlightthickness=0, bg='#0C7478')
        canvas_sqrt.grid(row=4, column=2, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_sqrt, button_width, button_height, button_width, '√',lambda event: self.click_button('sqrt'))

        label_pi = Label(label_key, bg='#0C7478')
        label_pi.grid(row=4, column=3)
        canvas_pi = Canvas(label_pi, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_pi.grid(row=4, column=3, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_pi, button_width, button_height, button_width, '𝞹',lambda event: self.click_button('pi'))

        label_del = Label(label_key, bg='#0C7478')
        label_del.grid(row=4, column=4)
        canvas_del = Canvas(label_del, width=button_width * 2, height=button_height * 2, highlightthickness=0, bg='#0C7478')
        canvas_del.grid(row=4, column=4, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_del, button_width, button_height, button_width, 'Del',lambda event: self.delete_last())

        label_deg = Label(label_key, bg='#0C7478')
        label_deg.grid(row=5, column=0)
        canvas_deg = Canvas(label_deg, width=button_width * 2, height=button_height * 2, highlightthickness=0, bg='#0C7478')
        canvas_deg.grid(row=5, column=0, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_deg, button_width, button_height, button_width, 'deg',lambda event: self.click_button('deg'))

        label_2pi = Label(label_key, bg='#0C7478')
        label_2pi.grid(row=5, column=1)
        canvas_2pi = Canvas(label_2pi, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_2pi.grid(row=5, column=1, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_2pi, button_width, button_height, button_width, '2𝞹',lambda event: self.click_button('2pi'))

        label_mod = Label(label_key, bg='#0C7478')
        label_mod.grid(row=5, column=2)
        canvas_mod = Canvas(label_mod, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_mod.grid(row=5, column=2, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_mod, button_width, button_height, button_width, '%',lambda event: self.click_button('%'))

        label_exp = Label(label_key, bg='#0C7478')
        label_exp.grid(row=5, column=3)
        canvas_exp = Canvas(label_exp, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_exp.grid(row=5, column=3, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_exp, button_width, button_height, button_width, 'x^',lambda event: self.click_button('exp'))

        label_C = Label(label_key, bg='#0C7478')
        label_C.grid(row=5, column=4)
        canvas_C = Canvas(label_C, width=button_width * 2, height=button_height * 2, highlightthickness=0,bg='#0C7478')
        canvas_C.grid(row=5, column=4, ipadx=2, ipady=2, sticky="nsew")
        self.create_circle_button(canvas_C, button_width, button_height, button_width, 'AC',lambda event: self.clear())


        '''label_del = Label(label_fkey, bg ='black')
        label_del.grid(row=0,column=1,sticky=E)
        button_del = Button(label_del, text='del', font=('Helvetica', '16'),bd=3, height=1, width=3,command=  self.delete)
        button_del.pack()'''
        call(["python3", "PySimpleGUIWeb/PyGUI.py"])



c = Calculator(root)
root.title("Python Calculator Challenge")
root.mainloop()