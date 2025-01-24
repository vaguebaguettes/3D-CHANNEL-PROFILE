import numpy as np
import func
import matplotlib.pyplot as plt

def linemesh(div, y_axis):

    x = np.array([])
    y = np.array([])

    up = 0
    i = 0
    zero = 0

    def first(f):
        b = f + 1
        d = b / 100
        g = d * div
        return g

    def second():
        t = y_axis / 2 
        return t

    def third(w):
        v = w * 0.3
        if zero >= v:
            return True
        else:
            return False

    def fourth(a):
        l = a + zero
        return l

    def fifth(l, target=100):
        if l >= target:
            return 1
        else:
            return 0

    while True:
        q = first(i)
        r = second()
        g = third(r)
        res = func.select(q, div, g)
        
        up = fourth(res)
        down = fifth(up, 100)
        if down == 1:
            break
        last = func.select(up, r, down)
        x = np.append(x, last)
        y = np.append(y, i)

        i += 1
        zero = last

    return x, y

# Example usage:
x, y = linemesh(1, 200)
print(x)
plt.plot(x, y)
plt.show()
