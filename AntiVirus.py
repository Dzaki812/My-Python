#!/usr/bin/env python3
# Fungsi: Menghapus File Yang Mengandung 'msg', 'stk-', 'doc-', '=.', '.apk', '.xapk', Atau '.zip' Dan Menghapus File Berukuran Kurang Dari 22.00B Dan Menghapus File Berukuran Lebih Dari 1GB 
# Fungsi2: Menghapus File '.nomedia' Tanpa Wildcard Atau Asterisk  
# Fungsi3: Menghapus Folder '.Shared', '.Links' Tanpa Wildcard Atau Asterisk Dan Hanya Menampilkan File Nya Saja 
# Banner Besar "ANTI" Tanpa pyfiglet

import os
from pathlib import Path
 
os.system("clear")

#!/usr/bin/env python3
import os
import subprocess

# Langkah 1: Masuk Ke HOME
home = os.path.expanduser("~")
os.chdir(home)
bashrc_path = os.path.join(home, ".bashrc")

# Langkah 2: Tambahkan Fungsi Ke .bashrc
fungsi = '\nr() { fc -s; }\n'

# Cek Apakah Sudah Ada Fungsi r Di .bashrc
if os.path.exists(bashrc_path):
    with open(bashrc_path, "r") as file:
        isi = file.read()
    if 'r() { fc -s; }' not in isi:
        with open(bashrc_path, "a") as file:            
            file.write(fungsi)
        print(" ") 
        os.system("clear")
    else:
        print(" ") 
        os.system("clear")
else:
    # Kalau .bashrc Belum Ada, Buat Baru
    with open(bashrc_path, "w") as file:                
        file.write(fungsi)
    
# Langkah 3: Aktifkan Fungsi Tanpa Restart Termux
os.system("source ~/.bashrc")

os.system("clear")

def merek_hape():
    import subprocess
    try:
        brand = subprocess.check_output(["getprop", "ro.product.brand"]).decode().strip()
        model = subprocess.check_output(["getprop", "ro.product.model"]).decode().strip()
        
        # Gabungkan Brand + Model Lalu Buat Setiap Kata Huruf Depannya Besar
        full_name = f"{brand} {model}".title()
        
        return full_name
    except:
        return ""  # Tidak Ada Teks

import os
import time

# Warna-Warna Indah Yang Ada
hitam = "\033[30m"
merah = "\033[31m"
hijau = "\033[32m"
kuning = "\033[33m"
biru = "\033[34m"
ungu = "\033[35m"
cyan = "\033[36m"
putih = "\033[37m"
hitam_muda = "\033[90m"     
merah_muda = "\033[91m"     
hijau_muda = "\033[92m"     
kuning_muda = "\033[93m"    
biru_muda = "\033[94m"      
ungu_muda = "\033[95m"      
cyan_muda = "\033[96m"      
putih_muda = "\033[97m"     
tebal_hitam = "\033[1;30m"
tebal_merah = "\033[1;31m"
tebal_hijau = "\033[1;32m"
tebal_kuning = "\033[1;33m"
tebal_biru = "\033[1;34m"
tebal_ungu = "\033[1;35m"
tebal_cyan = "\033[1;36m"
tebal_putih = "\033[1;37m"
bg_hitam = "\033[40m"
bg_merah = "\033[41m"
bg_hijau = "\033[42m"
bg_kuning = "\033[43m"
bg_biru = "\033[44m"
bg_ungu = "\033[45m"
bg_cyan = "\033[46m"
bg_putih = "\033[47m"
bg_hitam_muda = "\033[100m"
bg_merah_muda = "\033[101m"
bg_hijau_muda = "\033[102m"
bg_kuning_muda = "\033[103m"
bg_biru_muda = "\033[104m"
bg_ungu_muda = "\033[105m"
bg_cyan_muda = "\033[106m"
bg_putih_muda = "\033[107m"
reset = "\033[0m"
bold = "\033[1m"

def Home_Termux():     
    # Pindah Ke HOME Termux
    home_path = os.path.expanduser("~")
    os.chdir(home_path)

    for _ in range(4):
        os.system("clear")         
        print(kuning_muda + f"⏳ Mencari Penyimpanan {merek_hape()}" + reset)
        time.sleep(0.50)        
    
        os.system("clear")         
        print_text = kuning_muda + f" ⏳ Mencari Penyimpanan {merek_hape()}" + reset

        for _ in range(1):  # Ulang Animasi 1 Kali
            for dots in range(1, 2):
                print(f"{print_text}{'\033[93m \033[0m' * dots}  ", end="\r", flush=True)         
                time.sleep(0.50)  
        print(" " * (len(print_text) + 3), end="\r")  # Bersihkan Baris Setelah Animasi

        os.system("clear")         
        base_text = kuning_muda + f" ⏳ Mencari Penyimpanan {merek_hape()}" + reset

        for _ in range(1):  # Ulang Animasi 1 Kali
            for dots in range(1, 4):
                print(f"{base_text}{'\033[93m.\033[0m' * dots}  ", end="\r", flush=True)         
                time.sleep(0.50)  
        print(" " * (len(base_text) + 3), end="\r")  # Bersihkan Baris Setelah Animasi

        os.system("clear")                         
        print(kuning_muda + f"⏳ Mencari Penyimpanan {merek_hape()}.." + reset)
        time.sleep(0.50)        

        os.system("clear")                         
        print(kuning_muda + f"⏳ Mencari Penyimpanan {merek_hape()}..." + reset)
        time.sleep(0.50)        

def Penyimpanan():   
    time.sleep(31.60)
    os.system("clear")

    # Coba Akses storage/emulated/0
    storage_path = "/storage/emulated/0"

    if os.path.exists(storage_path):
        os.chdir(storage_path)
        # Contoh Pemakaian Merek Hape
        print(f"" + hijau_muda + f"✅ Penyimpanan {merek_hape()}" + reset)
        time.sleep(02.31)
        os.system("clear")
    else:
        os.system("termux-setup-storage") 
        os.system("clear")

        # Coba Jalankan r(), Kalau Gagal Langsung clear && login
        exit_code = os.system("r")

        if exit_code != 0:  # Kalau r() Gagal (Exit Code Selain 0)
            os.system("clear && login")    

os.system("clear")

# ========== BANNER BESAR TANPA PYFIGLET ==========

banner = r"""
 █████╗ ███╗   ██╗████████╗██╗
██╔══██╗████╗  ██║╚══██╔══╝██║
███████║██╔██╗ ██║   ██║   ██║
██╔══██║██║╚██╗██║   ██║   ██║
██║  ██║██║ ╚████║   ██║   ██║
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝
          ANTI VIRUS   
"""

import sys
import time

def animasi_loading():
    for _ in range(4):
        os.system("clear") 
        print(merah_muda + banner + reset)  # Warna Merah Terang
        print(kuning_muda + "⏳ Tunggu Sedang Melihat File" + reset)
        time.sleep(0.50)        
    
        os.system("clear") 
        print(merah_muda + banner + reset)  # Warna Merah Terang
        print_text = kuning_muda + " ⏳ Tunggu Sedang Melihat File" + reset

        for _ in range(1):  # Ulang Animasi 1 Kali
            for dots in range(1, 2):
                print(f"{print_text}{'\033[93m \033[0m' * dots}  ", end="\r", flush=True)         
                time.sleep(0.50)  
        print(" " * (len(print_text) + 3), end="\r")  # Bersihkan Baris Setelah Animasi

        os.system("clear") 
        print(merah_muda + banner + reset)  # Warna Merah Terang
        base_text = kuning_muda + " ⏳ Tunggu Sedang Melihat File" + reset

        for _ in range(1):  # Ulang Animasi 1 Kali
            for dots in range(1, 4):
                print(f"{base_text}{'\033[93m.\033[0m' * dots}  ", end="\r", flush=True)         
                time.sleep(0.50)  
        print(" " * (len(base_text) + 3), end="\r")  # Bersihkan Baris Setelah Animasi

        os.system("clear")
        print(merah_muda + banner + reset)  # Warna Merah Terang                 
        print(kuning_muda + "⏳ Tunggu Sedang Melihat File.." + reset)
        time.sleep(0.50)        

        os.system("clear")
        print(merah_muda + banner + reset)  # Warna Merah Terang                 
        print(kuning_muda + "⏳ Tunggu Sedang Melihat File..." + reset)
        time.sleep(0.50)        

import time
import sys

def LOADING():  # Gak Berguna! 
    base_text = "⏳ Tunggu Sedang Melihat File"
    for _ in range(2):  # Ulang Animasi 2 Kali
        for dots in range(4):  # 0,1,2,3 Titik
            print(f"{base_text}{'.'*dots}   ", end="\r", flush=True)
            time.sleep(0.5)
    # Pastikan Baris Terakhir Muncul
    print(f"{base_text}..." + " " * 3)

def print_banner():
    os.system("clear")
    banner = r"""
 █████╗ ███╗   ██╗████████╗██╗
██╔══██╗████╗  ██║╚══██╔══╝██║
███████║██╔██╗ ██║   ██║   ██║
██╔══██║██║╚██╗██║   ██║   ██║
██║  ██║██║ ╚████║   ██║   ██║
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝
          ANTI VIRUS   
"""

    animasi_loading()

# ========== PEMBERSIH FILE ==========
import sys

AUTO_Y = False
if len(sys.argv) > 1 and sys.argv[1] == "-y":
    AUTO_Y = True

import sys
import os
import signal

def hapus_file_msg(folder="."):
    root = Path(folder)
    if not root.exists():
        os.system("clear")
        print(merah_muda + banner + reset)  # Warna Merah Terang
        print(kuning_muda + "⚠️ Folder Tidak Ada.\n" + reset)
        return

    # Ubah Bagian Filter Files: Hapus .zip, Tetap Tampilkan .apk Dan .xapk
    files = [f for f in root.rglob("*") if f.is_file() and (
        "msg" in f.name.lower() or
        "stk-" in f.name.lower() or
        "doc-" in f.name.lower() or   # <-- Tambahan Ini
        f.name.lower() == ".nomedia" or
        "=." in f.name.lower() or
        f.suffix.lower() in [".apk", ".xapk"]   # <-- Tambah Ini
    )]

    # Kumpulkan Semua .nomedia (Ikut Konfirmasi Y/n)
    nomedia_files = [f for f in root.rglob(".nomedia") if f.is_file()]
    files.extend(nomedia_files)

    # Tambahan: Hapus File Berdasarkan Ukuran
    for f in root.rglob("*"):
        if not f.is_file():
            continue
        ukuran = f.stat().st_size
        # Hapus Jika ≤22B Atau ≥1GB
        if ukuran <= 22 or ukuran >= 1_000_000_000:
            if f not in files:
                files.append(f)

    # Tambahkan File Dari .Shared Dan .Links
    for folder_name in [".Shared", ".Links"]:
        folder_path = Path(folder_name)
        if folder_path.exists():
            for f in folder_path.iterdir():
                if f.is_file() and f not in files:
                    files.append(f)

    # <<< LETAKKAN HILANGKAN DUPLIKAT DI SINI >>>
    unik = []
    for f in files:
        full_path = str(f.resolve())  # path Absolut
        if full_path not in unik:
            unik.append(full_path)
    files = [Path(u) for u in unik]

    # <<< HILANGKAN DUPLIKAT BERDASARKAN NAMA FILE >>>
    unik_nama = []
    unik_files = []
    for f in files:
        if f.name not in unik_nama:
            unik_nama.append(f.name)
            unik_files.append(f)
    files = unik_files

    # Sekarang Tampilkan Files Ke Layar

    # Hapus Folder '.Shared' Atau '.Links'
    folders = [d for d in root.rglob("*") if d.is_dir() and d.name in [".Shared", ".Links"]]
    if not files:
        os.system("clear")
        print(merah_muda + banner + reset)  # Warna Merah Terang
        print(kuning_muda + "⚠️ Tidak Ada Sampah.\n" + reset)
        return

    files = list(dict.fromkeys(files))  # Hilangkan Duplikat

    os.system("clear") 
    print(merah_muda + banner + reset)  # Warna Merah Terang

    # Hilangkan Duplikat Berdasarkan Full Path
    unik = []
    for f in files:
        full_path = str(f.resolve())  # path absolut
        if full_path not in unik:
            unik.append(full_path)
    files = [Path(u) for u in unik]

    # Hapus File Yang Berasal Dari .Shared Dan .Links Agar Tidak Tampil Dua Kali
    files = [f for f in files if ".Shared" not in str(f) and ".Links" not in str(f)]

    # Baru Tampilkan     

    # Setelah Files Selesai Di-Filter Dan Duplikat Dihapus
    total_files = len(files)
 
    print(f""+ kuning_muda + "📥 Ditemukan Adanya",total_files,"Sampah",reset)
    # Tampilkan File Biasa

    # Lanjutkan Tampilkan File Satu Per Satu
    for f in files:
        nama_file = f.name
        max_len = 30
        potongan = [nama_file[i:i+max_len] for i in range(0, len(nama_file), max_len)]
        for i, bagian in enumerate(potongan):
            if i == 0:
                print(" - " + cyan_muda + bagian + reset)
            else:
                print("   " + cyan_muda + bagian + reset)  # Tambah 3 Spasi Untuk Baris Lanjutan

    # Kalau Tidak Ada File Sama Sekali
    if not files:
        os.system("clear")
        print(merah_muda + banner + reset)  # Warna Merah Terang                
        print(f"" + kuning_muda + "📥 Ditemukan Adanya Sampah" + reset)
        print(" - " + cyan_muda + "File Tersembunyi." + reset)
        
    # Tampilkan Isi Folder .Shared Saja
    shared_path = Path(".Shared")
    if shared_path.exists():
        shared_files = [f for f in shared_path.iterdir() if f.is_file()]
        for f in shared_files:
            if f in files:  # Skip Kalau Sudah Ditampilkan
                continue
            nama_file = f.name
            max_len = 30
            potongan = [nama_file[i:i+max_len] for i in range(0, len(nama_file), max_len)]
            for i, bagian in enumerate(potongan):
                if i == 0:
                    print(" - " + cyan_muda + bagian + reset)
                else:
                    print("   " + cyan_muda + bagian + reset)  # Tambah 3 Spasi Untuk Baris Lanjutan
        
    # Tampilkan Isi Folder .Links Saja
    links_path = Path(".Links")
    if links_path.exists():
        links_files = [f for f in links_path.iterdir() if f.is_file()]
        for f in links_files:
            if f in files:  # Skip Kalau Sudah Ditampilkan
                continue
            nama_file = f.name
            max_len = 30
            potongan = [nama_file[i:i+max_len] for i in range(0, len(nama_file), max_len)]
            for i, bagian in enumerate(potongan):
                if i == 0:
                    print(" - " + cyan_muda + bagian + reset)
                else:
                    print("   " + cyan_muda + bagian + reset)  # Tambah 3 Spasi Untuk Baris Lanjutan        

    # 4. Hapus Semua Duplikat (Full Path) ← PASANG DI SINI
    files = list({str(f.resolve()): f for f in files}.values())

    # Kalau Semua Kosong
    if not files and (not shared_path.exists() or not any(shared_path.iterdir())) and (not links_path.exists() or not any(links_path.iterdir())):
        os.system("clear")
        print(merah_muda + banner + reset)  # Warna Merah Terang                
        print(f"" + kuning_muda + "📥 Ditemukan Adanya Sampah"  + reset)
        print(" - " + cyan_muda + "File Tersembunyi." + reset)
        
    # <<< HAPUS DUPLIKAT FULL PATH DI SINI <<< 
    files = list({str(f.resolve()): f for f in files}.values())

    # Gabungkan Semua File Termasuk Dari .Shared Dan .Links
    all_files = set(files)  # Mulai Dari File Biasa

    # Tambahkan .Shared
    shared_path = Path(".Shared")
    if shared_path.exists():
        for f in shared_path.iterdir():
            if f.is_file():
                all_files.add(f)

    # Tambahkan .Links
    links_path = Path(".Links")
    if links_path.exists():
        for f in links_path.iterdir():
            if f.is_file():
                all_files.add(f)

    # Hapus Semua Duplikat Berdasarkan Full Path
    all_files = list({str(f.resolve()): f for f in all_files}.values())

    # Pisahkan Non-hidden & Hidden Tapi Bukan .nomedia
    main_files = [f for f in all_files if not f.name.startswith(".") and f.name.lower() != ".nomedia"]
    hidden_files = [f for f in all_files if f.name.startswith(".") and f.name.lower() != ".nomedia"]

    # Tampilkan File Utama
    def main_files():  # Gak Berguna! 
        for f in main_files:
            print(" - " + cyan_muda + f.name + reset)

    # Tampilkan File Hidden
    def hidden_files():  # Gak Berguna! 
        for f in hidden_files:
            print(" - " + cyan_muda + f.name + reset)

    if AUTO_Y:
        konfirmasi = "y"
        print("\n" + hijau_muda + "[Y/n] Yakin Ingin Dibersihkan? " + reset + konfirmasi)
    else:
        konfirmasi = input("\n" + hijau_muda + "[Y/n] Yakin Ingin Dibersihkan? " + reset).strip().lower()

    if konfirmasi != "y":
        print(merah_muda + "\n❌ Dibatalkan.\n" + reset)
        return "n"  # ← Return Ke Loop Utama

        # Hentikan Program Secara Paksa (Seperti CTRL+C)
        try:
            # Kirim KeyboardInterrupt Ke Proses Saat Ini
            os.kill(os.getpid(), signal.SIGINT)
        except KeyboardInterrupt:
            pass
    
        # Exit Paksa Sebagai Backup
        sys.exit(1)        

    total = 0
    # Hapus File
    for f in files:
        try:
            f.unlink()
        except FileNotFoundError:
            pass  # Diam Aja Kalau File Udah Gak Ada
        except Exception as e:
            print(f"\n{f} {e}\n")

    # Hapus Folder
    for d in folders:
        try:
            import shutil
            shutil.rmtree(d)
        except Exception as e:
            print(f"\n{d} {e}\n")

    print(f"" + hijau_muda +"\n✅ Selesai! \n" + reset)
    return "y"  # ← Tambahkan Di Akhir Kalau Lanjut

# ========== MAIN ==========
if __name__ == "__main__":
    import sys, time, os

    args = sys.argv[1:]
    mode_always = "always" in args
    AUTO_Y = "-y" in args

    delay = 1  # Mulai Dari 1 Detik

    while True:
        os.system("clear")
        Home_Termux()   # /data/data/com.termux/files/home/       
        Penyimpanan()  # /storage/emulated/0/   
        print_banner()
        
        # Tangkap Return Value
        result = hapus_file_msg(".")  # <- HARUS Disimpan Ke Variabel
        
        if not mode_always:
            break  # Keluar Kalau Gak Pakai Always
    
        # Cek Hasil Konfirmasi
        if result == "n":  # User Menekan N            
            # Hentikan program Seakan CTRL+C
            try:
                os.kill(os.getpid(), signal.SIGINT)
            except KeyboardInterrupt:
                pass
            sys.exit(1) 

        if not mode_always:
            break  # Keluar Kalau Gak Pakai Always    
                
        # Tanya Konfirmasi (Kecuali Mode -Y)
        if not AUTO_Y:
            if 'konfirmasi' in locals() and konfirmasi == "n":
                break
            
        # Tunggu Sebelum Mengulang        
        time.sleep(delay)
        delay = delay + 1 if delay < 10 else 10  # Batas Maksimal 10 Detik
        delay += 1  # Setiap Loop Bertambah 1 Detik
        os.system("clear")
