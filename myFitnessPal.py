from tkinter import *
from ttkbootstrap import Style, Window

style = Style(theme="superhero")
kalori = Window("My Fitness Pal", "superhero", resizable=(TRUE, TRUE))

def perintah():
    berat_badan = int(nilai1.get())
    tinggi_badan = int(nilai2.get())
    usia = int(nilai3.get())
    jenis_kelamin = jenis_kelamin_entry.get()
    aktivitas_fisik = aktivitas_fisik_entry.get()

    # Menghitung BMR (Basal Metabolic Rate) berdasarkan jenis kelamin
    if jenis_kelamin == "Pria":
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
    else:  # jenis_kelamin == "Wanita"
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)

    # Menghitung BMI (Body Mass Index)
    bmi = berat_badan / ((tinggi_badan / 100) ** 2)

    # Menentukan faktor aktivitas fisik
    if aktivitas_fisik == "tidak aktif":
        faktor_aktivitas = 1.2
    elif aktivitas_fisik == "sedikit aktif":
        faktor_aktivitas = 1.375
    elif aktivitas_fisik == "aktif":
        faktor_aktivitas = 1.55
    elif aktivitas_fisik == "sangat aktif":
        faktor_aktivitas = 1.725
    elif aktivitas_fisik == "ekstra aktif":
        faktor_aktivitas = 1.9
    else:
        faktor_aktivitas = 1.2 

    # Menghitung Total Daily Energy Expenditure (TDEE)
    tdee = bmr * faktor_aktivitas

    if bmi < 18.5:
        status = "Kekurangan Berat Badan"
        saran = "Anda membutuhkan lebih banyak kalori untuk mencapai berat badan ideal. Disarankan untuk mengonsumsi makanan bergizi dan berprotein tinggi."
    elif 18.5 <= bmi < 24.9:
        status = "Berat Badan Normal"
        saran = "Selamat, berat badan Anda sudah ideal. Pertahankan pola makan sehat dan tetap aktif berolahraga."
    else:
        status = "Kelebihan Berat Badan"
        saran = "Anda perlu memperhatikan pola makan dan rutin berolahraga untuk mencapai berat badan yang sehat."

    # Menampilkan hasil dan rekomendasi
    hasil.configure(text=f"Status Berat Badan: {status}\n{saran}\n\nTotal Kebutuhan Kalori Harian: {tdee:.2f} kalori")

# Menambahkan Frame utama
main_frame = Frame(kalori, padx=20, pady=20)
main_frame.pack(expand=YES, fill=BOTH)

# Menambahkan judul
judul_utama = Label(main_frame, text="Kebutuhan Kalori Harian", font="helvetica 20 bold", pady=5)
judul_utama.pack(fill=X)

# Label dan Entry untuk berat badan
teks1 = Label(main_frame, text="Masukkan Berat Badan (kg):", font="helvetica 12")
teks1.pack(pady=5, anchor=W)

nilai1 = Entry(main_frame, bd=5, font="helvetica 12 bold")
nilai1.pack(fill=X, pady=5)

# Label dan Entry untuk tinggi badan
teks2 = Label(main_frame, text="Masukkan Tinggi Badan (cm):", font="helvetica 12")
teks2.pack(pady=5, anchor=W)

nilai2 = Entry(main_frame, bd=5, font="helvetica 12 bold")
nilai2.pack(fill=X, pady=5)

# Label dan Entry untuk usia
teks3 = Label(main_frame, text="Masukkan Usia:", font="helvetica 12")
teks3.pack(pady=5, anchor=W)

nilai3 = Entry(main_frame, bd=5, font="helvetica 12 bold")
nilai3.pack(fill=X, pady=5)

# Label untuk jenis kelamin
teks4 = Label(main_frame, text="Jenis Kelamin (Pria/Wanita):", font="helvetica 12")
teks4.pack(pady=5, anchor=W)

jenis_kelamin_entry = Entry(main_frame, bd=5, font="helvetica 12 bold")
jenis_kelamin_entry.pack(fill=X, pady=5)

# Label untuk faktor aktivitas fisik
teks5 = Label(main_frame, text="Faktor Aktivitas Fisik (tidak aktif/sedikit aktif/aktif/sangat aktif/ekstra aktif):", font="helvetica 12")
teks5.pack(pady=5, anchor=W)

aktivitas_fisik_entry = Entry(main_frame, bd=5, font="helvetica 12 bold")
aktivitas_fisik_entry.pack(fill=X, pady=5)

# Tombol Submit
btn = Button(main_frame, text="Submit", command=perintah, font="helvetica 12 bold")
btn.pack(pady=10, fill=X)

# Label untuk hasil dan rekomendasi
teks6 = Label(main_frame, text="Hasil:", font="helvetica 12")
teks6.pack(pady=5, anchor=W)

hasil = Label(main_frame, text="", font="helvetica 12 bold", justify=LEFT)
hasil.pack(fill=X, pady=5)

kalori.mainloop()