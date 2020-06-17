fila=3
columna=3
m=[]
for i in range(fila):
    m.append([])
    for j in range(columna):
        m[i].append('0')

m[0][1]=5
print('   |     |   ')
print(m[0][0],' | ',m[0][1],' | ',m[0][2])
print('___|_____|___')
print('   |     |   ')
print(m[1][0],' | ',m[1][1],' | ',m[1][2])
print('___|_____|___')
print('   |     |   ')
print(m[2][0],' | ',m[2][1],' | ',m[2][2])
print('   |     |   ')
