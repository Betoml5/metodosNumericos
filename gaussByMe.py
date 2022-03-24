
from pprint import pprint

val_inicial_x = int(input("Ingresa el valor inicial de x1: "))
val_inicial_y = int(input("Ingresa el valor inicial de x2: "))
val_inicial_z = int(input("Ingresa el valor inicial de x3: "))

# Declaramos la matriz con 3 arreglos
x = []
y = []
z = []

# Pedimos los datos de la matriz

for i in range(4):
    print("Ingresa el valor de x sub " + str(i + 1))
    val = int(input("Ingresar: "))
    x.append(val)

for i in range(4):
    print("Ingresa el valor de y sub " + str(i + 1))
    val = int(input("Ingresar: "))
    y.append(val)

for i in range(4):
    print("Ingresa el valor de z sub " + str(i + 1))
    val = int(input("Ingresar: "))
    z.append(val)


print(x)
print(z)
print(y)

# Calcular Raices


# Raiz de X
for i in range(4):
    raiz_actual = (x[3]-(x[1]*val_inicial_y)*(-x[2]*val_inicial_z))/x[0]


# x = [8, 4, -2, 24]
# y = [3, 6, -1, 13]
# z = [2, -2, 6, 16]


# raiz_actual = (x[3]-(x[1]*val_inicial_y)*(-x[2]*val_inicial_z))/x[0]
# raiz_anterior = 0


# error = abs((raiz_actual - raiz_anterior)/raiz_actual)*100

# print(raiz_actual)
# print(error)


# for i in range(3):
#     raiz_actual = (x[3]-(x[1]*val_inicial_y)*(-x[2]*val_inicial_z))/x[0]
#     print(raiz_actual)
