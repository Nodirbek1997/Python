# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:36:16 2023

@author: User
"""

# =============================================================================
# def t_yil(ism,yosh,joriy_yil=2023):
#     """
#     
# 
#     Parameters
#     ----------
#     ism :Bu yerga foydalanuvchining ismini kiriting
#     yosh : yoshni kiriting
# 
#     Returns
#     -------
#     None.
# 
#     """
#     print(f"{ism.title()} {joriy_yil - yosh}-yilda tug'ilgan")
# t_yil('Nodir',26)
# =============================================================================
# =============================================================================
# def hisobla(son):
#     print(f"{son} ning kvadrati >>> {son**2}\n"
#           f"{son} ning kubi >>> {son**3}")
# hisobla(2)
# =============================================================================
# =============================================================================
# def juft_toq(son):
#     if son % 2:
#         print(f"{son} >>> Toq son")
#     else:
#         print(f"{son} >>> Juft son")
#         
# juft_toq(1564654654849654654654864656546546541324165465465465)
# =============================================================================
# =============================================================================
# def taqqosla(son1,son2):
#     if son1 < son2:
#         print(f"{son1} soni {son2} dan kichik")
#     elif son1>son2:
#         print(f"{son1} soni {son2} dan katta")
#     else:
#         print(f"{son1} soni {son2} ga teng")
#         
# taqqosla(165465465465465163456,6879846565465465)
# =============================================================================
def tekshir(son):
    for n in range(2,11):
        if not son % n:
            print(f"{son} {n} ga qooldiqsiz bo'linadi")
tekshir(20)