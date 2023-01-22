from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

# Basic window config
root=Tk()
root.title('IMC Calculator')
root.geometry('470x580+300+200')
root.resizable(False,False)
root.configure(bg='#f0f1f5')

# BMI function
def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    
    # Convert height into meter
    m=h/100
    bmi=round(float(w/m**2),1)
    label1.config(text=bmi)
    
    if bmi<=18.5:
        label2.config(text='Underweight')
        label3.config(text='You have lower weight then \nnormal body')
        
    elif bmi>18.5 and bmi<=25:
        label2.config(text='Normal')
        label3.config(text='It indicates that you are \nhealthy')
        
    elif bmi>25 and bmi<=30:
        label2.config(text='Overweight')
        label3.config(text='It indicates that a person \nis slightly overweight. \nA doctor may advise to lose \nsome weight for health reasons')
        
    else:
        label2.config(text='Obes')
        label3.config(text='Health may be at risk, \nif they do not lose \nweight')

# Icon
image_icon = PhotoImage(file = './img/icon.png')
root.iconphoto(False, image_icon)

# Program title
top = PhotoImage(file='./img/top.png')
top_image = Label(root, image=top, background='#f0f1f5')
top_image.place(x=-10, y=-10)

# Bottom box (lightblue)
Label(root, width=72, height=18, bg='#298294').pack(side=BOTTOM)

# Two box on the top
box = PhotoImage(file='./img/box.png')
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# Scale image
scale=PhotoImage(file='./img/scale.png')
Label(root, image=scale, bg='#298294').place(x=20, y=310)

# Slider1
# Slider functions
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    
    size = int(float(get_current_value()))
    img = (Image.open('img/man.png'))
    resized_image = img.resize((50, 10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    man_image.config(image=photo2)
    man_image.place(x=70, y=550-size)
    man_image.image = photo2

# Style configure
style = ttk.Style()
style.configure('TScale', background='white')
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style='TScale',
                   command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

# Slider2
# Slider functions
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

# Style configure
style2 = ttk.Style()
style2.configure('TScale', background='white')
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style='TScale',
                   command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# Input boxes
Height = StringVar()
Weight = StringVar()

height = Entry(root, textvariable= Height, width=5, font='arial 50',
               bg='#fff', fg='#000', bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable= Weight, width=5, font='arial 50',
               bg='#fff', fg='#000', bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# Man image
man_image = Label(root, bg='#298294')
man_image.place(x=70, y=530)

# Button report
Button(root, text='View Report', width=12, height=2, font='arial 10 bold', 
       bg='#416F3E', fg='white', command=BMI).place(x=300, y=315)

# Number label
label1 = Label(root, font='arial 40 bold', bg='#298294', fg='#fff')
label1.place(x=125, y=305)

# Title report
label2 = Label(root, font='arial 20 bold', justify=tk.LEFT, bg='#298294', fg='#000000')
label2.place(x=200, y=410)

# Text report
label3 = Label(root, font='arial 10 bold', justify=tk.LEFT, bg='#298294')
label3.place(x=200, y=460)

root.mainloop()