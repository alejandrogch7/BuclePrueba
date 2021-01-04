numeros = list(range(10000))
print(numeros)


# Revelar las posiciones donde se repiten caracteres en un array

u = [1, 2, 3, 4, 5, 4, 7, 2, 3]
m = [i for i, x in enumerate(u) if u.count(x)>1] 
print(m) 



