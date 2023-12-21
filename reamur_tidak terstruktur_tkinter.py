import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung():
    suhu = float(txtsuhu.get())
    
    # Rumus konversi suhu
    C = (5/4) * (float(suhu))
    F = (9/4) * (float(suhu)) + 32 
    K = (5/4) * (float(suhu)) + 273

    # Menampilkan hasil konversi
    txtCelcius.delete(0, END)
    txtCelcius.insert(END, C)

    txtFahrenheit.delete(0, END)
    txtFahrenheit.insert(END, F)

    txtKelvin.delete(0, END)
    txtKelvin.insert(END, K)

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Konversi Suhu Reamur")

# Windows
frame = Frame(app)
frame.pack(padx=40, pady=40)

# Label
suhu_label = Label(frame, text="Reamur:")
suhu_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox
txtsuhu = Entry(frame)
txtsuhu.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

C_label = Label(frame, text="Celcius:")
C_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

F_label = Label(frame, text="Fahrenheit:")
F_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

K_label = Label(frame, text="Kelvin:")
K_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox
txtCelcius = Entry(frame)
txtCelcius.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtFahrenheit = Entry(frame)
txtFahrenheit.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtKelvin = Entry(frame)
txtKelvin.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
