# Sistema de Registro de Alumnos - Academia

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema básico de registro de alumnos para una academia, desarrollado en Python como parte de la 1º evaluación. El sistema permite gestionar información de alumnos mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar) utilizando estructuras de datos nativas de Python.

## 🎯 Objetivos Cumplidos

- ✅ Almacenamiento de información de alumnos
- ✅ Búsqueda de alumnos por diferentes criterios (DNI y nombre)
- ✅ Visualización de todos los registros
- ✅ Validación de datos ingresados
- ✅ Eliminación de registros
- ✅ Estadísticas del sistema

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Estructuras de datos:** Listas y diccionarios
- **Paradigma:** Programación procedural con funciones

## 📁 Estructura del Código

### Componentes Principales

#### 1. Estructura de Datos

```python
alumnos = []  # Lista global que almacena todos los alumnos
```

Cada alumno se representa como un diccionario con la siguiente estructura:

```python
alumno = {
    'dni': str,        # DNI del alumno (formato: 12345678A)
    'nombre': str,     # Nombre completo
    'edad': int,       # Edad en años
    'curso': str,      # Curso en el que está matriculado
    'email': str,      # Email de contacto (opcional)
    'telefono': str    # Teléfono de contacto (opcional)
}
```

#### 2. Funciones Implementadas

##### Funciones de Interfaz
- **`mostrar_menu()`**: Muestra el menú principal con todas las opciones disponibles
- **`main()`**: Función principal que controla el flujo del programa

##### Funciones de Validación
- **`validar_dni(dni)`**: Valida el formato del DNI español (8 dígitos + 1 letra)
- **`validar_edad(edad)`**: Verifica que la edad sea un número válido entre 1 y 120
- **`dni_existe(dni)`**: Comprueba si un DNI ya está registrado en el sistema

##### Funciones de Gestión
- **`anadir_alumno()`**: Solicita datos y registra un nuevo alumno con validaciones
- **`mostrar_alumnos()`**: Lista todos los alumnos registrados con formato estructurado
- **`buscar_alumno_por_dni()`**: Busca un alumno específico por su DNI
- **`buscar_alumno_por_nombre()`**: Busca alumnos cuyo nombre contenga el texto ingresado
- **`eliminar_alumno()`**: Elimina un alumno del sistema tras confirmación
- **`mostrar_estadisticas()`**: Calcula y muestra estadísticas del sistema

## 🔄 Flujo de Ejecución

1. El programa inicia mostrando un mensaje de bienvenida
2. Presenta el menú principal con 7 opciones
3. El usuario selecciona una opción
4. Se ejecuta la función correspondiente
5. El sistema muestra los resultados
6. Espera confirmación del usuario para continuar
7. Vuelve al menú principal (excepto si se selecciona "Salir")

## 🎨 Características Destacadas

### Validación de Datos
- DNI con formato español estándar
- Edades dentro de rangos razonables
- Verificación de campos obligatorios
- Prevención de DNIs duplicados

### Búsqueda Flexible
- Búsqueda exacta por DNI
- Búsqueda parcial por nombre (insensible a mayúsculas)
- Múltiples resultados cuando corresponde

### Interfaz de Usuario
- Menú claro y estructurado
- Mensajes informativos con emojis
- Confirmación en operaciones críticas
- Separadores visuales para mejor legibilidad

### Estadísticas
- Total de alumnos registrados
- Edad promedio, mínima y máxima
- Curso más popular
- Distribución de alumnos por curso

## 💡 Conceptos de Python Aplicados

### Estructuras de Datos
- **Listas**: Para almacenar múltiples alumnos
- **Diccionarios**: Para representar cada alumno con sus atributos
- **Strings**: Para manipular y validar texto

### Control de Flujo
- **Bucles while**: Para el menú principal y validaciones
- **Bucles for**: Para iterar sobre alumnos
- **Condicionales if/elif/else**: Para decisiones y validaciones

### Funciones
- Modularización del código
- Reutilización de lógica
- Documentación con docstrings

### Manejo de Datos
- Validación de entrada del usuario
- Conversión de tipos de datos
- Búsqueda y filtrado de información

## 📊 Casos de Uso

### Caso 1: Registro de Nuevo Alumno
```
Usuario selecciona opción 1
→ Ingresa DNI: 12345678A
→ Ingresa nombre: Juan García López
→ Ingresa edad: 25
→ Ingresa curso: Python Avanzado
→ Ingresa email: juan@example.com
→ Ingresa teléfono: 600123456
✅ Alumno registrado correctamente
```

### Caso 2: Búsqueda por Nombre
```
Usuario selecciona opción 4
→ Ingresa: "juan"
✅ Muestra todos los alumnos con "juan" en su nombre
```

### Caso 3: Consulta de Estadísticas
```
Usuario selecciona opción 6
✅ Muestra:
   - Total de alumnos
   - Edad promedio
   - Curso más popular
   - Distribución por cursos
```

## 🔒 Seguridad y Validaciones

- **DNI único**: No permite registrar el mismo DNI dos veces
- **Formato DNI**: Valida 8 números + 1 letra
- **Edad válida**: Solo acepta números entre 1 y 120
- **Confirmación de eliminación**: Requiere confirmación antes de borrar
- **Longitud mínima**: Campos de texto con mínimo 3 caracteres

## 🚀 Instrucciones de Uso

### Requisitos
- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS

### Ejecución
```bash
python registro_alumnos.py
```

o en algunos sistemas:

```bash
python3 registro_alumnos.py
```

### Navegación
1. Ejecutar el programa
2. Leer el menú presentado
3. Ingresar el número de la opción deseada (1-7)
4. Seguir las instrucciones en pantalla
5. Presionar Enter para volver al menú

## 📝 Ejemplos de Datos de Prueba

Para probar el sistema, puedes usar estos datos de ejemplo:

**Alumno 1:**
- DNI: 12345678A
- Nombre: María González Pérez
- Edad: 22
- Curso: DAM 2º
- Email: maria@example.com
- Teléfono: 600111222

**Alumno 2:**
- DNI: 87654321B
- Nombre: Carlos Rodríguez Sánchez
- Edad: 20
- Curso: Python Avanzado
- Email: carlos@example.com
- Teléfono: 600333444

**Alumno 3:**
- DNI: 11223344C
- Nombre: Ana Martínez López
- Edad: 24
- Curso: DAM 2º
- Email: ana@example.com
- Teléfono: 600555666

## 🔍 Estándares de Código

El código sigue las convenciones de estilo PEP8:

- ✅ Nombres de funciones en snake_case
- ✅ Constantes en MAYÚSCULAS (si las hubiera)
- ✅ Docstrings en todas las funciones
- ✅ Líneas de máximo 100 caracteres (aproximadamente)
- ✅ Espaciado consistente
- ✅ Comentarios descriptivos

## 🎓 Conceptos Aprendidos

### Durante el Desarrollo
1. **Estructuras de datos en Python**: Uso efectivo de listas y diccionarios
2. **Validación de entrada**: Importancia de verificar datos del usuario
3. **Modularización**: Separación del código en funciones reutilizables
4. **Control de flujo**: Uso de bucles y condicionales para lógica compleja
5. **Experiencia de usuario**: Diseño de interfaces de texto claras e intuitivas
6. **Manejo de errores**: Prevención de errores mediante validaciones

### Aplicaciones Prácticas
- Gestión de bases de datos simples
- Validación de datos de usuarios
- Diseño de menús interactivos
- Organización de código en proyectos más grandes

## 🔮 Posibles Mejoras Futuras

### Funcionalidades
1. **Persistencia de datos**: Guardar alumnos en archivo JSON o CSV
2. **Edición de datos**: Permitir modificar información de alumnos existentes
3. **Exportación de reportes**: Generar informes en PDF o Excel
4. **Múltiples criterios de búsqueda**: Buscar por edad, curso, etc.
5. **Sistema de notas**: Añadir calificaciones a cada alumno
6. **Historial de cambios**: Registrar modificaciones realizadas

### Técnicas
1. **Base de datos**: Migrar a SQLite o MySQL
2. **Interfaz gráfica**: Implementar GUI con Tkinter o PyQt
3. **API REST**: Convertir en servicio web con Flask/FastAPI
4. **Testing**: Añadir pruebas unitarias con pytest
5. **Logging**: Implementar sistema de registro de eventos
6. **Autenticación**: Sistema de usuarios con diferentes permisos

### Optimizaciones
1. **Búsqueda indexada**: Mejorar rendimiento con diccionarios indexados
2. **Validación avanzada**: Regex para emails y teléfonos
3. **Configuración externa**: Archivo de configuración para parámetros
4. **Internacionalización**: Soporte para múltiples idiomas

## 📚 Referencias y Recursos

- [Documentación oficial de Python](https://docs.python.org/es/3/)
- [PEP 8 – Style Guide for Python Code](https://pep8.org/)
- [Real Python - Python Data Structures](https://realpython.com/python-data-structures/)
- [Python Tutorial - Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## 👨‍💻 Autor

**Entornito**  
Alumno de 2º DAM  
Proyecto 1º Evaluación - Python  
Noviembre 2025

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.
