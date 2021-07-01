# JALANIN INI
# apk add --no-cache gcc python3-dev jpeg-dev zlib-dev
# apk add --no-cache --virtual .build-deps build-base linux-headers
# pip install Pillow


import socket as sk
from socket import *
import os
import sys
import hashlib
import time

SERVER_NAME = "INS"

serverIp = "192.168.1.45"

host = "" # IP Client
clientPort = 10001 # Port Client
serverAddr = None
buffer = 1024
data = ""
filePath = os.getcwd()+ "/ClientFiles" # Path file client
saveToFile = "" # filename from server to save
COUNTER = 0 # Menghitung percobaan unduh
SENDFILE = "" # Daftar file yang ingin diunduh

# Daftar perintah
LIST = "LIST" # Request daftar file
FILE = "FILE" # Request file yang akan dikirim 
NACK = "NACK" # ACK Positif
PACK =  "PACK" # ACK Negatif
CHECK = "CHECK" # Checksum dari server

# Ambil IP dari server
host = sk.gethostbyname(sk.gethostname())

# Membuat socket server
clientSocket = None
def initSocket():
   "Inisialisasi koneksi dengan server"
   global clientSocket
   global serverAddr
   global serverIp
   serverAddr = (serverIp,10000)
   clientSocket = None # definisi ulang
   clientSocket = socket(AF_INET, SOCK_DGRAM)
   clientSocket.bind((host,clientPort))
initSocket()

# Apabila folder filePath belum ada, maka buat folder tersebut
if not os.path.exists(filePath):
   os.mkdir(filePath)

def menu():
   'Menu pada user'
   while True:
      time.sleep(0.5)
      print("\n=========== Masukkan Perintah ===========")
      print("Ketik 'proses' untuk melakukan image processing")
      print("Ketik 'keluar' untuk menutup aplikasi\n")
      time.sleep(0.5)
      command = input("Perintah > ")
      if command == "proses":
         process()
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

def process():
   'Melakukan image processing pada server'
   global serverAddr
   try:
      clientSocket.sendto("PROCESS".encode("utf-8"), serverAddr)
   except Exception:
      print("Koneksi ke server gagal")
      clientSocket.close() # Menutup socket
      initSocket() # Membuka socket
      return
   print("Menuggu server selesai memproses gambar.")
   data, serverAddr = clientSocket.recvfrom(buffer)
   time.sleep(0.5)
   totalTime = data.decode("utf-8").strip()
   totalTime = totalTime.split("\t")
   print("Waktu image processing dengan multiprocessing adalah: ", totalTime[0], " seconds")
   print("Waktu image processing dengan multithreading adalah: ", totalTime[1], " seconds")
   print("Waktu image processing dengan multiprocessing asynchronous adalah: ", totalTime[2], " seconds")
   print("Waktu image processing dengan multithreading asynchronous adalah: ", totalTime[3], " seconds")
   return

# Menampilkan menu
menu()