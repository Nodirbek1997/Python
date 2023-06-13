# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:22:57 2023

@author: User
"""
# =============================================================================
# #1
# countries = ['USA','Japan','Germany','UK','Australia','New Zealand']
# print(countries)
# #2
# print(len(countries))
# #3
# print(sorted(countries))
# #4
# print(sorted(countries,reverse=True))
# #5
# print(countries)
# #6
# countries.reverse()
# print(countries)
# #7
# countries.sort()
# print(countries)
# #8
# countries.sort(reverse=True)
# print(countries)
# =============================================================================
# =============================================================================
# #9
# #sonlar = list(range(120,1200,2))
# #print(sonlar)
# #10
# sonlar = list(range(120,1200))
# #print(sum(sonlar))
# #print(max(sonlar) - min(sonlar))
# #11
# #print(max(sonlar) - min(sonlar))
# #12
# #print(len(sonlar))
# #13
# print(sonlar[0:20])
# print(sonlar[530:550])
# print(sonlar[-20:])
# =============================================================================
#14
taomlar = ['osh', 'somsa','manti','mastava','qotirma']
print(taomlar)
nonushta = taomlar[:]
print(nonushta)
nonushta.remove('qotirma')
nonushta.remove('osh')
nonushta.append('saryog')
nonushta.append('moloko')
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = 'manpar'
print(nonushta)