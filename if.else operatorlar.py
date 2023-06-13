# -*- coding: utf-8 -*-
"""
Created on Sun May 21 14:06:03 2023

@author: User
"""
# =============================================================================
# avtolar = ['kia','nexia','onix','mercedez','bmw','lambo']
# for avto in avtolar:
#     if avto == "bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())
# =============================================================================
# =============================================================================
# ism = input("Ismingizni kiriting: >>>\n")
# if ism.lower() != 'nodir':
#     print(f"{ism.title()}, uzur biz Nodirni kutyapmiz")
# else:
#     print("Salom tizimga hush kelibsiz")
# =============================================================================
# =============================================================================
# son = float(input("15x5 nechiga teng:\n"))
# if son != 75:
#     print("Incorrect")
# =============================================================================
# =============================================================================
# yosh = int(input("Yoshingizni kiriting:>> "))
# if yosh <= 18 :
#     print("Tizimga kirish mumkin emas!")
# else:
#     print("Hush kelibsiz")
# =============================================================================
# =============================================================================
# login = input("yangi login tanlang:>>>  ")
# if len(login) <= 10:
#     print("10 ta symboldan koproq bo'lgan login kiriting, iltimos!")
# =============================================================================
yil = int(input("Tugilgan yilingizni kiriting: "))      
if 2023 - yil <= 18:
    print(f" Siz {2023-yil} yoshda ekansiz, kirish mumkin emas! ")
else:
    print("Hush kelibsiz!")
