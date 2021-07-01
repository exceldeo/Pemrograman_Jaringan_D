from library import download_gambar, get_url_list
import time
import socket
import logging
import datetime
import threading
import concurrent.futures
from multiprocessing import Process, Pool

#target IP kirim_sync
TARGET_IP = "192.168.122.255" #Bcast = Broadcast Address
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

def single_thread():
    urls = get_url_list()

    catat = datetime.datetime.now()
    for k in urls:
        print(f"mendownload {urls[k]}")
        waktu_proses = download_gambar(urls[k])
        print(f"completed {waktu_proses} detik")
    selesai = datetime.datetime.now() - catat
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik")

def kirim_multi_process_sync(daftar=None):
    if (daftar is None):
        return False
    f = open(daftar,"rb")
    l = f.read(1024)
    while (l):
        if(sock.sendto(l, (TARGET_IP, TARGET_PORT))):
                l = f.read(1024)
    f.close()

def multi_process_sync():
    texec = dict()
    daftar = ['testing1.png', 'testing2.jpeg']

    catat_awal = datetime.datetime.now()
    for k in range(len(daftar)):
        print(f"mengirim {daftar[k]}")
        texec[k] = Process(target=kirim_multi_process_sync, args=(daftar[k],))
        texec[k].start()
    for k in range(len(daftar)):
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


def kirim_multi_process_async(daftar=None):
    if (daftar is None):
        return False
    f = open(daftar,"rb")
    l = f.read(1024)
    while (l):
        if(sock.sendto(l, (TARGET_IP, TARGET_PORT))):
                l = f.read(1024)
    f.close()

def multi_process_async():
    texec = dict()
    daftar = ['testing1.png', 'testing2.jpeg']
    status_task = dict()
    task_pool = Pool(processes=20)
    catat_awal = datetime.datetime.now()
    for k in range(len(daftar)):
        print(f"mengirim {daftar[k]}")
        texec[k] = task_pool.apply_async(func=kirim_multi_process_async, args=(daftar[k],))
    for k in range(len(daftar)):
        status_task[k]=texec[k].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)

def kirim_multi_thread_sync(daftar=None):
    if (daftar is None):
        return False
    f = open(daftar,"rb")
    l = f.read(1024)
    while (l):
        if(sock.sendto(l, (TARGET_IP, TARGET_PORT))):
                l = f.read(1024)
    f.close()

def multi_thread_sync():
    texec = dict()
    daftar = ['testing1.png', 'testing2.jpeg']

    catat_awal = datetime.datetime.now()
    for k in range(len(daftar)):
        print(f"mengirim {daftar[k]}")
        texec[k] = threading.Thread(target=kirim_multi_thread_sync, args=(daftar[k],))
        texec[k].start()
    for k in range(len(daftar)):
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


def kirim_multi_thread_async(daftar=None):
    if (daftar is None):
        return False
    f = open(daftar,"rb")
    l = f.read(1024)
    while (l):
        if(sock.sendto(l, (TARGET_IP, TARGET_PORT))):
                l = f.read(1024)
    f.close()

def multi_thread_async():
    texec = dict()
    daftar = ['testing1.png', 'testing2.jpeg']
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    
    catat_awal = datetime.datetime.now()
    for k in range(len(daftar)):
        print(f"mendownload {daftar[k]}")
        waktu = time.time()
        texec[k] = task.submit(kirim_multi_thread_async, daftar[k])
    for k in range(len(daftar)):
        status_task[k]=texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)


def menu():
   'Menu pada user'
   while True:
      time.sleep(0.5)
      print("\n=========== Masukkan Perintah ===========")
      print("Ketik '1' untuk melakukan Single Thread")
      print("Ketik '2' untuk melakukan Multi Process Sync")
      print("Ketik '3' untuk melakukan Multi Process Async")
      print("Ketik '4' untuk melakukan Multi thread Sync")
      print("Ketik '5' untuk melakukan Multi thread Async")
      print("Ketik 'keluar' untuk menutup aplikasi\n")
      time.sleep(0.5)
      command = input("Perintah > ")
      if command == "1":
         single_thread()
      elif command == "2":
         multi_process_sync()
      elif command == "3":
         multi_process_async()
      elif command == "4":
         multi_thread_async()
      elif command == "5":
         multi_thread_sync()
      elif command == "keluar":
         closeApp()
      else:
         print("Perintah > Tidak ada perintah")
         continue

def closeApp():
   "Menutup aplikasi"
   time.sleep(0.5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print("Aplikasi akan ditutup. Menutup koneksi dengan server.")
   clientSocket.close() # Menutup socket
   sys.exit() # Keluar menuju ke sistem

# Menampilkan menu
menu()

