

val_inicial_x = 0
val_inicial_y = 0
val_inicial_z = 0


x = [8, 4, -2, 24]
y = [3, 6, -1, 13]
z = [2, -2, 6, 16]


raiz_actual = (x[3]-(x[1]*val_inicial_y)*(-x[2]*val_inicial_z))/x[0]
raiz_anterior = 0


error = abs((raiz_actual - raiz_anterior)/raiz_actual)*100

print(raiz_actual)
print(error)

for i in range(3):
    raiz_actual = (x[3]-(x[1]*val_inicial_y)*(-x[2]*val_inicial_z))/x[0]
    print(raiz_actual)
