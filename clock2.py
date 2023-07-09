import tkinter as tk
import time
import math
from tkinter import ttk
import numpy as np
import random
import re
import customtkinter as ctk


# Initialize root
root = tk.Tk()
# Prevent resize
root.resizable(False, False)
# Title root
root.title("Analog Clock Master")

# Set dimentions for canvas to be square
# For horizontal screen
if root.winfo_screenwidth() > root.winfo_screenheight():
    HEIGHT = root.winfo_screenheight() - root.winfo_screenheight() / 10
    WIDTH = HEIGHT
# For vertical screen
elif root.winfo_screenwidth() < root.winfo_screenheight():
    WIDTH = root.winfo_screenwidth() - root.winfo_screenwidth() / 10
    HEIGHT = WIDTH
# Set root size to screen size
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')

# Set canvas
canvas = tk.Canvas(
    root, 
    width=WIDTH, 
    height=HEIGHT, 
    bg="white", 
    borderwidth='5', 
    relief='groove'
    )
canvas.grid(
    column=0, 
    row=0, 
    sticky=tk.NSEW, 
    pady=HEIGHT/30, 
    padx=(WIDTH/50, 0), 
    rowspan=12
    )
# Set deafult GUI style
#ctk.set_appearance_mode('Light')

# Declare variables to store user's input
in_hour = tk.StringVar()
in_minute = tk.StringVar()
in_second = tk.StringVar()

# Globals
STATE = 0
h_list = []
m_list = []
s_list = []
hour = 0
minute = 0
second = 0
check_answ = ''
hour_box = ttk.Entry()
minute_box = ttk.Entry()
second_box = ttk.Entry()

def main():
    styles()
    draw_clock_face()
    start()
    menu()
    quit()
    draw_second_hand()
    draw_minute_hand()
    draw_hour_hand()
    users_input()
    draw_check()
    #layout_help()
    


def draw_clock_face():
    # Draw clock face
    canvas.create_oval(20, 20, WIDTH-10, HEIGHT-10, outline="black", width=8)
    # Draw central point
    canvas.create_oval(WIDTH/2-8, HEIGHT/2-8, WIDTH/2+8, HEIGHT/2+8, fill='black')
 
    # Draw hour numbers
    for i in range(12):
        angle = i * math.pi/6 - math.pi/2
        x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x, y-10, text=str(i+12), font=("Helvetica", 24))
        else:
            canvas.create_text(x, y, text=str(i), font=("Helvetica", 24))
 
    # Draw minute lines
    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        x1 = WIDTH/2 + 0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
        x2 = WIDTH/2 + 0.85 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.85 * HEIGHT/2 * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
        else:
            canvas.create_line(x1, y1, x2, y2, fill="black", width=1)
        # Draw minute numbers
        x0 = WIDTH/2 + 0.9 * WIDTH/2 * math.cos(angle)
        y0 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
        canvas.create_text(x0, y0, text=str(i), font=("Helvetica", 10))

    
def draw_hour_hand():
    canvas.delete('hour_hand')
    hour = new_hour()
    minute = new_minute()
    second = new_second()
    # Draw hour hand
    hour_angle = (hour + minute/60) * math.pi/6 - math.pi/2
    hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
    canvas.create_line(
        WIDTH/2, 
        HEIGHT/2, 
        hour_x, 
        hour_y, 
        fill="black", 
        width=6,
        tags='hour_hand'
    )
    canvas.after(40, draw_hour_hand)


def draw_minute_hand():
    canvas.delete('minute_hand')
    minute = new_minute()
    second = new_second()
    # Draw minute hand
    minute_angle = (minute + second/60) * math.pi/30 - math.pi/2
    minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
    minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
    canvas.create_line(
        WIDTH/2, 
        HEIGHT/2, 
        minute_x, 
        minute_y, 
        fill="black", 
        width=4,
        tags='minute_hand'
    )
    canvas.after(40, draw_minute_hand)


def draw_second_hand():
    canvas.delete('second_hand')
    global STATE
    second = new_second()
    # Draw second hand
    second_angle = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6 * WIDTH/2 * math.cos(second_angle)
    second_y = HEIGHT/2 + 0.6 * WIDTH/2 * math.sin(second_angle)
    canvas.create_line(
        WIDTH/2, 
        HEIGHT/2, 
        second_x, 
        second_y, 
        fill="red", 
        width=2,
        tags='second_hand'
    )
    STATE = 2
    canvas.after(200, draw_second_hand)


def start():
    start = ttk.Button(
        root,
        text='Start',
        style='A.TButton',
        command=start_func
    )
    start.grid(
        column=1, 
        row=0,
        columnspan=2,
        sticky=tk.EW,
        padx=(50, 5)
    )


def menu():
    menu = ttk.Button(
        root,
        text='Menu',
        style='A.TButton', 
    )
    menu.grid(
        column=3, 
        row=0,
        columnspan=2,
        sticky=tk.EW,
        padx=5
    )


def quit():
    quit = ttk.Button(
        root,
        text='Quit',
        style='A.TButton', 
    )
    quit.grid(
        column=5, 
        row=0,
        columnspan=2,
        sticky=tk.EW,
        padx=5
    )


def users_input():
    global hour_box, minute_box, second_box
    ttk.Separator(root, orient='horizontal').grid(column=1, row=1, columnspan=6, sticky=tk.EW)
    label = ttk.Label(
        root,
        text='What time is it?',
        font=('Helvetica, 30'),
        anchor=tk.CENTER
    )
    label.grid(
        column=2,
        row=1,
        columnspan=5,
        sticky=tk.EW,
        padx=50
    )
    hour = ttk.Label(
        root,
        text='Hour',
        style='A.TLabel',
        anchor=tk.CENTER
    )
    hour.grid(
        column=1,
        row=2,
        sticky=tk.EW,
        padx=(50, 5)
    )
    minute = ttk.Label(
        root,
        text='Minute',
        style='A.TLabel',
        anchor=tk.CENTER
    )
    minute.grid(
        column=3,
        row=2,
        sticky=tk.EW,
        padx=5
    )
    second = ttk.Label(
        root,
        text='Second',
        style='A.TLabel',
        anchor=tk.CENTER
    )
    second.grid(
        column=5,
        row=2,
        sticky=tk.EW,
        padx=5
    )
    hour_box = ttk.Entry(
        root,
        font=('Helvetica, 40'),
        justify='center',
        width=3,
        textvariable=in_hour        
    )
    hour_box.focus()
    hour_box.grid(
        column=1,
        row=3,
        padx=(50, 5)
    )
    label_1 = ttk.Label(
        root,
        text=':',
        font=('Helvetica, 40'),
        justify='center',
    )
    label_1.grid(
        column=2,
        row=3,
    )
    minute_box = ttk.Entry(
        root,
        font=('Helvetica, 40'),
        justify='center',
        width=3,
        textvariable=in_minute        
    )
    minute_box.grid(
        column=3,
        row=3,
        padx=5
    )
    label_2 = ttk.Label(
        root,
        text=':',
        font=('Helvetica, 40'),
        justify='center',
    )
    label_2.grid(
        column=4,
        row=3,
    )
    second_box = ttk.Entry(
        root,
        font=('Helvetica, 40'),
        justify='center',
        width=3,
        textvariable=in_second        
    )
    second_box.grid(
        column=5,
        row=3,
        padx=5
    )
    submit = ttk.Button(
        root,
        text='Check your answer',
        style='A.TButton',
        command=check_func 
    )
    submit.grid(
        column=3, 
        row=4,
        columnspan=3,
        sticky=tk.E
    )
    ttk.Separator(root, orient='horizontal').grid(column=1, row=5, columnspan=6, sticky=tk.EW)


def clear_entry_boxes():
        hour_box.delete(0, 'end')
        minute_box.delete(0, 'end')
        second_box.delete(0, 'end')


def new_hour():
    global STATE, hour
    if STATE == 0:
        hour = 0
    # Get random second
    elif STATE == 1:
        hour = random.randint(1, 12)
    return hour


def new_minute():
    global STATE, minute
    if STATE == 0:
        minute = 0
    # Get random second
    elif STATE == 1:
        minute = random.randint(0, 59)
    return minute


def new_second():
    global STATE, second
    if STATE == 0:
        second = 0
    # Get random second
    elif STATE == 1:
        second = random.randint(0, 59)
    return second
    

def layout_help():
    ROW = 1
    ttk.Label(background='red').grid(column=0, row=ROW, sticky=tk.EW)
    ttk.Label(background='blue').grid(column=1, row=ROW, sticky=tk.EW)
    ttk.Label(background='red').grid(column=2, row=ROW, sticky=tk.EW)
    ttk.Label(background='blue').grid(column=3, row=ROW, sticky=tk.EW)
    ttk.Label(background='red').grid(column=4, row=ROW, sticky=tk.EW)
    ttk.Label(background='blue').grid(column=5, row=ROW, sticky=tk.EW)
    ttk.Label(background='red').grid(column=6, row=ROW, sticky=tk.EW)


def styles():
    style = ttk.Style()
    style.configure(
        'A.TButton', 
        relief='groove',
        borderwidth=10,
        font=('Helvetica, 20')
    )
    style.configure(
        'A.TLabel',
        relief='groove',
        borderwidth=10,
        font=('Helvetica, 20')
    )


def start_func():
    global STATE
    STATE = 1
    return STATE
    

def check_func():
    print(f'{hour} : {minute} : {second}')
    global check_answ, STATE
    user_hour = in_hour.get()
    user_min = in_minute.get()
    user_sec = in_second.get()
    match_h = re.fullmatch(r'(^[0]?[0-9]?|[1]?[0-2]?$)', user_hour)
    match_m = re.fullmatch(r'(^[0]?[0-9]?|[1-5]?[0-9]?$)', user_min)
    match_s = re.fullmatch(r'(^[0]?[0-9]?|[1-5]?[0-9]?$)', user_sec)
    # Check corecness of input format
    if match_h and match_m and match_s:
        if int(user_hour) == hour and int(user_min) == minute and int(user_sec) == second:
            check_answ = 'Correct answer'
            STATE = 1
            clear_entry_boxes()
        else:
            check_answ = 'Wrong answer'
    else:
        check_answ = 'Wrong input format'


def draw_check():
    # Set canvas for check reply
    reply = tk.Canvas(
        root, 
        width=WIDTH/20, 
        height=HEIGHT/100, 
        bg="white", 
        borderwidth='5', 
        relief='flat'
        )
    reply.grid(
        column=1, 
        row=6,
        columnspan=6, 
        sticky=tk.NSEW, 
        pady=HEIGHT/30, 
        padx=(WIDTH/50, 0)
    )
    reply.delete('all')
    # Print text
    reply.create_text(200, 40, text=check_answ, font=("Helvetica", 24))
    reply.after(500, draw_check)
  

if __name__ == '__main__':
    main()
    root.mainloop()