# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:48:55 2023

@author: User
"""
# =============================================================================
# names = ['Ali','Vali','Hoshim','Kozim','Olim']
# for n in names:
#     print(f"{n} sizni Germaniyaga ishga taklif qilamiz! \n")
#     print(f"kod {len(names)} marta takrorlandi")
#     
# =============================================================================
# =============================================================================
# toq_sonlar = list(range(11,100,2))
# for n in toq_sonlar:
#     print(f"sonning kubi {n**3} ga teng")
#     
# =============================================================================
# =============================================================================
# kinolar = []
# print("5 ta sevimli kinolaringiz qaysilar:")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-kino:"))
#     print(kinolar)
# =============================================================================
n_people = int(input("Bugun nechta odam bn suhbatlashding? "))
names = []
for n in range(n_people):
    names.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi? "))
    print(names)