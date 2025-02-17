#Un mouse event, ugualmente ai key events, permette l'esecuzione di una funzione una volta premuto uno specifico tasto del mouse.

from tkinter import *

# ---- LEFT MOUSE BUTTON AREA ----

def get_left_coordinates(event, coordinates, check_click):

    new_coordinates = f"Mouse Coordinates = ({event.x};{event.y})"
    coordinates.config(text=new_coordinates)

    check_click.config(text="You clicked the left mouse button!")


def left_mouse_button():

    left_button_window = Toplevel()
    left_button_window.title("Left")
    
    explanation_text = "With the root bind '<Button-1>' a specific function will be called\n once the left mouse button is clicked."
    explanation_label = Label(left_button_window, text=explanation_text , bg="#bda86d", font=("Arial", 20, "bold"), relief=RAISED, bd=3)
    explanation_label.grid(row=1, column=1, columnspan=2)

    mouse_area = Frame(left_button_window)
    mouse_area.config(height=250, width=500, bg="gray")
    mouse_area.grid(row=2, column=1, columnspan=2, sticky="nsew") #Il keyword argument sticky="nsew" fa sì che il frame si aderisca a tutti i lati delle righe e colonne a cui appartiene.

    check_click = Label(left_button_window, text="You haven't clicked yet..", bg="#bda86d", font=("Arial", 20, "bold"))
    check_click.grid(row=3, column=1, columnspan=2, sticky="nsew")

    coordinates = Label(left_button_window, text="No coordinates yet..", bg="#bda86d", font=("Arial", 20, "bold"))
    coordinates.grid(row=4, column=1, columnspan=2, sticky="nsew")

    mouse_area.bind("<Button-1>", lambda event:get_left_coordinates(event, coordinates, check_click))

    left_button_window.mainloop()

# ---- LEFT MOUSE BUTTON AREA ----

# ---- RIGHT MOUSE BUTTON AREA ----

def get_right_coordinates(event, coordinates, check_click):

    new_coordinates = f"Mouse Coordinates = ({event.x};{event.y})"
    coordinates.config(text=new_coordinates)

    check_click.config(text="You clicked the right mouse button!")


def right_mouse_button():

    right_button_window = Toplevel()
    right_button_window.title("Right")
    
    explanation_text = "With the root bind '<Button-3>' a specific function will be called\n once the right mouse button is clicked."
    explanation_label = Label(right_button_window, text=explanation_text , bg="#aabd6d", font=("Arial", 20, "bold"), relief=RAISED, bd=3)
    explanation_label.grid(row=1, column=1, columnspan=2)

    mouse_area = Frame(right_button_window)
    mouse_area.config(height=250, width=500, bg="gray")
    mouse_area.grid(row=2, column=1, columnspan=2, sticky="nsew")

    check_click = Label(right_button_window, text="You haven't clicked yet..", bg="#aabd6d", font=("Arial", 20, "bold"))
    check_click.grid(row=3, column=1, columnspan=2, sticky="nsew")

    coordinates = Label(right_button_window, text="No coordinates yet..", bg="#aabd6d", font=("Arial", 20, "bold"))
    coordinates.grid(row=4, column=1, columnspan=2, sticky="nsew")

    mouse_area.bind("<Button-3>", lambda event:get_right_coordinates(event, coordinates, check_click))

    right_button_window.mainloop()

# ---- RIGHT MOUSE BUTTON AREA ----

# ---- SCROLL MOUSE BUTTON AREA ----

def get_scroll_coordinates(event, coordinates, check_click):

    new_coordinates = f"Mouse Coordinates = ({event.x};{event.y})"
    coordinates.config(text=new_coordinates)

    check_click.config(text="You clicked the scroll mouse button!")


def scroll_mouse_button():

    scroll_button_window = Toplevel()
    scroll_button_window.title("Scroll")
    
    explanation_text = "With the root bind '<Button-2>' a specific function will be called\n once the scroll mouse button is clicked."
    explanation_label = Label(scroll_button_window, text=explanation_text , bg="#6dbd75", font=("Arial", 20, "bold"), relief=RAISED, bd=3)
    explanation_label.grid(row=1, column=1, columnspan=2)

    mouse_area = Frame(scroll_button_window)
    mouse_area.config(height=250, width=500, bg="gray")
    mouse_area.grid(row=2, column=1, columnspan=2, sticky="nsew")

    check_click = Label(scroll_button_window, text="You haven't clicked yet..", bg="#6dbd75", font=("Arial", 20, "bold"))
    check_click.grid(row=3, column=1, columnspan=2, sticky="nsew")

    coordinates = Label(scroll_button_window, text="No coordinates yet..", bg="#6dbd75", font=("Arial", 20, "bold"))
    coordinates.grid(row=4, column=1, columnspan=2, sticky="nsew")

    mouse_area.bind("<Button-2>", lambda event:get_scroll_coordinates(event, coordinates, check_click))

    scroll_button_window.mainloop()

# ---- SCROLL MOUSE BUTTON AREA ----

# ---- RELEASE FUNCTION AREA ----

def get_release_coordinates(event, coordinates):

    new_coordinates = f"Mouse Coordinates = ({event.x};{event.y})"
    coordinates.config(text=new_coordinates)


def release_function():

    release_function_window = Toplevel()
    release_function_window.title("Release")
    
    explanation_text = "The '<ButtonRelease>' function allows a specific function to be called\n once the right mouse button get released."
    explanation_label = Label(release_function_window, text=explanation_text , bg="#6aba9a", font=("Arial", 20, "bold"), relief=RAISED, bd=3)
    explanation_label.grid(row=1, column=1, columnspan=2)

    mouse_area = Frame(release_function_window)
    mouse_area.config(height=250, width=500, bg="gray")
    mouse_area.grid(row=2, column=1, columnspan=2, sticky="nsew")

    coordinates = Label(release_function_window, text="No coordinates yet..", bg="#6aba9a", font=("Arial", 20, "bold"))
    coordinates.grid(row=3, column=1, columnspan=2, sticky="nsew")

    mouse_area.bind("<ButtonRelease>", lambda event:get_release_coordinates(event, coordinates))

    release_function_window.mainloop()

# ---- RELEASE FUNCTION AREA ----

# ---- ENTER FUNCTION AREA ----

def get_enter_coordinates(event, coordinates):

    new_coordinates = f"Mouse Coordinates = ({event.x};{event.y})"
    coordinates.config(text=new_coordinates)


def enter_function():

    enter_function_window = Toplevel()
    enter_function_window.title("Enter")
    
    explanation_text = "The '<Enter>' function allows a specific function to be called\n as soon as the mouse cursor enter a specific area."
    explanation_label = Label(enter_function_window, text=explanation_text , bg="#b56582", font=("Arial", 20, "bold"), relief=RAISED, bd=3)
    explanation_label.grid(row=1, column=1, columnspan=2)

    mouse_area = Frame(enter_function_window)
    mouse_area.config(height=250, width=500, bg="gray")
    mouse_area.grid(row=2, column=1, columnspan=2, sticky="nsew")

    coordinates = Label(enter_function_window, text="No coordinates yet..", bg="#b56582", font=("Arial", 20, "bold"))
    coordinates.grid(row=3, column=1, columnspan=2, sticky="nsew")

    mouse_area.bind("<Enter>", lambda event:get_enter_coordinates(event, coordinates))

    enter_function_window.mainloop()

# ---- ENTER FUNCTION AREA ----

# ---- LEAVE FUNCTION AREA ----

def get_leave_coordinates(event, coordinates):

    new_coordinates = f"Mouse Coordinates = ({event.x};{event.y})"
    coordinates.config(text=new_coordinates)


def leave_function():

    leave_function_window = Toplevel()
    leave_function_window.title("Leave")
    
    explanation_text = "The '<Leave>' function allows a specific function to be called\n as soon as the mouse cursor exit a specific area."
    explanation_label = Label(leave_function_window, text=explanation_text , bg="#c28b67", font=("Arial", 20, "bold"), relief=RAISED, bd=3)
    explanation_label.grid(row=1, column=1, columnspan=2)

    mouse_area = Frame(leave_function_window)
    mouse_area.config(height=250, width=500, bg="gray")
    mouse_area.grid(row=2, column=1, columnspan=2, sticky="nsew")

    coordinates = Label(leave_function_window, text="No coordinates yet..", bg="#c28b67", font=("Arial", 20, "bold"))
    coordinates.grid(row=3, column=1, columnspan=2, sticky="nsew")

    mouse_area.bind("<Leave>", lambda event:get_leave_coordinates(event, coordinates))

    leave_function_window.mainloop()

# ---- LEAVE FUNCTION AREA ----

# ---- MOTION FUNCTION AREA ----

def get_motion_coordinates(event, coordinates):

    new_coordinates = f"Mouse Coordinates = ({event.x};{event.y})"
    coordinates.config(text=new_coordinates)


def motion_function():

    motion_function_window = Toplevel()
    motion_function_window.title("Leave")
    
    explanation_text = "The '<Motion>' function call a specific function\n as soon as the mouse move."
    explanation_label = Label(motion_function_window, text=explanation_text , bg="#657db5", font=("Arial", 20, "bold"), relief=RAISED, bd=3)
    explanation_label.grid(row=1, column=1, columnspan=2)

    mouse_area = Frame(motion_function_window)
    mouse_area.config(height=250, width=500, bg="gray")
    mouse_area.grid(row=2, column=1, columnspan=2, sticky="nsew")

    coordinates = Label(motion_function_window, text="No coordinates yet..", bg="#657db5", font=("Arial", 20, "bold"))
    coordinates.grid(row=3, column=1, columnspan=2, sticky="nsew")

    mouse_area.bind("<Motion>", lambda event:get_motion_coordinates(event, coordinates))

    motion_function_window.mainloop()

# ---- MOTION FUNCTION AREA ----

def main():

    main_window = Tk()
    main_window.title("Main")

    left_button = Button(main_window, text="Left", font=("Arial", 20, "bold"), width=25, bg="#bda86d", activebackground="black", activeforeground="white", command=left_mouse_button)
    left_button.pack()

    right_button = Button(main_window, text="Right", font=("Arial", 20, "bold"), width=25, bg="#aabd6d", activebackground="black", activeforeground="white", command=right_mouse_button)
    right_button.pack()

    scroll_button = Button(main_window, text="Scroll", font=("Arial", 20, "bold"), width=25, bg="#6dbd75", activebackground="black", activeforeground="white", command=scroll_mouse_button)
    scroll_button.pack()

    release_button = Button(main_window, text="Release", font=("Arial", 20, "bold"), width=25, bg="#6aba9a", activebackground="black", activeforeground="white", command=release_function)
    release_button.pack()

    enter_button = Button(main_window, text="Enter", font=("Arial", 20, "bold"), width=25, bg="#b56582", activebackground="black", activeforeground="white", command=enter_function)
    enter_button.pack()

    leave_button = Button(main_window, text="Leave", font=("Arial", 20, "bold"), width=25, bg="#c28b67", activebackground="black", activeforeground="white", command=leave_function)
    leave_button.pack()

    motion_button = Button(main_window, text="Motion", font=("Arial", 20, "bold"), width=25, bg="#657db5", activebackground="black", activeforeground="white", command=motion_function)
    motion_button.pack()

    main_window.mainloop()

main()