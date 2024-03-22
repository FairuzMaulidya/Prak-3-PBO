# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:15:59 2024

@author: Fairuz Maulidya
"""

class Praktikan:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi
    
    def tampilkan_identitas(self):
        print(f"Nama saya adalah {self.nama} NIM saya ({self.nim}).")
        print(f"Saya dari fakultas {self.fakultas}.")
        print(f"Hobi saya adalah {self.hobi}")

# Membuat objek praktikan
praktikan1 = Praktikan("Fairuz Maulidya", "064002100018", "Teknik Informatika", "Memasak")

# Menampilkan identitas praktikan
print("----PROGRAM MENAMPILKAN IDENTITAS-----")
praktikan1.tampilkan_identitas()
