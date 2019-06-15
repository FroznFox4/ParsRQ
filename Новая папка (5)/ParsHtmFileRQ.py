from collections import Iterable
from os import remove

func = lambda el1: '%s : %s : %s' % (el1.tupe, el1.name, el1.damage)
ll=['нанесли','восстановили','наносит','промахивается']
g={
        ll[0]:{},
        ll[1]:{},
        ll[2]:{},
        ll[3]:{}
}

class hel():
    def __init__(self,name,damage,tupe):
        self.name = str(name)
        self.damage = int(damage)
        self.tupe = str(tupe)

def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

def addmob(name,uron,tupe):
    if g[tupe].get(name,True)==True: 
        mob = hel(name,uron,tupe)
        g[tupe].setdefault(mob.name,mob)
    else:
        (g[tupe][name]).damage+=int(uron)

def rid(NFile):
    f = open(str(NFile),encoding='utf-8')
    l=[line.split() for line in f]
    f.close
    return(l)

def one(NFile):
    try:
        l=rid(NFile)
    except:
        exit('File is epsent')

    for i in range(4):
        l.pop(0)
    for i in range(3):
        l.pop(-1)
    
    h = [] #nanesenniy uron
    c = [] #poluch uron
    m = [] #kol missov po vam
    j = [] #kol heal
    p = []

    for i in range(len(l)):

        if bool(l[i].count(ll[0])):
            o=l[i].index(ll[0])
            h.append([l[i][10],l[i][7]])
        elif bool(l[i].count(ll[1])):
            o=l[i].index(ll[1])
            j.append([l[i][5][10:],l[i][7]])
        elif bool(l[i].count(ll[2])):
            o=l[i].index(ll[2])
            c.append([l[i][5][10:],l[i][o+2]])
        elif bool(l[i].count(ll[3])):
            o=l[i].index(ll[3])
            m.append([l[i][5][10:],1])
     
    print() 
    
    for i in range(len(h)):
        addmob(h[i][0],h[i][1],ll[0])
    for i in range(len(m)):
        addmob(m[i][0],m[i][1],ll[3])
    for i in range(len(j)):
        addmob(j[i][0],j[i][1],ll[1])
    for i in range(len(c)):
        addmob(c[i][0],c[i][1],ll[2])
 
    k=list(flatten([list(g[ll[i]].values()) for i in range(4)]))    
    
    
    k=(list(map(func,k)))
    return(k)