# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:15:59 2024

@author: Fairuz Maulidya
"""

class Praktikan:
    def __init__(self):
        self.nama = None
        self.nim = None
        self.fakultas = None
        self.hobi = None
    
    def set_nama(self, nama):
        self.nama = nama
    
    def set_nim(self, nim):
        self.nim = nim
    
    def set_fakultas(self, fakultas):
        self.fakultas = fakultas
    
    def set_hobi(self, hobi):
        self.hobi = hobi
    
    def tampilkan_identitas(self):
        print(f"Nama saya adalah {self.nama} NIM saya ({self.nim}).")
        print(f"Saya dari fakultas {self.fakultas}.")
        print(f"Hobi saya adalah {self.hobi}")

# Membuat objek praktikan dan mengatur atribut-atributnya satu per satu
praktikan1 = Praktikan()
praktikan1.set_nama("Fairuz Maulidya")
praktikan1.set_nim("064002300018")
praktikan1.set_fakultas("Teknik Informatika")
praktikan1.set_hobi("Memasak")

# Menampilkan identitas praktikan
print("----PROGRAM MENAMPILKAN IDENTITAS-----")
praktikan1.tampilkan_identitas()
