from tkinter import *

first_number=operator=second_number=None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)
    # print(digit)

def clear():
    result_label.config(text='')    

def get_operator(op):
    global first_number,operator

    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator
    second_number = int(result_label['text'])

    if operator == '+':
        result = first_number+second_number
    elif operator == '-':
        result = first_number-second_number    
    elif operator == 'x':
        result = first_number*second_number
    else:
        result = round(first_number/second_number,4)

    result_label.config(text=result)           

root = Tk()

root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)



result_label = Label(root,text='',fg='black')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))

# row 1:

btn7 = Button(root,text='7',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8 = Button(root,text='8',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_add = Button(root,text='+',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))


# row 2:

btn4 = Button(root,text='4',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_sub = Button(root,text='-',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))

# row 3:

btn1 = Button(root,text='1',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_mul = Button(root,text='x',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_operator('x'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))

# row 4:

btn_clear = Button(root,text='C',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :clear())
btn_clear.grid(row=4,column=0)
btn_clear.config(font=('verdana',14))

btn0 = Button(root,text='0',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btn_eq = Button(root,text='=',bg='black',fg='black',highlightbackground="black",width=3,height=2,command= lambda :get_result())
btn_eq.grid(row=4,column=2)
btn_eq.config(font=('verdana',14))

btn_div = Button(root,text='/',bg='black',fg='black',highlightbackground="black",width=3,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))










root.mainloop()