# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:03:55 2023

@author: User
"""

# =============================================================================
# def info(name,surname,birth_year,hometown,e_mail='', contact_number=''):
#     yosh = 2023-birth_year
#     info_lugat = {
#         'name':name,
#         'surname':surname,
#         'birth_year':birth_year,
#         'yosh':yosh,
#         'hometown':hometown,
#         'e_mail':e_mail,
#         'contact_number':contact_number
#                   }
#     return info_lugat
# person1 = info('Nodirjon', 'Yusupov', 1997, 'Namangan', e_mail='nrakhimjanovich@gmail.com')#,'998900012028')
# person2 = info('Hoshim', 'Karimov', 2000, 'Tashkent', e_mail='furious@gmail.com', contact_number='998900009897')
# 
# person_info = [person1,person2]
# print("Foydalanuvchi haqida malumotlar: ")
# for info_lugat in person_info:
#     if info_lugat['e_mail']:
#         e_mail = info_lugat['e_mail']
#     elif info_lugat['contact_number']:
#         contact_number = info_lugat['contact_number']
#     else:
#         e_mail = "Not Found"
#         contact_number = "Not Found"
#     print(f"{info_lugat['name']}, {info_lugat['contact_number']}")
# =============================================================================

# =============================================================================
# def info(name,surname,birth_year,hometown,e_mail='', contact_number=None):
#     info_lugat = {
#         'name':name,
#         'surname':surname,
#         'birth_year':birth_year,
#         'yosh':2023-birth_year,
#         'hometown':hometown,
#         'e_mail':e_mail,
#         'contact_number':contact_number
#                   }
#     return info_lugat
# print("Mijoz haqidagi malumotlarni kititing: ")
# mijozlar = []
# while True:
#     name = input("Mijozning ismini kiriting: ")
#     surname = input("Mijozning familiyasini kiriting: ")
#     birth_year = int(input("Mijozning tugilgan yilini kiriting: "))
#     hometown = input("Tugilgan joyingizni kirting: ")
#     e_mail = input("Email manzilingizni kiriting: ")
#     contact_number =input("Telefon nomeringizni kiriting: ")
#     mijozlar.append(info(name, surname, birth_year, hometown,e_mail,contact_number))
#     javob = input("Yana mijoz qo'shishni istasysizmi?(yes/no): ")
#     if javob == "no":
#         break
# print("Mijozlarning royhati: ")
# for info_lugat in mijozlar:
#     print(f"\n{info_lugat['name'].title()} {info_lugat['surname'].title()}, "
#           f"{info_lugat['yosh']} yoshda, {info_lugat['e_mail']}, Contact number: {info_lugat['contact_number']}")
# =============================================================================
def largest(son1,son2,son3):
    max = son1
    if son2>max:
        max = son2
    if son3>max:
        max = son3
    return max
print(largest(10, -80, 42))


    
    




















































































