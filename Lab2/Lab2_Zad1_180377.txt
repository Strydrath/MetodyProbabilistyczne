przedzialy = [0]*10
def generator():
    global przedzialy
    x0 = 15
    a = 69069
    c = 1
    m = 2**31
    for i in range(100000):
        x = (a*x0 + c) % m
        x0 = x
        j = x*10//m
        przedzialy[j] += 1

generator()
for a in przedzialy:
    print(a)
