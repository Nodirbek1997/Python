# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:29:37 2023

@author: User
"""

#             FUNKSIYADAN QIYMAT QAYTARISH
# =============================================================================
# def toliq_ism_yasa(ism,familiya,otasining_ismi = ''):
#     if otasining_ismi:
#         toliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('Nodirjon','Yusupov','Rahimjonovich')
# talaba2 = toliq_ism_yasa('Hoshim', 'Karimov')
# 
# print(f"{talaba1} darslarda faol qatnashadi, ammo {talaba2} darslarni kop qoldiradi va uyga topshiriqlarni bajarmaydi")
# 
# print(talaba1)
# =============================================================================
# =============================================================================
# def avto_info(company,model,colour,korobka,year,narh=None):
#     avto = {'company':company,
#             'model':model,
#             'colour':colour,
#             'korobka':korobka,
#             'year':year,
#             'narh':narh
#             }
#     return avto
# avto1 = avto_info('BMW', 'X5', 'Black', 'avtomat', 2023, 45000)
# avto2 = avto_info('Mercedes', 'Mybach', 'white', 'mexanika', 2022)
# avtolar = [avto1,avto2]
# print("Online bozordagi mashinalar: ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Nomalum"
#     print(f"{avto['colour']} {avto['company']} {avto['model']}. The Price: {narh}")
# =============================================================================

# =============================================================================
# def toliq_ism_yasa(ism,familiya, otasining_ismi = ''):
#     """
#     
# 
#     Parameters
#     ----------
#     ism : ism kiriting
#     familiya :familiya kiriting
#     """
#     if otasining_ismi:
#         toliq_ism = f"{ism.title()} {familiya.title()} {otasining_ismi.title()}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hoshim','karimov','odilovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# =============================================================================
# =============================================================================
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
# =============================================================================
# =============================================================================
# def oraliq(min,max,qadam=None):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         if qadam:
#             min+=qadam
#         else:
#             min+=1
#     return sonlar
# print(oraliq(0,10))
# =============================================================================
def avto_info(company,model,colour,korobka,year,narh=None):
    avto = {'company':company,
            'model':model,
            'colour':colour,
            'korobka':korobka,
            'year':year,
            'narh':narh
            }
    return avto
print("Saytimizdagi avtomobillarni royhatini shakillantiramiz:")
avtolar = []
while True:
    print("\nQuyidagi malumotlarni kiriting:")
    company = input("Kompaniya nomini kiriting: ")
    model = input("Modeli: ")
    colour = input("Rangi: ")
    korobka = input("Karobka turi: ")
    year = input("Ishlab chiqarilgan sana: ")
    narh = input("Narhi: ")
    avtolar.append(avto_info(company, model, colour, korobka, year,narh))
    javob = input("Yana avto qoshishni hohlaysizmi? (yes/no): ")
    if javob == "no":
        break
print("\n Salonimizdagi avtolar royhati: ")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = 'Nomalum'
    print(f"{avto['colour'].title()}, {avto['model'].title()}, {korobka} karobka. Narhi: {narh} ")
        
    














































