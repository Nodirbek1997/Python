# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:49:48 2023

@author: User
"""
# =============================================================================
# 
# countries = ['USA','Germany','Canada','UK','Switzerland','Australia']
# print(countries )
# print(len(countries))
# print(sorted(countries))
# print(sorted(countries,reverse=True))
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)
# =============================================================================
# =============================================================================
# juft_sonlar = list(range(120,1200))
# print(sum(juft_sonlar))
# print(max(juft_sonlar) - min(juft_sonlar))
# print(max(juft_sonlar))
# print(min(juft_sonlar))
# print(len(juft_sonlar))
# print(juft_sonlar[:20])
# print(juft_sonlar[-20:])
# print(juft_sonlar[530:550])
# =============================================================================
taomlar = ['shashlik','somsa','kasha','mastava','qozon kabob']
nonushta = taomlar[:]
nonushta.remove('shashlik')
nonushta.remove('qozon kabob')
nonushta.append('grechka')
nonushta.append('soup')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'
print(nonushta)