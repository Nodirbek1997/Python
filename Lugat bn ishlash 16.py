# -*- coding: utf-8 -*-
"""
Created on Wed May 31 10:19:38 2023

@author: User
"""

#     NESTING

# =============================================================================
# car0 = {'model':'Gentra',
#         'narh':15000,
#         'rang':'black',
#         'km':30000
#         }
# 
# car1 = {'model':'BMW',
#         'narh':30000,
#         'rang':'red',
#         'km':12000
#         }
# 
# car2 = {'model':'Audi',
#         'narh':25000,
#         'rang':'qora',
#         'km':5000
#         }
# =============================================================================

# =============================================================================
# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang'].title()}, "
#       f"{car['km']}, "
#       f"{car['narh']}$.")
# =============================================================================

# =============================================================================
# cars = [car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#       f"color: {car['rang'].title()}, "
#       f"{car['km']} km/h, "
#       f"{car['narh']}$.")
# =============================================================================
# =============================================================================
# gentras = []
# for n in range(10):
#     new_car = {
#         'model':'gentra',
#         'rang':None,
#         'narh':None,
#         'korobka':'avtomat'
#         }
#     gentras.append(new_car)
# # =============================================================================
# #     for gentra in gentras: 
# #         print(gentra)
# # =============================================================================
# for gentra in gentras[:3]:
#     gentra['rang'] = 'Red'
# # =============================================================================
# # for gentra in gentras:
# #     print(gentra)
# # =============================================================================
# for gentra in gentras[3:6]:
#     gentra['rang'] = 'Black'
# 
# for gentra in gentras[6:]:
#     gentra['korobka'] = 'mehanika'
# # =============================================================================
# # for gentra in gentras:
# #     print(gentra)
# # =============================================================================
# for gentra in gentras:
#     if gentra['korobka'] == 'avtomat':
#         gentra['narh'] = 40000
#     else:
#         gentra['narh'] = 35000
# for gentra in gentras:
#     print(gentra)
# =============================================================================
# =============================================================================
# dasturchilar = {
#     'ali':['python','C++'],
#     'vali':['java','cotlin'],
#     'karim':['R','php']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi tillarni biladi: ", end='')
#     for til in tillar:
#         print(f"{til.upper()} ", end='')
# =============================================================================
hamkasblar = {
    "ali": {
        "familiya": "valiyev",
        "tyil": 1995,
        "malumot": "oliy",
        "tillar": ["python", "c++"],
    },
    "vali": {
        "familiya": "aliyev",
        "tyil": 2001,
        "malumot": "o'rta-maxsus",
        "tillar": ["html", "css", "js"],
    },
    "hasan": {
        "familiya": "husanov",
        "tyil": 1999,
        "malumot": "maxsus",
        "tillar": ["python", "php"],
    },
}

for ism,info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}"
          f" Tugulgan yili: {info['tyil']}"
          f" Malumoti: {info['malumot']}"
          f" Quyidagi dasturlash tillarini biladi: {info['tillar']}")
#    for til in info['tillar']:
#        print(til.upper())
        
    

    
 






































