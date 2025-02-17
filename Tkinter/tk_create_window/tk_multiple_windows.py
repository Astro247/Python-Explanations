#Ci sono due modi per aprire più finestre contemporaneamente in tkinter:
#1) La funzione Tk() crea una finestra indipendente da qualsiasi altra finestra.
#2) La funzione Toplevel() crea una finestra il cui stato dipende da quello della finestra di partenza.

from tkinter import *


def create_tk_window():
    new_window = Tk()

    new_tk_label = Label(new_window, text="The state of this window is indipendent from the previous", font=("Arial", 20, "bold"), bg="#ccb985", bd=5, relief=RAISED)
    new_tk_label.pack()

    new_window.mainloop()


def create_toplevel_window():
    new_window = Toplevel()

    new_toplevel_label = Label(new_window, text="The state of this window is dipendent from the previous", font=("Arial", 20, "bold"), bg="#a0cc85", bd=5, relief=RAISED)
    new_toplevel_label.pack()

    new_window.mainloop() 


def destroy_previous_window(starter_window):
    new_window = Tk()
    starter_window.destroy()

    new_tk_label = Label(new_window, text="The state of this window is indipendent from the previous\nAnd the previous window is destroyed", font=("Arial", 20, "bold"), bg="#778dba", bd=5, relief=RAISED)
    new_tk_label.pack()

    re_open_main_button = Button(new_window, text="Re-open Previous Window", font=("Arial", 20, "bold"), bg="#8478bf", activebackground="#442fad", activeforeground="#adadad", command=main) 
    re_open_main_button.pack()

    new_window.mainloop()


def main():

    starter_window = Tk()

    first_label_frame = Frame(starter_window)
    first_label_frame.grid(row=1, column=1)

    second_label_frame = Frame(starter_window)
    second_label_frame.grid(row=2,column=1)

    third_label_frame = Frame(starter_window)
    third_label_frame.grid(row=3,column=1)

    tk_label = Label(first_label_frame, text="Create New Indipendent Window:", font=("Arial", 20, "bold"), bg="#ccb985", bd=5, relief=RAISED)
    tk_label.grid(row=1, column=1)
    
    tk_button = Button(starter_window, text="Click Here", font=("Arial", 20, "bold"), activebackground="black", activeforeground="white", command=create_tk_window)
    tk_button.grid(row=1, column=2)

    topLevel_label = Label(second_label_frame, text="Create New Top Level Window:", font=("Arial", 20, "bold"), bg="#a0cc85", bd=5, relief=RAISED)
    topLevel_label.grid(row=2, column=1)
    
    topLevel = Button(starter_window, text="Click Here", font=("Arial", 20, "bold"), activebackground="black", activeforeground="white", command=create_toplevel_window)
    topLevel.grid(row=2, column=2)

    destroy_starter_label = Label(third_label_frame, text="Create New Window and Destroy Previous:", font=("Arial", 20, "bold"), bg="#778dba", bd=5, relief=RAISED)
    destroy_starter_label.grid(row=3, column=1)
    
    destroy_starter_label = Button(starter_window, text="Click Here", font=("Arial", 20, "bold"), activebackground="black", activeforeground="white", command=lambda:destroy_previous_window(starter_window))
    destroy_starter_label.grid(row=3, column=2)

    starter_window.mainloop()

main()