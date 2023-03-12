
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def busqueda_dicotomica_recursiva(t, inicio, fin, c):
    if inicio > fin: 
        return "AUSENTE"
    
    medio = (inicio + fin) // 2
    
    if t[medio] == c: 
        return medio
    
    elif t[medio] < c:  
        return busqueda_dicotomica_recursiva(t, medio+1, fin, c)
    
    else:  
        return busqueda_dicotomica_recursiva(t, inicio, medio-1, c)



print(busqueda_dicotomica_recursiva(t, 0, len(t)-1, 17))
