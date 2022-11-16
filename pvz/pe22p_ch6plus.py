# -*- coding: utf-8 -*-
from pvzplus import *
from time import *
import functools
PaoList=[(1, 1), (1, 3), (1, 5), (1, 7), \
         (2, 1), (2, 3), (3, 1), (2, 7), \
         (2, 5), (3, 3), (3, 5), \
         (4, 1), (4, 3), (4, 5), \
         (5, 3), (5, 1), (5, 5), (6, 1), \
         (5, 7), (6, 3), (6, 5), (6, 7)]
'''
effect: ['P', 238, (1, 9)]1
effect: ['P', 238, (5, 9)]4
effect: ['P', 278, (2, 9)]2
effect: ['P', 348, (5, 7.8)]5#需要调整炮位
effect: ['P', 388, (1, 8.8)]3
effect: ['P', 278, (2, 8.5)]6
effect: ['P', 553, (5, 7.2)]7#需要调整炮位
effect: ['P', 1000, (2, 8.6)]8
effect: ['P', 1000, (5, 8.6)]10
effect: ['P', 1220, (1, 8.4)]9
effect: ['P', 1220, (5, 8.4)]11
'''
CardList=['CoffeeBean','IceShroom','imIceShroom','CherryBomb','Squash',\
          'Pumpkin','FlowerPot','ScaredyShroom','SunShrooom','PuffShroom']
IceList=[(4,8),(3,8),(4,7),(3,7)]

def PSD(halfscene=['up','down'],hugewave=False):
    l=[]
    if 'up' in halfscene:
        if hugewave:
            l.append(('P',318,(1,9)))
            l.append(('P',318,(2,9)))
            l.append(('P',428,(1,8.8)))
        else:
            l.append(('P',238,(1,9)))
            l.append(('P',278,(2,9)))
            l.append(('P',388,(1,8.8)))
    if 'down' in halfscene:
        if hugewave:
            l.append(('P',318,(5,9)))
            l.append(('P',318,(5,9)))
            l.append(('P',428,(5,8.8)))
        else:
            l.append(('P',238,(5,9)))
            l.append(('P',278,(5,9)))
            l.append(('P',388,(5,8.8)))
    return l

def PD(halfscene=['up','down'],waveduration=600,ice=False,hugewave=False):
    l=[]
    if waveduration==600:
        col=9
        effecttime=238
        if hugewave:
            effecttime+=40
    else:
        col=8.6
        effecttime=waveduration-200
    if ice:
        delay=220
        left=0.2
    else:
        delay=110
        left=1.2
    if 'up' in halfscene:
        l.append(('P',effecttime,(2,col)))
        l.append(('P',effecttime+delay,(1,col-left)))
    if 'down' in halfscene:
        l.append(('P',effecttime,(5,col)))
        l.append(('P',effecttime+delay,(5,col-left)))
    return l

def CI(halfscene=['up','down'],waveduration=600):
    icetime=waveduration+50
    dctime=icetime-10-180
    l=[('I',icetime)]
    if 'up' in halfscene:
        l.append(('A','FlowerPot',dctime,(1,9)))
        l.append(('A','ScaredyShroom',dctime,(2,9)))
        l.append(('A','Shovel',dctime+20,(1,9)))
        l.append(('A','Shovel',dctime+20,(2,9)))
    if 'down' in halfscene:
        l.append(('A','SunShrooom',dctime,(5,9)))
        l.append(('A','PuffShroom',dctime,(6,9)))
        l.append(('A','Shovel',dctime+20,(5,9)))
        l.append(('A','Shovel',dctime+20,(6,9)))
    return l

def SeparateP(halfscene=['up','down'],time='early',hugewave=False):
    l=[]
    if time=='early':
        col=8.5
        effecttime=278
        if hugewave:
            effecttime+=40
    elif time=='late':
        col=7.2
        effecttime=553
    if 'up' in halfscene:
        l.append(('P',effecttime,(2,col)))
    if 'down' in halfscene:
        l.append(('P',effecttime,(5,col)))
    return l
    
shortwave=PSD(['up'])+PD(['down'])+CI(['down'])

longwave=SeparateP(['up'],'early')+SeparateP(['down'],'late')\
          +PD(['up','down'],1200,True)

ch6=[shortwave,longwave]

wave9=[shortwave+[('P',1153,(5,7.2))]+PD(['down'],1600,True)+\
       [('P',2038,(2,9)),('P',2038,(5,9))]]

wave10=[PSD(['up'],True)+PD(['down'],hugewave=True)+CI(['down'])]

wave19=[longwave+[('P',1438,(1,9)),('P',1438,(5,9)),\
                  ('P',2238,(2,9)),('P',2238,(5,9))]]
wave20=[[('P',223,(4,7)),('P',223,(4,8)),\
         ('P',318,(2,9)),('P',318,(5,9)),\
         ('P',318,(2,9)),('P',318,(5,9)),\
         ('P',408,(2,9)),('P',408,(5,9)),\
         ('P',408,(2,9)),('P',408,(5,9))]]
eachwave=ch6*4+wave9+wave10+[longwave]+ch6*3+[shortwave]+wave19+wave20
sleep(4)
game=Game(PaoList,CardList,IceList,2,[],-1,[],[],eachwave,1)
sleep(1)
game.Start()
"""
wave: 1
effect: ['P', 238, (1, 9)]
effect: ['P', 278, (2, 9)]
effect: ['P', 388, (1, 8.8)]
effect: ['P', 238, (5, 9)]
effect: ['P', 348, (5, 7.8)]
effect: ['I', 650]
effect: ['A', 'SunShrooom', 465, (5, 9)]
effect: ['A', 'PuffShroom', 465, (6, 9)]
effect: ['A', 'Shovel', 485, (5, 9)]
effect: ['A', 'Shovel', 485, (6, 9)]
wave: 2
effect: ['P', 278, (2, 8.5)]
effect: ['P', 553, (5, 7.2)]
effect: ['P', 1000, (2, 8.6)]
effect: ['P', 1220, (1, 8.4)]
effect: ['P', 1000, (5, 8.6)]
effect: ['P', 1220, (5, 8.4)]
"""
