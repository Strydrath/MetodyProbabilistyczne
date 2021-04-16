
def permutacje(tab, indeks=0):
    if indeks == len(tab):
        print(tab)
    else:
        for i in range(indeks, len(tab)):
            tab[indeks], tab[i] = tab[i], tab[indeks]
            permutacje(tab, indeks+1)
            tab[indeks], tab[i] = tab[i], tab[indeks]


def drukuj_warP(m,n):
    tab =[1]*m
    wariacjeP(m,n,tab,0)

licz=0

def wariacjeP(m,n, tab,i):
    global licz
    if(i==m):
        print(tab)
        licz+=1
    else:
        for j in range(n):
            wariacjeP(m,n,tab,i+1)
            tab[i]+=1
        for j in range(i,m):
            tab[j]=1


drukuj_warP(10,2)
print(licz)

def drukuj_warB(m,n):
    tab = list(range(1,n+1))
    wariacjeB(tab,m,m)


def wariacjeB(tab,m,ind):
    if ind<=0:
        return [[]]
    l=[]
    for i in range(0,len(tab)):
        x=tab[i]
        remLst=tab[:i] + tab[i+1:]
        for p in wariacjeB(remLst,m,ind-1):
            a=[x]+p
            if(len(a)==m):
                print(a)
            l.append(a)
    return l


# drukuj_warB(3,4)
