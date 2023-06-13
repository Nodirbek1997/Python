# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:12:44 2023

@author: User
"""
# =============================================================================
# talaba_0 = {'ism':'Nodir',
#             'familiya':'Yusupov',
#             'kurs':4,
#             'yosh':26,
#             'fakultet':'Economics'
#             }
# #print(talaba_0.items())
# =============================================================================
# =============================================================================
# for key,value in talaba_0.items():
#     print(f"Qiymat: {value}")
#     print(f"Kalit: {key}")
# =============================================================================
# =============================================================================
# mahsulotlar = {
#     'olma':10000,
#     'anor':9000,
#     'bodring':3000,
#     'pomidor':5000,
#     'balgar':3500
#     }
# =============================================================================
#print(mahsulotlar.keys())

# =============================================================================
# print("Do\'kondagi mahsulotlar: ")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# =============================================================================
# =============================================================================
# bozorlik = ['piyoz','anor','shaftoli','pomidor','bodring']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# 
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizga quyidagi {buyum} mahsulotlarni ham olib keling")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# =============================================================================
telefonlar = {'ali':'Iphone X',
              'vali':'Nokia 1202',
              'karim':'Galaxy A40',
              'Nodir':'Iphone 15 pro max',
              'Doni':'RealMI 15',
              'Olim':'Iphone X',
              'Hoshim':'RealMI 15',
              'Ozoda':'Iphone 15 pro max'
              }
# =============================================================================
# print(telefonlar['ali'])
# phone = telefonlar.get('Doni','Bunday qiymat mavjud emas')
# print(phone)
# =============================================================================
#print(telefonlar.values())
print("Foydanalanuvchilar quyidagi rusmdagi telefonlar ishlatishadi: ")
for tel in sorted(set(telefonlar.values())):
    print(tel)
    
toys = {'bear','car','doll','car','lamb','camel','bear'}
print(toys)















































