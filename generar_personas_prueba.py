
import os
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from residentes.models import Registro, Persona

nombres = [
    "Juan", "Pedro", "Luis", "Carlos", "José", "Miguel",
    "Andrés", "Felipe", "Diego", "Pablo", "Jorge", "Rodrigo",
    "Francisco", "Sebastián", "Matías", "Cristóbal", "Daniel",
    "Camila", "María", "Carolina", "Daniela", "Paula", "Andrea",
    "Fernanda", "Valentina", "Javiera", "Catalina", "Antonia",
    "Francisca", "Claudia", "Patricia", "Verónica", "Marcela"
]

apellidos = [
    "González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto",
    "Contreras", "Silva", "Martínez", "Sepúlveda", "Morales",
    "Rodríguez", "López", "Fuentes", "Hernández", "Torres",
    "Araya", "Flores", "Espinoza", "Valenzuela", "Castillo",
    "Ramírez", "Reyes", "Gutiérrez", "Castro", "Álvarez"
]


def nombre_aleatorio():
    nombre = random.choice(nombres)
    apellido = (
        random.choice(apellidos) + " " +
        random.choice(apellidos)
    )
    return nombre, apellido


def rut_ficticio():
    numero = random.randint(10_000_000, 25_000_000)
    factores = [2, 3, 4, 5, 6, 7]
    suma = 0

    for i, digito in enumerate(reversed(str(numero))):
        suma += int(digito) * factores[i % 6]

    resto = 11 - (suma % 11)

    if resto == 11:
        dv = "0"
    elif resto == 10:
        dv = "K"
    else:
        dv = str(resto)

    return f"{numero}-{dv}"


creadas = {
    "SOCIO": 0,
    "REPRESENTANTE": 0,
    "ADICIONAL": 0,
}
casas_omitidas = 0

for registro in Registro.objects.all().iterator():
    if registro.personas.exists():
        casas_omitidas += 1
        continue

    nombre, apellido = nombre_aleatorio()

    Persona.objects.create(
        registro=registro,
        nombre=nombre,
        apellido=apellido,
        rut=rut_ficticio(),
        tipo_persona="SOCIO",
    )
    creadas["SOCIO"] += 1

    if random.random() < 0.65:
        nombre, apellido = nombre_aleatorio()

        Persona.objects.create(
            registro=registro,
            nombre=nombre,
            apellido=apellido,
            rut=rut_ficticio(),
            tipo_persona="REPRESENTANTE",
        )
        creadas["REPRESENTANTE"] += 1

    cantidad = random.choices(
        [0, 1, 2, 3],
        weights=[20, 40, 30, 10],
    )[0]

    for _ in range(cantidad):
        nombre, apellido = nombre_aleatorio()

        Persona.objects.create(
            registro=registro,
            nombre=nombre,
            apellido=apellido,
            rut=rut_ficticio(),
            tipo_persona="ADICIONAL",
        )
        creadas["ADICIONAL"] += 1

print("Personas creadas:", creadas)
print("Casas omitidas por tener personas:", casas_omitidas)
print("Total de personas:", Persona.objects.count())
