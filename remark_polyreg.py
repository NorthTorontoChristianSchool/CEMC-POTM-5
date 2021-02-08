import numpy

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [4, 14, 52, 194, 724, 2702, 10084, 37634, 140452]

for i in range(1, 11):
    print(numpy.polyfit(x, y, i))