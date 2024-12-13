# Program Prediksi Peluang Diterima di Universitas Internasional dan Indonesia dengan GUI, Sistem Pakar, dan Rekomendasi Universitas

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Daftar 30 Universitas dengan Kriteria Penerimaan
UNIVERSITIES = [
    # 10 Universitas Terbaik di Dunia
    {
        "name": "Massachusetts Institute of Technology (MIT)",
        "min_ipk": 3.8,
        "min_sat": 1500,
        "min_toefl": 100,
        "penelitian": "ya",
        "rekomendasi": "sangat baik",
        "sop": "sangat baik"
    },
    {
        "name": "Stanford University",
        "min_ipk": 3.7,
        "min_sat": 1450,
        "min_toefl": 95,
        "penelitian": "ya",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "Harvard University",
        "min_ipk": 3.8,
        "min_sat": 1480,
        "min_toefl": 100,
        "penelitian": "ya",
        "rekomendasi": "sangat baik",
        "sop": "sangat baik"
    },
    {
        "name": "California Institute of Technology (Caltech)",
        "min_ipk": 3.8,
        "min_sat": 1500,
        "min_toefl": 100,
        "penelitian": "ya",
        "rekomendasi": "sangat baik",
        "sop": "sangat baik"
    },
    {
        "name": "University of Oxford",
        "min_ipk": 3.7,
        "min_sat": 1400,
        "min_toefl": 100,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "University of Cambridge",
        "min_ipk": 3.7,
        "min_sat": 1400,
        "min_toefl": 100,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "ETH Zurich",
        "min_ipk": 3.6,
        "min_sat": 1350,
        "min_toefl": 95,
        "penelitian": "baik",
        "rekomendasi": "cukup",
        "sop": "baik"
    },
    {
        "name": "Imperial College London",
        "min_ipk": 3.6,
        "min_sat": 1350,
        "min_toefl": 95,
        "penelitian": "baik",
        "rekomendasi": "cukup",
        "sop": "baik"
    },
    {
        "name": "University of Chicago",
        "min_ipk": 3.7,
        "min_sat": 1400,
        "min_toefl": 95,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "Princeton University",
        "min_ipk": 3.8,
        "min_sat": 1480,
        "min_toefl": 100,
        "penelitian": "ya",
        "rekomendasi": "sangat baik",
        "sop": "sangat baik"
    },
    # 20 Universitas Terbaik di Indonesia
    {
        "name": "Universitas Indonesia (UI)",
        "min_ipk": 3.5,
        "min_sat": 85,
        "min_toefl": 80,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "Institut Teknologi Bandung (ITB)",
        "min_ipk": 3.6,
        "min_sat": 90,
        "min_toefl": 85,
        "penelitian": "baik",
        "rekomendasi": "cukup",
        "sop": "baik"
    },
    {
        "name": "Universitas Gadjah Mada (UGM)",
        "min_ipk": 3.4,
        "min_sat": 80,
        "min_toefl": 75,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Institut Pertanian Bogor (IPB)",
        "min_ipk": 3.5,
        "min_sat": 85,
        "min_toefl": 80,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "Universitas Airlangga (Unair)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Diponegoro (Undip)",
        "min_ipk": 3.4,
        "min_sat": 80,
        "min_toefl": 75,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Padjadjaran (Unpad)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Brawijaya (UB)",
        "min_ipk": 3.2,
        "min_sat": 70,
        "min_toefl": 65,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Sebelas Maret (UNS)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Hasanuddin (Unhas)",
        "min_ipk": 3.4,
        "min_sat": 80,
        "min_toefl": 75,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "Institut Teknologi Sepuluh Nopember (ITS)",
        "min_ipk": 3.5,
        "min_sat": 85,
        "min_toefl": 80,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "Universitas Andalas (UNAND)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Telkom (Telkom)",
        "min_ipk": 3.4,
        "min_sat": 80,
        "min_toefl": 75,
        "penelitian": "baik",
        "rekomendasi": "baik",
        "sop": "baik"
    },
    {
        "name": "Universitas Bina Nusantara (Binus)",
        "min_ipk": 3.2,
        "min_sat": 70,
        "min_toefl": 65,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Trisakti (Trisakti)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Negeri Jakarta (UNJ)",
        "min_ipk": 3.2,
        "min_sat": 70,
        "min_toefl": 65,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Surabaya (UBAYA)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Udayana (Unud)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    },
    {
        "name": "Universitas Sebelas Maret (UNS)",
        "min_ipk": 3.3,
        "min_sat": 75,
        "min_toefl": 70,
        "penelitian": "cukup",
        "rekomendasi": "cukup",
        "sop": "cukup"
    }
]

def evaluasi_peluang(user_data, university=None):
    skor = 0
    if university:
        # Mengambil kriteria minimal dari universitas yang dipilih
        min_ipk = university["min_ipk"]
        min_sat = university["min_sat"]
        min_toefl = university["min_toefl"]
        req_penelitian = university["penelitian"]
        req_rekomendasi = university["rekomendasi"]
        req_sop = university["sop"]
        
        # Evaluasi IPK
        if user_data["ipk"] >= min_ipk:
            skor += 50
        elif user_data["ipk"] >= min_ipk - 0.3:
            skor += 30
        else:
            skor += 10

        # Evaluasi Skor Tes Standar (SAT)
        if user_data["sat"] >= min_sat:
            skor += 40
        elif user_data["sat"] >= min_sat - 150:
            skor += 25
        else:
            skor += 10

        # Evaluasi Skor Bahasa (TOEFL)
        if user_data["toefl"] >= min_toefl:
            skor += 30
        elif user_data["toefl"] >= min_toefl - 20:
            skor += 15
        else:
            skor += 5

        # Evaluasi Pengalaman Penelitian
        if req_penelitian == "ya":
            if user_data["penelitian"] == "ya":
                skor += 30
            else:
                skor += 10
        elif req_penelitian == "baik":
            if user_data["penelitian"] in ["ya", "baik"]:
                skor += 20
            else:
                skor += 10
        else:
            skor += 10

        # Evaluasi Surat Rekomendasi
        rekomendasi_levels = ["cukup", "baik", "sangat baik"]
        user_rekom_index = rekomendasi_levels.index(user_data["rekomendasi"])
        req_rekom_index = rekomendasi_levels.index(req_rekomendasi)
        if user_rekom_index >= req_rekom_index:
            skor += 20
        elif user_rekom_index == req_rekom_index -1:
            skor += 10
        else:
            skor += 5

        # Evaluasi Pernyataan Tujuan (SOP)
        sop_levels = ["cukup", "baik", "sangat baik"]
        user_sop_index = sop_levels.index(user_data["sop"])
        req_sop_index = sop_levels.index(req_sop)
        if user_sop_index >= req_sop_index:
            skor += 25
        elif user_sop_index == req_sop_index -1:
            skor += 15
        else:
            skor += 5

        # Menentukan Peluang berdasarkan skor total
        if skor >= 160:
            peluang = "Tinggi"
        elif 100 <= skor < 160:
            peluang = "Sedang"
        else:
            peluang = "Rendah"

        return skor, peluang
    else:
        # Jika universitas tidak ditentukan, gunakan sistem pakar umum
        # Asumsi: Sama seperti sebelumnya, dapat ditingkatkan atau diubah jika diperlukan
        pass

def find_alternative_university(user_data):
    # Cari universitas terbaik yang kriteria input pengguna penuhi
    for uni in UNIVERSITIES:
        try:
            # Cek IPK
            if user_data["ipk"] < uni["min_ipk"] - 0.3:
                continue
            # Cek SAT
            if user_data["sat"] < uni["min_sat"] - 150:
                continue
            # Cek TOEFL
            if user_data["toefl"] < uni["min_toefl"] - 20:
                continue
            # Cek Pengalaman Penelitian
            if uni["penelitian"] == "ya" and user_data["penelitian"] != "ya":
                continue
            elif uni["penelitian"] == "baik" and user_data["penelitian"] not in ["ya", "baik"]:
                continue
            # Cek Surat Rekomendasi
            rekom_levels = ["cukup", "baik", "sangat baik"]
            user_rekom = rekom_levels.index(user_data["rekomendasi"])
            req_rekom = rekom_levels.index(uni["rekomendasi"])
            if user_rekom < req_rekom -1:
                continue
            # Cek SOP
            sop_levels = ["cukup", "baik", "sangat baik"]
            user_sop = sop_levels.index(user_data["sop"])
            req_sop = sop_levels.index(uni["sop"])
            if user_sop < req_sop -1:
                continue
            # Jika semua kriteria terpenuhi
            return uni["name"]
        except:
            continue
    return None

def submit():
    try:
        ipk = float(entry_ipk.get())
        sat = float(entry_tes.get())
        toefl = float(entry_bahasa.get())

        if not (0.0 <= ipk <= 4.0):
            messagebox.showerror("Input Error", "IPK harus antara 0.0 dan 4.0.")
            return
        if not (400 <= sat <= 1600):
            messagebox.showerror("Input Error", "Skor tes standar (SAT) harus antara 400 dan 1600.")
            return
        if not (0 <= toefl <= 120):
            messagebox.showerror("Input Error", "Skor bahasa harus antara 0 dan 120.")
            return

        penelitian = var_penelitian.get()
        rekomendasi = var_rekomendasi.get()
        sop = var_sop.get()
        kampus = var_kampus.get()

        user_data = {
            "ipk": ipk,
            "sat": sat,
            "toefl": toefl,
            "penelitian": penelitian,
            "rekomendasi": rekomendasi,
            "sop": sop
        }

        # Cari universitas yang dipilih
        selected_uni = next((u for u in UNIVERSITIES if u["name"] == kampus), None)

        skor, peluang = evaluasi_peluang(user_data, selected_uni)

        result = f"Skor Total: {skor}/180\nPeluang Diterima di {kampus}: {peluang}"

        if peluang != "Tinggi":
            # Cari rekomendasi universitas alternatif
            alternative_uni = find_alternative_university(user_data)
            if alternative_uni and alternative_uni != kampus:
                result += f"\n\nRekomendasi Universitas yang Sesuai: {alternative_uni}"
            else:
                result += "\n\nTidak ada rekomendasi universitas alternatif yang sesuai dengan kriteria Anda."

        messagebox.showinfo("Hasil Prediksi", result)

    except ValueError:
        messagebox.showerror("Input Error", "Silakan masukkan nilai yang valid.")

def reset_fields():
    entry_ipk.delete(0, tk.END)
    entry_tes.delete(0, tk.END)
    entry_bahasa.delete(0, tk.END)
    var_penelitian.set("tidak")
    var_rekomendasi.set("baik")
    var_sop.set("baik")
    var_kampus.set("Massachusetts Institute of Technology (MIT)")

# Membuat Jendela Utama
root = tk.Tk()
root.title("Prediksi Penerimaan Universitas Internasional dan Indonesia")
root.geometry("800x900")
root.resizable(False, False)

# Menambahkan Gambar
try:
    img = Image.open("university.png")  # Pastikan Anda memiliki gambar bernama 'university.png' di direktori yang sama
    img = img.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    label_img = tk.Label(root, image=photo)
    label_img.image = photo
    label_img.pack(pady=10)
except Exception as e:
    print("Gambar tidak ditemukan. Melanjutkan tanpa gambar.")

# Judul
label_title = tk.Label(root, text="Prediksi Peluang Penerimaan", font=("Helvetica", 20, "bold"))
label_title.pack(pady=10)

# Frame untuk Input
frame = tk.Frame(root)
frame.pack(pady=10)

# IPK
label_ipk = tk.Label(frame, text="IPK (0.0 - 4.0):", font=("Helvetica", 12))
label_ipk.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_ipk = tk.Entry(frame)
entry_ipk.grid(row=0, column=1, padx=5, pady=5)

# Skor Tes Standar (SAT)
label_tes = tk.Label(frame, text="Skor Tes Standar (SAT 400-1600):", font=("Helvetica", 12))
label_tes.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_tes = tk.Entry(frame)
entry_tes.grid(row=1, column=1, padx=5, pady=5)

# Skor Bahasa (TOEFL)
label_bahasa = tk.Label(frame, text="Skor Bahasa (TOEFL 0-120):", font=("Helvetica", 12))
label_bahasa.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_bahasa = tk.Entry(frame)
entry_bahasa.grid(row=2, column=1, padx=5, pady=5)

# Pengalaman Penelitian
label_penelitian = tk.Label(frame, text="Pengalaman Penelitian:", font=("Helvetica", 12))
label_penelitian.grid(row=3, column=0, sticky="e", padx=5, pady=5)
var_penelitian = tk.StringVar(value="tidak")
radio_penelitian_ya = tk.Radiobutton(frame, text="Ya", variable=var_penelitian, value="ya")
radio_penelitian_tidak = tk.Radiobutton(frame, text="Tidak", variable=var_penelitian, value="tidak")
radio_penelitian_ya.grid(row=3, column=1, sticky="w", padx=5)
radio_penelitian_tidak.grid(row=3, column=1, padx=65, sticky="w")

# Surat Rekomendasi
label_rekomendasi = tk.Label(frame, text="Kualitas Surat Rekomendasi:", font=("Helvetica", 12))
label_rekomendasi.grid(row=4, column=0, sticky="e", padx=5, pady=5)
var_rekomendasi = tk.StringVar(value="baik")
dropdown_rekomendasi = tk.OptionMenu(frame, var_rekomendasi, "sangat baik", "baik", "cukup")
dropdown_rekomendasi.config(width=15)
dropdown_rekomendasi.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Pernyataan Tujuan (SOP)
label_sop = tk.Label(frame, text="Kualitas Pernyataan Tujuan (SOP):", font=("Helvetica", 12))
label_sop.grid(row=5, column=0, sticky="e", padx=5, pady=5)
var_sop = tk.StringVar(value="baik")
dropdown_sop = tk.OptionMenu(frame, var_sop, "sangat baik", "baik", "cukup")
dropdown_sop.config(width=15)
dropdown_sop.grid(row=5, column=1, padx=5, pady=5, sticky="w")

# Pilihan Kampus Tujuan
label_kampus = tk.Label(frame, text="Kampus Tujuan:", font=("Helvetica", 12))
label_kampus.grid(row=6, column=0, sticky="e", padx=5, pady=5)
var_kampus = tk.StringVar(value="Massachusetts Institute of Technology (MIT)")
kampus_list = [uni["name"] for uni in UNIVERSITIES]
dropdown_kampus = tk.OptionMenu(frame, var_kampus, *kampus_list)
dropdown_kampus.config(width=50)
dropdown_kampus.grid(row=6, column=1, padx=5, pady=5, sticky="w")

# Tombol Submit dan Reset
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

button_submit = tk.Button(button_frame, text="Prediksi", font=("Helvetica", 14), command=submit, bg="blue", fg="white", width=12)
button_submit.grid(row=0, column=0, padx=10)

button_reset = tk.Button(button_frame, text="Reset", font=("Helvetica", 14), command=reset_fields, bg="grey", fg="white", width=12)
button_reset.grid(row=0, column=1, padx=10)

# Footer
label_footer = tk.Label(root, text="© 2024 Universitas Internasional dan Indonesia", font=("Helvetica", 10), fg="grey")
label_footer.pack(side="bottom", pady=10)

# Menjalankan Aplikasi
root.mainloop()
