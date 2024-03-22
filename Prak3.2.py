# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:17:38 2024

@author: Fairuz Maulidya
"""

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def tampilkan_hasil(self):
        luas = self.hitung_luas()
        print(f"Persegi panjang dengan panjang {self.panjang}cm dan lebar {self.lebar}cm memiliki luas sebesar {luas}cm^2")

# Membuat objek persegi panjang
persegi_panjang1 = PersegiPanjang(20, 12)

# Menampilkan hasil perhitungan luas persegi panjang
print("Fairuz Maulidya 064002300018 Teknik Industri")
print(">PROGRAM MENGHITUNG LUAS PERSEGI PANJANG<-----")
persegi_panjang1.tampilkan_hasil()
