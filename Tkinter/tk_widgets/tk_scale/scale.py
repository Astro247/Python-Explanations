#Una scale è una barra che mostra un range di valori.

from tkinter import *

scale_window = Tk()
scale_window.config(bg="#adacac")
scale_window.title("Temperature Scale")
scale_window.geometry("300x920")

temp_icon = PhotoImage(file="temp_icon.png")
hot_image = PhotoImage(file="hot.png")
cold_image = PhotoImage(file="cold.png")

scale_window.iconphoto(True,temp_icon)

hot_label_image = Label(image=hot_image, bg = "#adacac")
cold_label_image = Label(image=cold_image, bg = "#adacac")


def get_temperature():
    temp_string = f"Current Temperature: {temperature_scale.get()}°C"
    temp_label.config(text=temp_string)

temperature_scale = Scale(scale_window, from_ = 100, to = 0) #Determina il punto più alto, "from_", e il punto più basso, "to", della barra
temperature_scale.config(length=500, #Modifica la lunghezza della barra nella finestra
                          tickinterval=10, #mostra, accanto alla barra ad ogni 10, il valore presente a quella determinata posizione nella barra
                          showvalue=False, #il keyword argument showvalue mostra la posizione numerica esatta nella barra se è True, mentre non la mostra se è False
                          troughcolor="#4a4a4a", #Questo keyword argument modifica il colore della barra
                          font = ("Courier New", 20),
                          fg = "black",
                          bg = "#a8a7a7")

temp_label = Label(scale_window, bg="#adacac", font = ("Arial", 10, "bold"))
request_temp = Button(scale_window, text="Print Temperature", font=("Arial", 20, "bold"))
request_temp.config(command=get_temperature)

temp_label.pack()
hot_label_image.pack()
temperature_scale.pack(padx = 50, pady = 50)
cold_label_image.pack()
request_temp.pack(pady=20)

scale_window.mainloop()