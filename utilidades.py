def tiene_mayusculas_y_minusculas(cadena):
    return any(c.islower() for c in cadena) and any(c.isupper() for c in cadena)
