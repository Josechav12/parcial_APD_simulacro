# Realiza una función llamada area_rectangulo() que devuelva 
# el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
# Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

base = 15
altura = 10
def area_rectangulo(base, altura):
    return base * altura

area = area_rectangulo(base,altura)

print(f"el área del rectángulo con base{base} y altura {altura} es: {area}")