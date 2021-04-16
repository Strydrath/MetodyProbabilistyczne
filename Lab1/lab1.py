licz = 0
def drukuj_permutacje(n):
    tab = list(range(1,n+1))
    permutacje(tab,0)


def permutacje(tab, indeks=0):
    if indeks == len(tab):
        print(tab)
        global licz
        licz+=1
    else:
        for i in range(indeks, len(tab)):
            tab[indeks], tab[i] = tab[i], tab[indeks]
            permutacje(tab, indeks+1)
            tab[indeks], tab[i] = tab[i], tab[indeks]

drukuj_permutacje(5)
print(licz)
