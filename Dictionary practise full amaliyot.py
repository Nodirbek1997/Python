# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:48:56 2023

@author: User
"""
#    PRACTISE 1 AND 2
# =============================================================================
# xorazmiy = {
#     'ism':'Muhammad al-xorazmiy',
#     'tyil':1402,
#     'millat':'uzbek',
#     'famous for': 'algebra',
#     'asar':'al-jabr val muqobala'
#     }
# ulugbek = {
#     'ism':'Mirzo Ulugbek',
#     'tyil':1508,
#     'millat':'uzbek',
#     'famous for': 'astronomy',
#     'asar':'jizzi koragoniy'
#     }
# ibn_sino = {
#     'ism':'Abu ali Ibn Sino',
#     'tyil':1308,
#     'millat':'afgon',
#     'famous for': 'medicine',
#     'asar':'avitsena'
#     }
# ferguson = {
#     'ism':'Alex Ferguson',
#     'tyil':1956,
#     'millat':'english',
#     'famous for': 'ManU fc',
#     'asar':'We are the champions'
#     }
# 
# # =============================================================================
# # famous = [xorazmiy,ulugbek,ibn_sino,ferguson]
# # for shaxs in famous:
# #     ism = shaxs['ism']
# #     tyil = shaxs['tyil']
# #     millat = shaxs['millat']
# #     famous_for = shaxs['famous for']
# #     print(f"\n{ism} {tyil}-yilda tugilgan. Millati {millat.title()}. {ism.title()}" 
# #           f"{famous_for.upper()} uchun mashxurlikka erishgan!")
# # =============================================================================
# mashxurlar = [xorazmiy,ulugbek,ibn_sino,ferguson]
# for shaxs in mashxurlar:
#     ism = shaxs['ism']
#     asar = shaxs['asar']
#     print(f"\n{ism.title()} {asar.title()} ni yozgan va shu orqali mashxur bolgan")
# =============================================================================
#       PRACTISE 3
# =============================================================================
# kino = {'Doni':['Titanic,',' Scarface,',' Mission Impossible'],
#         'Sergey':['Soldat,',' T-34,',' Missiya'],
#         'Bunyod':['Qalb,',' Kozgu,',' Kamina']
#         }
# for ism,kino in kino.items():
#     print(f"\n{ism.title()}ning sevimli kinolari quyidagilar: ", end="")
#     for kinolar in kino:
#         print(kinolar, end="")
# =============================================================================
#        PRACTISE 4
# =============================================================================
# davlatlar = {'USA':{'president':'Jo Biden',
#                    'area': 560000,
#                    'currency':'dollar',
#                    'independence':'June',
#                    'capital':'Washington'
#                    },
#             'Uzbekistan': {'president':'Shavkat Mirziyoyev',
#                                'area': 3000,
#                                'currency':'sum',
#                                'independence':'September',
#                                'capital':'Tashkent'
#                                },
#             'kazakhstan': {'president':'Jamar Toqayev',
#                                'area': 25000,
#                                'currency':'tenge',
#                                'independence':'November',
#                                'capital':'Bishkek'
#                                },
#             'Poland':{'president':'Dudek',
#                                'area': 12000,
#                                'currency':'zlot',
#                                'independence':'February',
#                                'capital':'Warsaw'
#                                }
#             }
# for davlat,info in davlatlar.items():
#     if davlat.lower() == 'usa':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#         
#     print(f"\n{davlat}ning poytaxti {info['capital'].title()}.\n"
#           f"The area of {davlat} is {info['area']} sq/km\n"
#           f"National Currency is {info['currency']}\n"
#           f"The Independence Day of {davlat} is on {info['independence']}\n"
#           f"The Capital of {davlat} is {info['capital']}")
# =============================================================================

#                                  PRACTISE 5

davlatlar = {'USA':{'president':'Jo Biden',
                   'area': 560000,
                   'currency':'dollar',
                   'independence':'June',
                   'capital':'Washington'
                   },
            'Uzbekistan': {'president':'Shavkat Mirziyoyev',
                               'area': 3000,
                               'currency':'sum',
                               'independence':'September',
                               'capital':'Tashkent'
                               },
            'kazakhstan': {'president':'Jamar Toqayev',
                               'area': 25000,
                               'currency':'tenge',
                               'independence':'November',
                               'capital':'Bishkek'
                               },
            'Poland':{'president':'Dudek',
                               'area': 12000,
                               'currency':'zlot',
                               'independence':'February',
                               'capital':'Warsaw'
                               }
            }
davlat = input("Istalgan davlat nomini kiriting: ")
#davlat = davlatlar.get(kiriting, "Bizda bunday davlat mavjud emas")
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['capital'].title()}"
          f"\nHududi: {info['area']} kv.km"
          f"\nMustaqillik kuni: {info['independence']}"
          f"\nPul birligi: {info['currency']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")









































    