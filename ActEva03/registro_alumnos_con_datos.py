"""
Sistema de Registro de Alumnos - Academia (CON DATOS DE PRUEBA)
Versión para capturas de pantalla

Esta versión viene con datos de prueba pre-cargados para facilitar
la demostración del sistema y la toma de capturas de pantalla.

Autor: Entornito
Fecha: Noviembre 2025
"""

# Lista global para almacenar los alumnos (con datos de prueba pre-cargados)
alumnos = [
    {
        'dni': '12345678A',
        'nombre': 'María González Pérez',
        'edad': 22,
        'curso': 'DAM 2º',
        'email': 'maria@example.com',
        'telefono': '600111222'
    },
    {
        'dni': '87654321B',
        'nombre': 'Carlos Rodríguez Sánchez',
        'edad': 20,
        'curso': 'Python Avanzado',
        'email': 'carlos@example.com',
        'telefono': '600333444'
    },
    {
        'dni': '11223344C',
        'nombre': 'Ana Martínez López',
        'edad': 24,
        'curso': 'DAM 2º',
        'email': 'ana@example.com',
        'telefono': '600555666'
    },
    {
        'dni': '99887766D',
        'nombre': 'Juan Pérez García',
        'edad': 19,
        'curso': 'Python Avanzado',
        'email': 'juan@example.com',
        'telefono': '600777888'
    }
]


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    
    Returns:
        None
    """
    print("\n" + "="*50)
    print("   SISTEMA DE REGISTRO DE ALUMNOS - ACADEMIA")
    print("="*50)
    print("1. Añadir nuevo alumno")
    print("2. Mostrar todos los alumnos")
    print("3. Buscar alumno por DNI")
    print("4. Buscar alumno por nombre")
    print("5. Eliminar alumno")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    print("="*50)


def validar_dni(dni):
    """
    Valida el formato básico de un DNI español.
    
    Args:
        dni (str): DNI a validar
        
    Returns:
        bool: True si el DNI tiene formato válido, False en caso contrario
    """
    dni = dni.strip().upper()
    
    if len(dni) != 9:
        return False
    
    if not dni[:8].isdigit():
        return False
    
    if not dni[8].isalpha():
        return False
    
    return True


def validar_edad(edad):
    """
    Valida que la edad sea un número positivo razonable.
    
    Args:
        edad (str): Edad a validar
        
    Returns:
        bool: True si la edad es válida, False en caso contrario
    """
    try:
        edad_int = int(edad)
        return 1 <= edad_int <= 120
    except ValueError:
        return False


def dni_existe(dni):
    """
    Verifica si un DNI ya está registrado en el sistema.
    
    Args:
        dni (str): DNI a verificar
        
    Returns:
        bool: True si el DNI existe, False en caso contrario
    """
    dni = dni.strip().upper()
    for alumno in alumnos:
        if alumno['dni'] == dni:
            return True
    return False


def anadir_alumno():
    """
    Solicita los datos de un nuevo alumno y lo añade a la lista.
    Valida los datos ingresados antes de añadirlos.
    
    Returns:
        None
    """
    print("\n--- AÑADIR NUEVO ALUMNO ---")
    
    while True:
        dni = input("DNI (formato: 12345678A): ").strip().upper()
        
        if not validar_dni(dni):
            print("❌ Error: El DNI debe tener 8 números seguidos de una letra.")
            continue
        
        if dni_existe(dni):
            print("❌ Error: Este DNI ya está registrado en el sistema.")
            return
        
        break
    
    while True:
        nombre = input("Nombre completo: ").strip()
        if len(nombre) >= 3:
            break
        print("❌ Error: El nombre debe tener al menos 3 caracteres.")
    
    while True:
        edad = input("Edad: ").strip()
        if validar_edad(edad):
            edad = int(edad)
            break
        print("❌ Error: La edad debe ser un número entre 1 y 120.")
    
    while True:
        curso = input("Curso (ej: Python Avanzado, DAM, etc.): ").strip()
        if len(curso) >= 3:
            break
        print("❌ Error: El curso debe tener al menos 3 caracteres.")
    
    email = input("Email (opcional, presiona Enter para omitir): ").strip()
    telefono = input("Teléfono (opcional, presiona Enter para omitir): ").strip()
    
    alumno = {
        'dni': dni,
        'nombre': nombre,
        'edad': edad,
        'curso': curso,
        'email': email if email else "No especificado",
        'telefono': telefono if telefono else "No especificado"
    }
    
    alumnos.append(alumno)
    print(f"\n✅ Alumno {nombre} registrado correctamente con DNI {dni}.")


def mostrar_alumnos():
    """
    Muestra todos los alumnos registrados en el sistema.
    Si no hay alumnos, muestra un mensaje informativo.
    
    Returns:
        None
    """
    print("\n--- LISTADO DE ALUMNOS ---")
    
    if not alumnos:
        print("⚠️  No hay alumnos registrados en el sistema.")
        return
    
    print(f"\nTotal de alumnos registrados: {len(alumnos)}\n")
    
    for i, alumno in enumerate(alumnos, 1):
        print(f"{'─'*50}")
        print(f"Alumno #{i}")
        print(f"{'─'*50}")
        print(f"DNI:      {alumno['dni']}")
        print(f"Nombre:   {alumno['nombre']}")
        print(f"Edad:     {alumno['edad']} años")
        print(f"Curso:    {alumno['curso']}")
        print(f"Email:    {alumno['email']}")
        print(f"Teléfono: {alumno['telefono']}")
        print()


def buscar_alumno_por_dni():
    """
    Busca y muestra la información de un alumno por su DNI.
    
    Returns:
        None
    """
    print("\n--- BUSCAR ALUMNO POR DNI ---")
    
    if not alumnos:
        print("⚠️  No hay alumnos registrados en el sistema.")
        return
    
    dni = input("Introduce el DNI a buscar: ").strip().upper()
    
    encontrado = False
    for alumno in alumnos:
        if alumno['dni'] == dni:
            print(f"\n{'─'*50}")
            print("✅ ALUMNO ENCONTRADO")
            print(f"{'─'*50}")
            print(f"DNI:      {alumno['dni']}")
            print(f"Nombre:   {alumno['nombre']}")
            print(f"Edad:     {alumno['edad']} años")
            print(f"Curso:    {alumno['curso']}")
            print(f"Email:    {alumno['email']}")
            print(f"Teléfono: {alumno['telefono']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"❌ No se encontró ningún alumno con el DNI {dni}.")


def buscar_alumno_por_nombre():
    """
    Busca y muestra alumnos cuyo nombre contenga el texto ingresado.
    La búsqueda no es sensible a mayúsculas/minúsculas.
    
    Returns:
        None
    """
    print("\n--- BUSCAR ALUMNO POR NOMBRE ---")
    
    if not alumnos:
        print("⚠️  No hay alumnos registrados en el sistema.")
        return
    
    nombre_buscar = input("Introduce el nombre (o parte del nombre) a buscar: ").strip().lower()
    
    resultados = []
    for alumno in alumnos:
        if nombre_buscar in alumno['nombre'].lower():
            resultados.append(alumno)
    
    if resultados:
        print(f"\n✅ Se encontraron {len(resultados)} resultado(s):\n")
        for i, alumno in enumerate(resultados, 1):
            print(f"{'─'*50}")
            print(f"Resultado #{i}")
            print(f"{'─'*50}")
            print(f"DNI:      {alumno['dni']}")
            print(f"Nombre:   {alumno['nombre']}")
            print(f"Edad:     {alumno['edad']} años")
            print(f"Curso:    {alumno['curso']}")
            print(f"Email:    {alumno['email']}")
            print(f"Teléfono: {alumno['telefono']}")
            print()
    else:
        print(f"❌ No se encontraron alumnos con '{nombre_buscar}' en su nombre.")


def eliminar_alumno():
    """
    Elimina un alumno del sistema buscándolo por su DNI.
    Solicita confirmación antes de eliminar.
    
    Returns:
        None
    """
    print("\n--- ELIMINAR ALUMNO ---")
    
    if not alumnos:
        print("⚠️  No hay alumnos registrados en el sistema.")
        return
    
    dni = input("Introduce el DNI del alumno a eliminar: ").strip().upper()
    
    for i, alumno in enumerate(alumnos):
        if alumno['dni'] == dni:
            print(f"\nAlumno encontrado:")
            print(f"Nombre: {alumno['nombre']}")
            print(f"DNI:    {alumno['dni']}")
            print(f"Curso:  {alumno['curso']}")
            
            confirmacion = input("\n¿Estás seguro de eliminar este alumno? (S/N): ").strip().upper()
            
            if confirmacion == 'S':
                alumnos.pop(i)
                print(f"✅ Alumno {alumno['nombre']} eliminado correctamente.")
            else:
                print("❌ Operación cancelada.")
            return
    
    print(f"❌ No se encontró ningún alumno con el DNI {dni}.")


def mostrar_estadisticas():
    """
    Muestra estadísticas generales sobre los alumnos registrados.
    Incluye: total de alumnos, edad promedio, curso más popular.
    
    Returns:
        None
    """
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    
    if not alumnos:
        print("⚠️  No hay alumnos registrados para mostrar estadísticas.")
        return
    
    total_alumnos = len(alumnos)
    
    suma_edades = sum(alumno['edad'] for alumno in alumnos)
    edad_promedio = suma_edades / total_alumnos
    
    edad_minima = min(alumno['edad'] for alumno in alumnos)
    edad_maxima = max(alumno['edad'] for alumno in alumnos)
    
    cursos = {}
    for alumno in alumnos:
        curso = alumno['curso']
        if curso in cursos:
            cursos[curso] += 1
        else:
            cursos[curso] = 1
    
    curso_popular = max(cursos, key=cursos.get)
    
    print(f"\n{'─'*50}")
    print(f"Total de alumnos registrados:  {total_alumnos}")
    print(f"Edad promedio:                 {edad_promedio:.1f} años")
    print(f"Edad mínima:                   {edad_minima} años")
    print(f"Edad máxima:                   {edad_maxima} años")
    print(f"Curso más popular:             {curso_popular} ({cursos[curso_popular]} alumno(s))")
    print(f"{'─'*50}")
    
    print(f"\nDistribución por cursos:")
    for curso, cantidad in cursos.items():
        print(f"  • {curso}: {cantidad} alumno(s)")


def main():
    """
    Función principal que ejecuta el bucle del menú del sistema.
    Gestiona la navegación entre las diferentes opciones.
    
    Returns:
        None
    """
    print("\n¡Bienvenido al Sistema de Registro de Alumnos!")
    print("⚠️  NOTA: Esta versión incluye datos de prueba pre-cargados")
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-7): ").strip()
        
        if opcion == '1':
            anadir_alumno()
        elif opcion == '2':
            mostrar_alumnos()
        elif opcion == '3':
            buscar_alumno_por_dni()
        elif opcion == '4':
            buscar_alumno_por_nombre()
        elif opcion == '5':
            eliminar_alumno()
        elif opcion == '6':
            mostrar_estadisticas()
        elif opcion == '7':
            print("\n¡Gracias por usar el sistema! Hasta pronto. 👋")
            break
        else:
            print("\n❌ Opción no válida. Por favor, selecciona una opción del 1 al 7.")
        
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()
