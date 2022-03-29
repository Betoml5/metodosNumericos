# Gauss Seidel Iteration

# 20x + y - 2z = 17
# 3x + 20y -z = -18
# 2x - 3y + 20z = 25


# Formula
# x = (17-y+2z)/20
# y = (-18-3x+z)/20
# z = (25-2x+3y)/20

# Defining equations to be solved
# in diagonally dominant form
def f1(x, y, z): return (17-y+2*z)/20
def f2(x, y, z): return (-18-3*x+z)/20
def f3(x, y, z): return (25-2*x+3*y)/20


# Initial setup
x0 = 0
y0 = 0
z0 = 0
count = 1

# Reading tolerable error
e = float(input('Enter tolerable error: '))

# Implementation of Gauss Seidel Iteration
print('\nCount\tx\ty\tz\n')

condition = True

while condition:
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1))
    e1 = abs(x0-x1)
    e2 = abs(y0-y1)
    e3 = abs(z0-z1)

    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e and e2 > e and e3 > e

print('\nSolution: x=%0.3f, y=%0.3f and z = %0.3f\n' % (x1, y1, z1))
