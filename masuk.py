from tkinter import *
from ttkbootstrap import Style, Window

# Inisialisasi style
style = Style(theme="superhero")

# Buat instance Window
app = Window("My Fitness Pal", "superhero", resizable=(TRUE, TRUE))

# Fungsi untuk membuka halaman lain
def buka_halaman():
    app.destroy()
    import myFitnessPal

# Menambahkan Frame utama
main_frame = Frame(app, padx=20, pady=20)
main_frame.pack(expand=YES, fill=BOTH)

# Menambahkan judul utama
judul_utama = Label(main_frame, text="My Fitness Pal", font="helvetica 20 bold", pady=5)
judul_utama.pack(fill=X)

# Tombol Masuk untuk membuka halaman lain
btn_masuk = Button(main_frame, text="Masuk", command=buka_halaman, font="helvetica 12 bold")
btn_masuk.pack(pady=10, fill=X)

app.mainloop()
