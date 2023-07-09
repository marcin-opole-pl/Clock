import tkinter as tk
import time
import math
from tkinter import ttk
import numpy as np
import random
import re
import customtkinter as ctk
from style import *

# Set theme
th = 1

# Initialize root
root = ctk.CTk()
# Prevent resize
root.resizable(False, False)
# Title root
root.title("Analog Clock Master")
# Set window's theme
ctk.set_default_color_theme("dark-blue")
# Mask window icon
root.iconbitmap('empty.ico')

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
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0')
# Set canvas
canvas = ctk.CTkCanvas(
    root, 
    width=WIDTH, 
    height=HEIGHT,
    background='#325882'
    )
canvas.grid(
    column=0, 
    row=0, 
    sticky=tk.NSEW, 
    pady=HEIGHT/30, 
    padx=(WIDTH/50, 0), 
    rowspan=12
    )


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
hour_box = ttk.Entry()
minute_box = ttk.Entry()
second_box = ttk.Entry()

def main():
    # Bind enter key to check_func
    root.bind('<Return>', lambda event: check_func())
    draw_clock_face()
    start()
    menu()
    quit()
    draw_second_hand()
    draw_minute_hand()
    draw_hour_hand()
    users_input()
    #layout_help()
    


def draw_clock_face():
    # Draw clock face
    canvas.create_oval(
        20, 20,
        WIDTH-10, HEIGHT-10,
        outline=themes[th]['clock_outline'],
        width=themes[th]['clock_outline_width'])
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
    start = ctk.CTkButton(
        root,
        height=40,
        text='Start',
        font=(font[1]),
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
    menu = ctk.CTkOptionMenu(
        root,
        height=40,
        font=(font[1]),
        anchor='center',
        values=['Light mode', 'Dark mode'],
        command=set_theme
    )
    menu.grid(
        column=3, 
        row=0,
        columnspan=2,
        sticky=tk.EW,
        padx=5
    )


def quit():
    quit = ctk.CTkButton(
        root,
        height=40,
        text='Quit',
        font=(font[1]),
        command=root.destroy
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
    label = ctk.CTkLabel(
        root,
        text='What time is it?',
        font=(font[3]),
        anchor=tk.CENTER
    )
    label.grid(
        column=2,
        row=1,
        columnspan=5,
        sticky=tk.EW,
        padx=50
    )
    hour = ctk.CTkLabel(
        root,
        text='Hour',
        font=(font[2]),
        anchor=tk.CENTER
    )
    hour.grid(
        column=1,
        row=2,
        sticky=tk.EW,
        padx=(50, 5)
    )
    minute = ctk.CTkLabel(
        root,
        text='Minute',
        font=(font[2]),
        anchor=tk.CENTER
    )
    minute.grid(
        column=3,
        row=2,
        sticky=tk.EW,
        padx=5
    )
    second = ctk.CTkLabel(
        root,
        text='Second',
        font=(font[2]),
        anchor=tk.CENTER
    )
    second.grid(
        column=5,
        row=2,
        sticky=tk.EW,
        padx=5
    )
    hour_box = ctk.CTkEntry(
        root,
        font=(font[3]),
        justify='center',
        width=100,
        textvariable=in_hour        
    )
    hour_box.focus()
    hour_box.grid(
        column=1,
        row=3,
        padx=(50, 5)
    )
    label_1 = ctk.CTkLabel(
        root,
        text=':',
        font=(font[3]),
        justify='center',
    )
    label_1.grid(
        column=2,
        row=3,
    )
    minute_box = ctk.CTkEntry(
        root,
        font=(font[3]),
        justify='center',
        width=100,
        textvariable=in_minute        
    )
    minute_box.grid(
        column=3,
        row=3,
        padx=5
    )
    label_2 = ctk.CTkLabel(
        root,
        text=':',
        font=(font[3]),
        justify='center',
    )
    label_2.grid(
        column=4,
        row=3,
    )
    second_box = ctk.CTkEntry(
        root,
        font=(font[3]),
        justify='center',
        width=100,
        textvariable=in_second        
    )
    second_box.grid(
        column=5,
        row=3,
        padx=5
    )
    submit = ctk.CTkButton(
        root,
        text='Check your answer',
        font=(font[4]),
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
    ttk.Label(background='yellow').grid(column=6, row=0, sticky=tk.EW)
    ttk.Label(background='green').grid(column=6, row=1, sticky=tk.EW)
    ttk.Label(background='yellow').grid(column=6, row=2, sticky=tk.EW)
    ttk.Label(background='green').grid(column=6, row=3, sticky=tk.EW)
    ttk.Label(background='yellow').grid(column=6, row=4, sticky=tk.EW)
    ttk.Label(background='green').grid(column=6, row=5, sticky=tk.EW)
    ttk.Label(background='yellow').grid(column=6, row=6, sticky=tk.EW)
    ttk.Label(background='green').grid(column=6, row=7, sticky=tk.EW)
    ttk.Label(background='yellow').grid(column=6, row=8, sticky=tk.EW)
    ttk.Label(background='green').grid(column=6, row=9, sticky=tk.EW)
    ttk.Label(background='yellow').grid(column=6, row=10, sticky=tk.EW)
    ttk.Label(background='green').grid(column=6, row=11, sticky=tk.EW)


def start_func():
    global STATE
    STATE = 1
    return STATE
    

def check_func():
    global STATE
    check_answ = tk.StringVar()
    user_hour = in_hour.get()
    user_min = in_minute.get()
    user_sec = in_second.get()
    match_h = re.fullmatch(r'(^[0]?[0-9]?|[1]?[0-2]?$)', user_hour)
    match_m = re.fullmatch(r'(^[0]?[0-9]?|[1-5]?[0-9]?$)', user_min)
    match_s = re.fullmatch(r'(^[0]?[0-9]?|[1-5]?[0-9]?$)', user_sec)
    # Check corectness of input format
        # User's input is blank '' '' ''
    if user_hour == '' or user_min == '' or user_sec == '':
        check_answ.set('Wrong input format')
    # User's input is in corrrect format
    elif match_h and match_m and match_s:
        # Correct answer
        if int(user_hour) == hour and int(user_min) == minute and int(user_sec) == second:
            check_answ.set('Correct answer')
            STATE = 1
            clear_entry_boxes()
        # Incorrect answer
        else:
            check_answ.set('Wrong answer')
    # User's input in incorrect format eg. 'dog'
    else:    
        check_answ.set('Wrong input format')

    # Print result
    reply = ctk.CTkLabel(
        root,
        text='YO',
        font=(font[2]),
        textvariable=check_answ
        )
    reply.grid(
        column=1, 
        row=6,
        columnspan=4, 
        sticky=tk.NSEW, 
    )


def set_theme(option):
    '''Sets GUI mode (light / dark)'''
    if option == 'Light mode':
        ctk.set_appearance_mode('Light')
        canvas.configure(background='#825C32')
    elif option == 'Dark mode':
        ctk.set_appearance_mode('Dark')
        canvas.configure(background='#325882')

if __name__ == '__main__':
    main()
    root.mainloop()