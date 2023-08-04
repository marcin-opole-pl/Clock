
# Clock

## Main file to run program is project.py

#### Program structure

1. GUI

    The main problem with the project was to choose the right library for graphical users interface. I started with tkInter, slowly migrating towards Custom tkInter.

    Main window layout is set with grid method. Window is non-resizable, and adjusts its size to the screen size.

    Clock face is static, and is drawn in CTkCanvas widget.

    Clock hands are draw dynamically, accordingly to set time.

2. Functional approach

    Although object-oriented approach can be implied in this program, lack of multiple objects of the some class has driven me to functional approach.

3. Program overview

    Program is running in ***main function***.

    ***draw_clock_face function*** is responsible for drawing clock face.

    Three consecutive functions:

        - draw_hour_hand,
        - draw_minute_hand,
        - draw_second_hand

    are responsible for animation of the clock. They receive updated time from ***new_hour, new_minute and new_second functions***.

    Calculation of the new time is triggered either by clicking ***start button*** or by submitting correct answer.

    The heart of this program is ***check_func function***. It is responsible for checking correctness of the users input and returning corresponding message to the user.
    Checking algorithm is based on regular expression.

    Rest of the functions is used mainly for layout and styling. Including disabled ***layout_help function***, which is used only during developing stage.

### Final word

This is my first project of this scale. I am fully aware of missing functionality, that would improve user's experience. Project will evolve...
