# -*- coding: utf8 -*-
## @file
## @brief fuzzy sets and inheritance<br>нечеткие множества и вывод

from Qbject import *

# библиотека вывода графиков
from matplotlib import pylab as plt
from matplotlib import colors

## @defgroup fuzzy Fuzzy
## @brief fuzzy sets and inheritance<br>нечеткие множества и вывод
## @see @ref fuzzypage page
## @see https://www.calvin.edu/~pribeiro/othrlnks/Fuzzy/fuzzysets.htm
## @see short intro course in Russian (c) Artem Denisov:
## - 0. Введение в теорию нечетких множеств:
##   http://www.youtube.com/watch?v=I1wiWAyeA4Y 
## - 1. Понятие нечеткого множества:
##   http://www.youtube.com/watch?v=6R4jKWgdXQA
## @{

## fuzzy set<br>
## нечеткое множество
class Set(Qbject):
    ## создание нечеткого множества
    ## @param[in] V имя множества
    def __init__(self,V):
        Qbject.__init__(self,V)
        ## хранилище для характеристической функции, заданной таблично
        self.attr['Mu'] = {}
    ## dump object in short form (header only)
    def head(self,prefix=''):
        return '%s<fuzzy/%s:%s>' % (prefix,self.type, self.value)

## fuzzy set member<br>
## элемент нечеткого множества
class Member: pass

## trapezoidal fuzzy set<br>
## трапецеидальное нечеткое множество 
class Trapezoid(Set):
    ## создание нечеткого множества
    ## @param[in] V имя множества
    ## @param[in] U универсальное множество
    ## @param[in] min_U минимум по оси U
    ## @param[in] max_U максимум по оси U
    ## @param[in] min_plato левая ордината плато
    ## @param[in] max_plato правая ордината плато
    ## @param[in] h выcота характеристической функции (максимальная оценка)
    def __init__(self, V, U, min_U, min_plato, max_plato, max_U, h=1):
        Set.__init__(self,V)
        ## преобразование параметров
        if min_U == None: min_U = min(U)   #  начало трапеции от левого края
        if max_U == None: max_U = max(U)   # кончало трапеции от правого края
        ## проверка параметров
        if min_plato>max_plato: raise AttributeError((min_plato,max_plato))
        if min_U>min_plato:     raise AttributeError((min_U,min_plato))
        if max_U<max_plato:     raise AttributeError((max_plato,max_U))
        ## запись параметров множества в атрибуты Qбъекта
        self.attr['min_U'] = min_U ; self.attr['max_U'] = max_U
        self.attr['min_plato'] = min_plato ; self.attr['max_plato'] = max_plato
        self.attr['h'] = h
        ## генерация табличной функции
        mu = self.attr['Mu']
        # слева от трапеции
        if min_U > min(U):
            for el in filter(lambda a:a<=min_U,U): # U[U <= min_U]
                mu[el] = h if form == '<' else 0
        # справа от трапеции
        if max_U < max(U):
            for el in filter(lambda a:a>=max_U,U): # U[U >= max_U]
                mu[el] = h if form == '>' else 0
        # плато
        for el in filter(lambda a:a>=min_plato and a<=max_plato, U):
                mu[el] = h if form == '=' else 0
            

print Trapezoid('lesson1', range(17), 2, 3, 9, None)

## @}
