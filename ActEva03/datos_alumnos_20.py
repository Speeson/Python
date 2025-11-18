"""
Lista de 20 alumnos de prueba para el Sistema de Registro
Datos realistas y variados para testing y demostraciones

Puedes copiar esta lista directamente en tu programa
"""

alumnos = [
    {
        'dni': '12345678A',
        'nombre': 'María González Pérez',
        'edad': 22,
        'curso': 'DAM 2º',
        'email': 'maria.gonzalez@example.com',
        'telefono': '600111222'
    },
    {
        'dni': '87654321B',
        'nombre': 'Carlos Rodríguez Sánchez',
        'edad': 20,
        'curso': 'Python Avanzado',
        'email': 'carlos.rodriguez@example.com',
        'telefono': '600333444'
    },
    {
        'dni': '11223344C',
        'nombre': 'Ana Martínez López',
        'edad': 24,
        'curso': 'DAM 2º',
        'email': 'ana.martinez@example.com',
        'telefono': '600555666'
    },
    {
        'dni': '99887766D',
        'nombre': 'Juan Pérez García',
        'edad': 19,
        'curso': 'Python Avanzado',
        'email': 'juan.perez@example.com',
        'telefono': '600777888'
    },
    {
        'dni': '55566677E',
        'nombre': 'Laura Fernández Ruiz',
        'edad': 23,
        'curso': 'DAW 2º',
        'email': 'laura.fernandez@example.com',
        'telefono': '611223344'
    },
    {
        'dni': '44455566F',
        'nombre': 'David López Moreno',
        'edad': 21,
        'curso': 'DAM 2º',
        'email': 'david.lopez@example.com',
        'telefono': '622334455'
    },
    {
        'dni': '33344455G',
        'nombre': 'Carmen Sánchez Díaz',
        'edad': 25,
        'curso': 'Python Avanzado',
        'email': 'carmen.sanchez@example.com',
        'telefono': '633445566'
    },
    {
        'dni': '22233344H',
        'nombre': 'Miguel Ángel Torres Vega',
        'edad': 20,
        'curso': 'DAW 2º',
        'email': 'miguel.torres@example.com',
        'telefono': '644556677'
    },
    {
        'dni': '66677788I',
        'nombre': 'Isabel Ramírez Castro',
        'edad': 22,
        'curso': 'DAM 1º',
        'email': 'isabel.ramirez@example.com',
        'telefono': '655667788'
    },
    {
        'dni': '77788899J',
        'nombre': 'Javier Morales Ortiz',
        'edad': 26,
        'curso': 'Python Avanzado',
        'email': 'javier.morales@example.com',
        'telefono': '666778899'
    },
    {
        'dni': '88899900K',
        'nombre': 'Lucía Romero Navarro',
        'edad': 19,
        'curso': 'DAM 1º',
        'email': 'lucia.romero@example.com',
        'telefono': '677889900'
    },
    {
        'dni': '99900011L',
        'nombre': 'Pablo Jiménez Serrano',
        'edad': 23,
        'curso': 'DAW 2º',
        'email': 'pablo.jimenez@example.com',
        'telefono': '688990011'
    },
    {
        'dni': '00011122M',
        'nombre': 'Elena Gutiérrez Molina',
        'edad': 21,
        'curso': 'DAM 2º',
        'email': 'elena.gutierrez@example.com',
        'telefono': '699001122'
    },
    {
        'dni': '11122233N',
        'nombre': 'Sergio Castro Herrera',
        'edad': 24,
        'curso': 'Python Avanzado',
        'email': 'sergio.castro@example.com',
        'telefono': '600112233'
    },
    {
        'dni': '22233344O',
        'nombre': 'Marta Vargas Iglesias',
        'edad': 20,
        'curso': 'DAM 1º',
        'email': 'marta.vargas@example.com',
        'telefono': '611223344'
    },
    {
        'dni': '33344455P',
        'nombre': 'Adrián Rubio Pascual',
        'edad': 22,
        'curso': 'DAW 2º',
        'email': 'adrian.rubio@example.com',
        'telefono': '622334455'
    },
    {
        'dni': '44455566Q',
        'nombre': 'Cristina Delgado Marín',
        'edad': 25,
        'curso': 'Python Avanzado',
        'email': 'cristina.delgado@example.com',
        'telefono': '633445566'
    },
    {
        'dni': '55566677R',
        'nombre': 'Raúl Núñez Campos',
        'edad': 19,
        'curso': 'DAM 1º',
        'email': 'raul.nunez@example.com',
        'telefono': '644556677'
    },
    {
        'dni': '66677788S',
        'nombre': 'Beatriz Santana Gil',
        'edad': 23,
        'curso': 'DAM 2º',
        'email': 'beatriz.santana@example.com',
        'telefono': '655667788'
    },
    {
        'dni': '77788899T',
        'nombre': 'Daniel Medina Cortés',
        'edad': 21,
        'curso': 'DAW 2º',
        'email': 'daniel.medina@example.com',
        'telefono': '666778899'
    }
]

# Información sobre los datos
print("="*70)
print("DATOS DE 20 ALUMNOS GENERADOS")
print("="*70)
print(f"\nTotal de alumnos: {len(alumnos)}")
print("\nDistribución por curso:")

# Contar alumnos por curso
cursos = {}
for alumno in alumnos:
    curso = alumno['curso']
    if curso in cursos:
        cursos[curso] += 1
    else:
        cursos[curso] = 1

for curso, cantidad in sorted(cursos.items()):
    print(f"  • {curso}: {cantidad} alumno(s)")

# Estadísticas de edad
edades = [alumno['edad'] for alumno in alumnos]
print(f"\nEdad promedio: {sum(edades) / len(edades):.1f} años")
print(f"Edad mínima: {min(edades)} años")
print(f"Edad máxima: {max(edades)} años")

print("\n" + "="*70)
print("Puedes copiar la lista 'alumnos' directamente en tu programa")
print("="*70)
