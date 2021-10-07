# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def xy_line(x1, y1, x2, y2): #расстояние между точками на плоскости
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist

def distance(x1, y1, x2, y2, x3, y3): #минимальная длина для 3 координат
    distAB=xy_line(x1,y1,x2,y2)
    distBC=xy_line(x2,y2,x3,y3)
    distAC=xy_line(x1,y1,x3,y3)
    min_dist=min(distAB,distBC,distAC)
    if min_dist==distAB:
       res="AB"
    elif min_dist==distBC:
        res="BC"
    else:
        res="AC"
    return res

print("Самый короткий отрезок: ", distance(1,1,2,1,3,3))
