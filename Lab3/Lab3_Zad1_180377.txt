import random
granice = [60,70,80,90,100,110,120,130,140,150]
przedzialy = [0]*10
def generator():
    global przedzialy
    for i in range(100000):
        y = random.random()
        x = y * 100 + 50
        for j in range(10):
            if x < granice[j]:
                przedzialy[j] += 1
                break

generator()
for a in przedzialy:
    print(a)