import os
import socket
import random
import time

# Clear Layar
os.system("clear")

# Banner EXEC
print("\033[1;31m" + r"""
 ███████╗██╗  ██╗███████╗ ██████╗ 
 ██╔════╝██║  ██║██╔════╝██╔═══██╗
 ███████╗███████║█████╗  ██║   ██║
 ╚════██║██╔══██║██╔══╝  ██║   ██║
 ███████║██║  ██║███████╗╚██████╔╝
 ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ 
            📱 EXEC 📲
""" + "\033[0m")
      
mode = input("\033[93m" + "Mau Jadi (1).Server Atau (2).Client? " + "\033[0m")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def port():
    import random
    return random.choice([1024, 4444, 10000, 12345, 65535])

server_port = port()   # Ambil Port 

def random_port(check_free=True, low=10000, high=65535, tries=1000):
    import random, socket
    if low < 0: low = 0
    total = high - low + 1
    if tries >= total:
        ports = list(range(low, high+1))
        random.shuffle(ports)
        iterator = ports
    else:
        iterator = (random.randint(low, high) for _ in range(tries))
    seen = set()
    for p in iterator:
        if p in seen: continue
        seen.add(p)
        if not check_free:
            return p
        s = socket.socket()
        try:
            s.bind(('0.0.0.0', p))
            s.close()
            return p
        except OSError:
            s.close()
    return None

if mode == "1":
    # SERVER
    host = "0.0.0.0"
    port = port() 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print("\033[96m" + f"📡 Connect IP Server: {get_local_ip()}" + "\033[0m")
    conn, addr = s.accept()    
    print("\033[92m" + f"\n✅ Terhubung Dari {addr}\n" + "\033[0m")    

    while True:
        cmd = conn.recv(1024).decode().strip()
        if not cmd:
            break        
        print("\033[0m" + " " + "\033[92m" + f"$" + "\033[0m" + " " + cmd)
        try:
            if cmd.lower() == "clear":
                # Kalau Perintah Clear → Jangan Hilangin Banner
                output = "\033c" + "\033[1;31m" + r"""
 ███████╗██╗  ██╗███████╗ ██████╗ 
 ██╔════╝██║  ██║██╔════╝██╔═══██╗
 ███████╗███████║█████╗  ██║   ██║
 ╚════██║██╔══██║██╔══╝  ██║   ██║
 ███████║██║  ██║███████╗╚██████╔╝
 ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ 
            📱 EXEC 📲
""" + "\033[0m\n"
            else:
                # Jalankan Perintah Lain
                output = os.popen(cmd).read()
                if not output:
                    output = "\033[1;31m" + "\033[0m" + " " + "\033[0m"
        except Exception as e:
            output = "\033[1;31m" + f"{str(e)}" + "\033[0m"

        # Tampilkan Di Server, Tapi Blokir Clear
        if cmd.lower() != "clear":
            os.system(cmd)
            print(" ")
        else:
            print(" ")
        
        # Kirim Balik Ke Client
        conn.send(output.encode())

elif mode == "2":
    # CLIENT
    server_ip = input("\033[96m" + "Masukkan IP Server: " + "\033[0m")    
    port = port()       
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))
    
    print("\033[92m" + f"✅ Terhubung Oleh {server_ip}: {random_port(check_free=True, low=10000, high=65535, tries=1000)}\n" + "\033[0m")

    while True:
        cmd = input("\033[0m" + " " + "\033[92m" + "$" + "\033[0m" + " ")        
        if not cmd.strip():
            continue
        s.send(cmd.encode())
        # Terima Hasil Dari Server
        result = s.recv(4096).decode()
        print(result)
