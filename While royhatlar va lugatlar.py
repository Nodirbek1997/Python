# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:23:13 2023

@author: User
"""
# =============================================================================
# buyurtma = []
# n = 1
# while True:
#     buyumlar = input(f"{n}-mahsulotni nomini kiriting: ")
#     buyurtma.append(buyumlar)
#     extra = input("Yana buyum olishni hohlaysizmi (yes/no): ")
#     if extra == "yes":
#         n+=1
#         continue
#     else:
#         break
# print("\nBuyurtma qilingan mahsulotlar royhati: ")
# for buyurtmalar in buyurtma:
#     print(buyurtmalar)
# =============================================================================

# =============================================================================
# print("E-bazar uchun mahsulotlar royhati va ularni narhlarini chiqaruvchi dastur:")
# bazar = {}
# ishora = True
# while ishora:
#       mahsulot = input("Mahsulotning nomini kiriting: ")
#       narh = int(input("Mahsulotning narhini kiriting: "))
#       bazar[mahsulot] = narh
#       
#       extra = input("Yana boshqa mahsulot olishni istaysizmi(yes/no): ")
#       if extra == "no":
#          ishora = False
# 
# print("\nMahsulotlar va ularning narhlari")         
# for mahsulot,narh in bazar.items():
#     print(f"{mahsulot.title()}ning narhi >>> {narh}")
# =============================================================================
    
mahsulotlar = ['olma','anor','nok','behi','daftar','ruchka']
e_bazar = {
    'anor':2000,
    'nok':3000,
    'sabzi':5000,
    'behi':7000,
    'kartoshka':3500
    }
while mahsulotlar:
    buyurtma = mahsulotlar.pop()
    if buyurtma in e_bazar.keys():
        narh = e_bazar[buyurtma]
        print(f"{buyurtma.title()}ning narhi - {narh} som")
    else:
        print(f"Bizda {buyurtma.title()} mavjud emas")
        
      
    
    
    
    
