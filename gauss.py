# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

def seidel(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if(j != i):
                d -= a[j][i] * x[i]
        # updating the value of our solution
        x[j] = d / a[j][j]
    # returning our updated solution
    return x


# int(input())input as number of variable to be solved
n = 3
a = []
b = []

dummy_array_1 = []
dummy_array_2 = []
dummy_array_3 = []


# Valores iniciales
x = []
# Valores del final de la matriz
b = []
for i in range(3):
    number = int(input("Ingresa el numero:  " + str(i+1)))
    dummy_array_1.append(number)
for i in range(3):
    number = int(input("Ingresa el numero " + str(i+1)))
    dummy_array_2.append(number)
for i in range(3):
    number = int(input("Ingresa el numero " + str(i+1)))
    dummy_array_3.append(number)

# Los valores del final de la matriz
for i in range(3):
    number = int(input("Ingresa el numero " + str(i+1)))
    b.append(number)


# Valores iniciales
print("Ingresa los valores iniciales")
for i in range(3):
    number = int(input("Ingresa el numero " + str(i+1)))
    x.append(number)


a.append(dummy_array_1)
a.append(dummy_array_2)
a.append(dummy_array_3)


# initial solution depending on n(here n=3)
# x = [0, 0, 0]
# a = [[8, 4, -2], [3, 6, -1], [2, -2, 6]]
# b = [24, 13, 16]
print(x)

# loop run for m times depending on m the error value
# for i in range(0, 25):
#     x = seidel(a, x, b)
#     # print each time the updated solution
#     print(x)
