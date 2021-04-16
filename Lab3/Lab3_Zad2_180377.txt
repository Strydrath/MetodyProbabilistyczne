import random
przedzialy = [0]*5
F = [0, 0.2, 0.6, 0.8, 0.95, 1]
def generator():
    global przedzialy
    for i in range(100000):
        y = random.random()
        for j in range(6):
            if y <= F[j]:
                x = j
                przedzialy[x-1] += 1
                break

generator()
for a in przedzialy:
    print(a)