# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 13:06:37 2023

@author: User
"""
# =============================================================================
# print("Doslaringizni royhatini chiqaruvchi dastur: ")
# ismlar = []
# n=1
# while True:
#     savol = f"{n}-dostingizni kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     extra = "Yana boshqa do'stingizni qoshishni hohlaysizmi: (yes/no) >> "
#     n+=1
#     nom = input(extra)
#     if nom !="yes":
#         break
# print("Yaqin dostlaringiz royxati quyidagilardan iborat: ")
# for ism in ismlar:
#     print(ism)
# =============================================================================
 
print("Do'stlaringizni yoshini chiqaruvchi dastur: ")
savol = {}
ishora = True
while ishora:
    ism = input("Do'stingizni ismini kiriting: ")
    yosh = input("Do'stingizni yoshini kiriting: ")
    