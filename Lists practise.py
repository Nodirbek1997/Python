# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:50:05 2023

@author: User
"""
# print(mevalar)
# narxlar = [1200,2500,16000,13000,-55,70.2]
# print(narxlar)
# print(mevalar[2])
# print(mevalar[3].upper())
# print(narxlar[0]+narxlar[1])
# mevalar[0] = "banan"
# print(mevalar)
# =============================================================================
# =============================================================================
# mevalar.append('uzum')
# print(mevalar)
# 
# =============================================================================
# =============================================================================
# cars = []
# cars.append('BMW')
# print(cars)
# cars.append('Spark')
# cars.append('Lambo')
# print(cars)
# =============================================================================
# =============================================================================
# hayvonlar = ['mol', ' qoy', 'buzoq', 'quyon', 'ot', 'mol']
# print(hayvonlar)
# domestic = hayvonlar.pop(1)
# print(hayvonlar)
# =============================================================================
# =============================================================================
# ismlar = ['Doniyor','Suronjon', 'Zuhriddin']
# ism1 = ismlar.pop(0)
# print("Salom "  + ism1 + ", bugun choyxona bormi?")
# ism2 = ismlar.pop(1)
# print("Do'stim " + ism2 + " futbol ko'rgani boramizmi?")
# =============================================================================
# =============================================================================
# sonlar = [125,-66,2.5,12]
# print(sonlar[0] / sonlar[2])
# =============================================================================
# =============================================================================
# t_shaxslar = ['Amir Temur', 'Napaleon','Columb','Sezar','Hitler']
# z_shaxslar = ['Alpachino','Barack Obama','Ferguson','Steve Jobs']
# #      1
# old = t_shaxslar.pop(0)
# modern = z_shaxslar.pop(2)
# print("Men tarixxiy shaxslardan " + old + " bilan, zamonaviy shaxslardan esa " + modern + " bilan suhbat qurishni istar edim")
# =============================================================================
friends = []
print(friends)
friends.append('Doni')
friends.append('Sergey')
friends.append('Salohiddin')
friends.append('Ibn sino')
friends.append('Zuhi')
print(friends)
friends.remove('Salohiddin')
friends.remove('Ibn sino')
print(friends)
friends.insert(0,'Maqsud')
friends.insert(2,'Nodir')
friends.append('Jamshid')
print(friends)
yangi_mehmonlar = []
yangi_mehmonlar.append(friends.pop(0))
yangi_mehmonlar.append(friends.pop(2))
yangi_mehmonlar.append(friends.pop(-1))
print("\n Yangi kelgan mehmonlar:", yangi_mehmonlar)
