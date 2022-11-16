# -*- coding: utf-8 -*-
from pvzplus import *
from time import *
import functools
PaoList=[(1, 5), (1, 7), (2, 5), (2, 7), \
         (3, 1), (3, 3), (3, 5), (3, 7), \
         (4, 1), (4, 3), (4, 5), (4, 7), \
         (5, 5), (5, 7), (6, 5), (6, 7)]
CardList=['imIceShroom','IceShroom','CoffeeBean','Squash','WallNut',\
          'CherryBomb','FlowerPot','ScaredyShroom','SunShrooom','PuffShroom']
IceList=[(5,1),(2,1),(1,1),(6,1),(5,1),(2,1),(6,2),(1,2),(1,1),(6,1)]
shortwave=[('P',278,(2,9)),('P',278,(5,9)),\
           ('P',358,(2,9)),('P',358,(5,9)),('I',650)]
longwave=[('P',278,(2,8.5)),('P',278,(5,8.5)),\
          ('P',1000,(2,9)),('P',1000,(5,9))]
ch6=[shortwave,longwave]
wave9=[shortwave+[('P',878,(2,9)),('P',878,(5,9)),\
                  ('P',1600,(2,9)),('P',1600,(5,9))]]
wave10=[[('P',318,(2,9)),('P',318,(5,9)),\
         ('P',358,(2,9)),('P',358,(5,9)),('I',650)]]
wave19=[longwave+[('P',1478,(2,9)),('P',1478,(5,9)),\
                  ('P',1558,(2,9)),('P',1558,(5,9)),\
                  ('P',2078,(2,9)),('P',2078,(5,9))]]
wave20=[[('P',223,(4,7)),\
         ('P',318,(2,9)),('P',318,(5,9)),\
         ('P',418,(2,9)),('P',418,(5,9)),\
         ('P',418,(2,9)),('P',418,(5,9)),\
         ('P',518,(2,9)),('A','CherryBomb',518,(5,9)),\
         ('A','IceShroom',1000,(5,1)),('A','IceShroom',1000,(2,1))]]
eachwave=ch6*4+wave9+wave10+[longwave]+ch6*3+[shortwave]+wave19+wave20
sleep(4)
game=Game(PaoList,CardList,IceList,2,[],-1,[],[],eachwave,0,19)
sleep(1)
game.Start()
