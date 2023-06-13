# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:19:00 2023

@author: User
"""

#talaba_0 = {'ism':'Nodirbek','yosh':26,'t_yil':1997}
#talaba_0['yosh'] = 27
#print(f"Talaba {talaba_0['ism'].upper()} {talaba_0['yosh']} yoshda")
# =============================================================================
# telefonlar = {'ali':'Iphone X',
#               'vali':'Nokia 1202',
#               'karim':'galaxy A40',
#               'Nodir':'Iphone 15 pro max',
#               'Doni':'RealMI 15'
#               }
# print(telefonlar['ali'])
# phone = telefonlar.get('Doni','Bunday qiymat mavjud emas')
# print(phone)
# =============================================================================
# =============================================================================
# otam = {'yosh':52,'ism':'Rahimjon','kasb':'doctor'}
# onam = {'yosh':50,'ism':'Mafisa','kasb':'uy bekasi'}
# singlim = {'yosh':24,'ism':'Maftuna','kasb':'student'}
# print(f"Otamning ismi {otam['ism']}, U {otam['yosh']} yoshda.Uning kasbi {otam['kasb']}")
# =============================================================================
# =============================================================================
# meals = {'Yusufjon':'shirguruch','Fotima':'sho\'rva','Rahimjon':'qotirma','Nafisa':'osh','Maftuna':'shashlik'}
# print(f"Yusufjon otamning sevimli taomi {meals['Yusufjon']}")
# print(f"Dadamning sevimli taomi {meals['Rahimjon']}")
# print(f"Oyimnning sevimli taomi {meals['Nafisa']}")
# =============================================================================
python_dic = {'integer':'butun qiymat qabul qiluvchi funksiya',
              'float':'o\'nlik qiymat qabul qiluvchi funksiya',
              'append':'qo\'shadigan metod',
              'print':'Qiymatni chiqaruvchi operator',
              'lower':'matnni uppercase ga o\'zgartiradigan metod',
              'get':'qiymnatni dictionary dan ajratib oladi',
              'remove':'qoymatni o\'chiradi',
              'if':'shart operatori',
              'for':'sikl operatori',
              'tuple':'o\'zgarmas ro\'yxat'
              }
#print(python_dic['tuple'])
word = input("Istalgan Python atamasini kriting: ").lower()
#print(python_dic.get(word,'Bunday atma bizning lug\'atda hali mavjud emas'))
if word in python_dic:
    print(python_dic[f"{word}"])
else:
    print(f"Lugatga {word} atamasi hali kiritilmagan")
