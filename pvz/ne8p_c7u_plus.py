# -*- coding: utf-8 -*-
from pvzplus import *
from time import *
import functools
PaoList=[(1,1),(1,5),(3,1),(3,5),(5,1),(5,5),(2,5),(4,5)]
CardList=['imIceShroom','IceShroom','DoomShroom','CherryBomb','Squash',\
          'GraveBuster','Blover','ScaredyShroom','SunShrooom','PuffShroom']
IceList=[(3,7)]

def IceTwice(game,effecttime):
    game.CardList['imIceShroom'].UsePlantByEffectTime(effecttime,(3,7))
    game.CardList['imIceShroom'].UsePlantByEffectTime(effecttime,(3,8))

def Mubei(game,operatetime):
    for r in range(1,6):
        for c in range(7,10):
            game.CardList['GraveBuster'].UsePlantByOperateTime(operatetime,(r,c))

c7u=[[('P',278,(2,9)),('P',278,(4,9))],\
     [('A','ScaredyShroom',150,(2,9)),\
      ('A','SunShrooom',150,(3,9)),\
      ('A','PuffShroom',150,(4,9)),\
      ('A','Shovel',250,(2,9)),\
      ('A','Shovel',250,(3,9)),\
      ('A','Shovel',250,(4,9)),\
      ('P',700,(2,8.5)),('P',700,(4,8.5)),('I',1550)],\
     [('P',278,(2,9)),('P',278,(4,9))],\
     [('P',1300,(2,8.6)),('P',1300,(4,8.6)),('I',1550)],\
     [('P',278,(2,8)),('P',278,(4,8)),\
      ('P',1800,(2,8.4)),('P',1800,(4,8.4))]]
     
wave10=[[('P',318,(2,9)),('P',318,(4,9)),('A','CherryBomb',318,(2,9)),\
         ('A','Blover',400,(1,7)),('I',650)]]
wave20=[[('P',318,(2,9)),('P',318,(4,9)),\
         ('I2',500),('M',510)]]
eachwave=[[]]+(c7u*2)[:9]+wave10+(c7u*3)[3:12]+wave20

sleep(4)
game=Game(PaoList,CardList,IceList,-1,[],-1,[],[],eachwave,4)
game.operates['I2']=functools.partial(IceTwice,game)
game.operates['M']=functools.partial(Mubei,game)
sleep(1)
StartAutoCollectThread()
game.Start()
