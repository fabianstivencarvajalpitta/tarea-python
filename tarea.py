import tkinter as tk


def on_button_click():
    print("tarea python :)")


window = tk.Tk()


window.title("Mi Aplicación")


window.configure(background="#e1d8b9")


window.geometry("800x600")


button = tk.Button(window, text="Haz clic aquí", command=on_button_click)


button.configure(background="#a5c3d9")


button.pack()
 
window.mainloop()
