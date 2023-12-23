import tkinter as tk

display =tk.Tk()
display.title("Calculator by Python")
display.geometry("400x500")

display.grid_rowconfigure(0,weight=1)
display.grid_rowconfigure(1,weight=4)
display.grid_columnconfigure(0,weight=1)

text_field = tk.Frame(master = display,width = 400,height = 100,bg="red")
text_field.pack(fill=tk.BOTH,expand=True)

button_field = tk.Frame(master = display,width = 400,height = 400,bg="blue")
button_field.pack(fill=tk.BOTH,expand=True)

textbox= tk.Entry(text_field,font=("New Times Roman",30),state=tk.DISABLED,disabledbackground="#00FFFF",bg="#00FFFF",fg="black")
textbox.pack(fill=tk.BOTH,expand=True)


equation =""

def show(value):
    global equation
    equation += value
    textbox.config(state=tk.NORMAL)
    textbox.delete(0, tk.END)  
    textbox.insert(tk.END, equation)  
    textbox.config(state=tk.DISABLED)

def clear():
    global equation
    equation=""
    textbox.config(state=tk.NORMAL)
    textbox.delete(0, tk.END)
    textbox.config(state=tk.DISABLED)

def evaluate():
    global equation
    result =""
    result = eval(equation)
    textbox.config(state=tk.NORMAL)
    textbox.delete(0, tk.END)
    textbox.insert(tk.END, result)
    textbox.config(state=tk.DISABLED)
    equation = result

def delete_char():
    global equation
    equation = equation[:-1]
    textbox.config(state=tk.NORMAL)
    textbox.delete(0, tk.END)
    textbox.insert(tk.END, equation)
    textbox.config(state=tk.DISABLED)    

for i in range(4):
    button_field.grid_columnconfigure(i,weight=1)

for j in range(5): 
    button_field.grid_rowconfigure(j,weight=1)
  
button_one = tk.Button(button_field,text="1",command=lambda: show("1"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_one.grid(row=3,column=0,sticky=tk.NSEW)

button_two = tk.Button(button_field,text="2",command=lambda: show("2"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_two.grid(row=3,column=1,sticky=tk.NSEW)

button_three = tk.Button(button_field,text="3",command=lambda: show("3"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_three.grid(row=3,column=2,sticky=tk.NSEW)

button_four = tk.Button(button_field,text="4",command=lambda: show("4"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_four.grid(row=2,column=0,sticky=tk.NSEW)

button_five = tk.Button(button_field,text="5",command=lambda: show("5"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_five.grid(row=2,column=1,sticky=tk.NSEW)

button_six = tk.Button(button_field,text="6",command=lambda: show("6"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_six.grid(row=2,column=2,sticky=tk.NSEW)

button_seven = tk.Button(button_field,text="7",command=lambda: show("7"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_seven.grid(row=1,column=0,sticky=tk.NSEW)

button_eight = tk.Button(button_field,text="8",command=lambda: show("8"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_eight.grid(row=1,column=1,sticky=tk.NSEW)

button_nine = tk.Button(button_field,text="9",command=lambda: show("9"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_nine.grid(row=1,column=2,sticky=tk.NSEW)

button_zero = tk.Button(button_field,text="0",command=lambda: show("0"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_zero.grid(row=4,column=1,sticky=tk.NSEW)

button_clear = tk.Button(button_field,text="CLR",command=lambda: clear(),font =("New Times Roman",18,"bold"),width=6,bg="#FF0000",fg="white")        
button_clear.grid(row=0,column=0,sticky=tk.NSEW)

button_delete = tk.Button(button_field,text="del",command=lambda: delete_char(),font =("New Times Roman",18),width=6,bg="black",fg="white")        
button_delete.grid(row=0,column=3,sticky=tk.NSEW)

button_divide = tk.Button(button_field,text="/",command=lambda: show("/"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_divide.grid(row=0,column=1,sticky=tk.NSEW)

button_multiple = tk.Button(button_field,text="x",command=lambda: show("*"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_multiple.grid(row=0,column=2,sticky=tk.NSEW)

button_plus = tk.Button(button_field,text="+",command=lambda: show("+"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_plus.grid(row=2,column=3,sticky=tk.NSEW)

button_minus = tk.Button(button_field,text="-",command=lambda: show("-"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_minus.grid(row=1,column=3,sticky=tk.NSEW)

button_signchange = tk.Button(button_field,text="%",command=lambda: show("%"),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_signchange.grid(row=4,column=0,sticky=tk.NSEW)

button_dot = tk.Button(button_field,text=".",command=lambda: show("."),font =("New Times Roman",20),width=6,bg="black",fg="white")        
button_dot.grid(row=4,column=2,sticky=tk.NSEW)

button_equal = tk.Button(button_field,text="=",command=lambda: evaluate(),font =("New Times Roman",20),width=6,bg="#00008B",fg="white")        
button_equal.grid(row=3,column=3,rowspan=2,sticky=tk.NSEW)

display.mainloop()