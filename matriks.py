import math
import numpy as np
#Kartesius
cartesius_point = {
    "p1":[1,1],
    "p2":[1,2],
    "p3":[2,2],
    "p4":[3,1]
}

def distance(p, _p):
    return int(math.sqrt((p[0]-_p[0])**2 + ((p[1]-_p[1])**2)))

new_point = []
result = []
for i in range(1, len(cartesius_point)+1):
    temp = []
    for j in range(1, len(cartesius_point)+1):
        temp.append(distance(cartesius_point['p'+str(i)], cartesius_point['p'+str(j)]))
        new_point.append((cartesius_point['p'+str(i)], cartesius_point['p'+str(j)]))
    result.append(temp)

hasil = np.array(result)
print(hasil)