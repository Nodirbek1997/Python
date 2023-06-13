# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:25:17 2023

@author: User
"""

# =============================================================================
# juft_son = int(input("Juft son kiriting: "))
# if juft_son % 2 == 0:
#     print("Bu juft son")
# else:
#     print("Bu juft son emas")
# =============================================================================
# =============================================================================
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4 or yosh >= 60:
#     print("Chipta narhi bepul")
# elif yosh <= 18:
#     print("Chipta narhi 1 000 so'm")
# elif yosh > 18:
#     print("Chipta narhi 2 000 so'm")
# =============================================================================
# =============================================================================
# a = int(input("a sonni kiriting: "))
# b = int(input("b sonni kiriting: "))
# if a<b:
#     print("b son katta")
# elif a>b:
#     print("a son katta")
# =============================================================================
# =============================================================================
# mahsulotlar = ['olma','anor','nok','non','snikers','bounty','kartoshka','bodring','lagman','smetana']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Bizda {mahsulot} mavjud")
#     else:
#         print(f"Bizda {mahsulot} mavjud emas")
# for exist in mahsulot:
# =============================================================================
# =============================================================================
# mahsulotlar = ['olma','anor','nok','non','snikers','bounty','kartoshka','bodring','lagman','smetana']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting: "))
# 
# bor_mahsulotlar = []
# mavjud_emas =[]
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#         
# if mavjud_emas:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#         print("Siz so'ragan mahsulotlar do'konimizda mavjud emas")
# =============================================================================
# =============================================================================
# foydalanuvchilar = ['Nodek','Nodir','Maverick','Nodirbek','Nodirjon']
# yangi = input("Yangi login kiriting: ")
# if yangi.title() in foydalanuvchilar:
#     print("Tizimga hush kelibsiz")
# else:
#     print("Yangi login kiriting")
# =============================================================================
son = int(input("Istalgan sonni kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} soniga qoldiqsiz bo'linadi")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        