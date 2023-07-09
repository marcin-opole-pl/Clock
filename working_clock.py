import tkinter as tk
import time
import math
from tkinter import ttk
import numpy as np
import random


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


def main():
    draw_clock_face()
    draw_hour_hand()
    new_hour()
   

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
    hour = int(new_hour())
    minute = 23
    second = 45
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
    canvas.after(500, draw_hour_hand)
    ''' 
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
        width=4
    )
 
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
        width=2
    )
 
    canvas.after(1000, draw_clock)'''


def random_hour():
    hour = random.randint(0, 13)
    return hour


def new_hour():
    global hour
    for hour in range(0, random_hour()):
        return hour


if __name__ == '__main__':
    main()
    root.mainloop()