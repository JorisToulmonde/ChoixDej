
# @Author : Mohammed Amine HAJIR 
# @Date   : Octobre 2016
# @title  : Test Projet 
# @file   : 


#!/usr/bin/python3.5
# -*-coding:utf-8 -*

from random import uniform
from random import randint
import random
import math
import numpy as np
import statistics as stat

NB_MEMBRE = 7
NB_RESTO = 5

def avg(liste):
    return sum(liste)/len(liste)
    

class Restaurant:
    
   def __init__(self,a,n,f,nom,new): # définition du constructeur 
        self.Anc = a
        self.Note = n
        self.Freq = f
        self.name = nom
        self.new = False

NameList = ["RU", "SUBWAY", "GREC", "MACDONALD'S", "KFC", "QUICK", "SPEED BURGER", "GLOBE", "DOMINO'S"]        
RestoList = []

i = 0


while i < NB_RESTO:
    noteMembres = []
    j = 0
    
    while j < NB_MEMBRE:
        noteMembres.append(uniform(0,5))
        j+=1
        
    a = randint(0,100)
    f = randint(0,100)
    
    RestoList.append( Restaurant( a, 3*avg(noteMembres) + a - f, f , NameList[randint(0,len(NameList)-1)], random.choice([True, False]) ) )
    i+=1

maxi = RestoList[0].Note
R = RestoList[0].name
for elt in RestoList:
    if elt.Note > maxi:
        R = elt.name
        
print (R)
