# Guía para Capturas de Pantalla del Sistema

## 📸 Capturas Requeridas para el Informe

Para completar el proyecto, necesitas incluir capturas de pantalla que demuestren el funcionamiento del programa. Aquí te indico qué capturas tomar y cómo hacerlo.

## 🎯 Capturas Necesarias

### 1. Menú Principal
**Qué capturar**: La pantalla inicial con el mensaje de bienvenida y el menú completo.

**Cómo hacerlo**:
```bash
python registro_alumnos.py
```
Capturar cuando aparezca el menú con las 7 opciones.

---

### 2. Añadir Alumno - Proceso Completo
**Qué capturar**: Todo el proceso de añadir un alumno nuevo, desde la solicitud de datos hasta la confirmación.

**Pasos**:
1. Seleccionar opción `1`
2. Ingresar DNI: `12345678A`
3. Ingresar nombre: `María González Pérez`
4. Ingresar edad: `22`
5. Ingresar curso: `DAM 2º`
6. Ingresar email: `maria@example.com`
7. Ingresar teléfono: `600111222`
8. Capturar el mensaje de confirmación ✅

**Captura alternativa**: También puedes capturar el proceso con validación de error.

**Ejemplo de error a mostrar**:
1. Seleccionar opción `1`
2. Ingresar DNI: `123` (DNI incorrecto)
3. Capturar el mensaje de error ❌

---

### 3. Mostrar Todos los Alumnos
**Qué capturar**: La lista completa de alumnos registrados con todos sus datos.

**Pasos**:
1. Añadir al menos 3 alumnos primero
2. Seleccionar opción `2`
3. Capturar la lista completa con todos los alumnos

---

### 4. Buscar Alumno por DNI - Éxito
**Qué capturar**: Una búsqueda exitosa que muestre los datos del alumno encontrado.

**Pasos**:
1. Seleccionar opción `3`
2. Ingresar un DNI existente: `12345678A`
3. Capturar el resultado con los datos del alumno

---

### 5. Buscar Alumno por Nombre
**Qué capturar**: Una búsqueda por nombre que encuentre coincidencias.

**Pasos**:
1. Seleccionar opción `4`
2. Ingresar: `maría` o `María`
3. Capturar los resultados encontrados

**Captura adicional (opcional)**: Búsqueda que no encuentra resultados.

---

### 6. Estadísticas del Sistema
**Qué capturar**: Las estadísticas calculadas con varios alumnos registrados.

**Pasos**:
1. Asegurarte de tener al menos 3-4 alumnos registrados
2. Seleccionar opción `6`
3. Capturar las estadísticas completas:
   - Total de alumnos
   - Edad promedio
   - Edad mínima y máxima
   - Curso más popular
   - Distribución por cursos

---

### 7. Eliminar Alumno (Opcional pero recomendado)
**Qué capturar**: El proceso de eliminación con confirmación.

**Pasos**:
1. Seleccionar opción `5`
2. Ingresar DNI de un alumno existente
3. Capturar la solicitud de confirmación
4. Ingresar `S` para confirmar
5. Capturar el mensaje de confirmación de eliminación

---

### 8. Validaciones de Error (Muy Recomendado)
**Qué capturar**: Ejemplos de validaciones funcionando.

**Ejemplos a mostrar**:

**Error DNI duplicado**:
1. Añadir un alumno con DNI `12345678A`
2. Intentar añadir otro alumno con el mismo DNI
3. Capturar el mensaje de error

**Error DNI formato incorrecto**:
1. Intentar añadir alumno con DNI `123`
2. Capturar el mensaje de error

**Error edad inválida**:
1. Intentar ingresar edad `-5` o `200`
2. Capturar el mensaje de error

---

## 🖼️ Cómo Tomar las Capturas

### En Windows
- **Captura de pantalla completa**: `Win + Impr Pant` o `Win + Shift + S`
- **Herramienta de recorte**: Buscar "Recorte" en el menú inicio
- **Alternativa**: Usar `Alt + Impr Pant` para capturar solo la ventana activa

### En Linux
- **Gnome**: `Shift + Impr Pant` o `PrintScreen`
- **KDE**: `Shift + Impr Pant` o usar Spectacle
- **Terminal específico**: Usar la función de captura de tu terminal

### En macOS
- **Captura de área**: `Cmd + Shift + 4`
- **Captura de ventana**: `Cmd + Shift + 4` luego `Espacio`
- **Captura completa**: `Cmd + Shift + 3`

---

## 📋 Organización de las Capturas

Guarda todas las capturas con nombres descriptivos:

```
captura_01_menu_principal.png
captura_02_añadir_alumno.png
captura_03_añadir_alumno_confirmacion.png
captura_04_error_dni_duplicado.png
captura_05_mostrar_todos_alumnos.png
captura_06_buscar_dni.png
captura_07_buscar_nombre.png
captura_08_estadisticas.png
captura_09_eliminar_alumno.png
```

---

## 💡 Consejos para Buenas Capturas

1. **Limpieza**: Asegúrate de que la terminal esté limpia y sin información innecesaria
2. **Legibilidad**: Usa un tamaño de fuente adecuado en tu terminal
3. **Contexto**: Cada captura debe mostrar suficiente contexto para entender qué se está haciendo
4. **Calidad**: Evita capturas borrosas o con reflejos
5. **Consistencia**: Usa el mismo tema/configuración de terminal en todas las capturas
6. **Recorte**: Recorta las capturas para mostrar solo lo relevante

---

## 📊 Datos de Prueba Recomendados

Para tener un conjunto completo de datos para las capturas, usa estos alumnos:

**Alumno 1**:
- DNI: `12345678A`
- Nombre: `María González Pérez`
- Edad: `22`
- Curso: `DAM 2º`
- Email: `maria@example.com`
- Teléfono: `600111222`

**Alumno 2**:
- DNI: `87654321B`
- Nombre: `Carlos Rodríguez Sánchez`
- Edad: `20`
- Curso: `Python Avanzado`
- Email: `carlos@example.com`
- Teléfono: `600333444`

**Alumno 3**:
- DNI: `11223344C`
- Nombre: `Ana Martínez López`
- Edad: `24`
- Curso: `DAM 2º`
- Email: `ana@example.com`
- Teléfono: `600555666`

**Alumno 4**:
- DNI: `99887766D`
- Nombre: `Juan Pérez García`
- Edad: `19`
- Curso: `Python Avanzado`
- Email: `juan@example.com`
- Teléfono: `600777888`

---

## 📝 Inserción en el Informe

Una vez tengas las capturas, incorpóralas en tu documento de la siguiente manera:

### En Word/LibreOffice
1. Insertar → Imagen
2. Seleccionar la captura
3. Ajustar el tamaño (recomendado: 15-18 cm de ancho)
4. Añadir pie de imagen descriptivo

### En Markdown
```markdown
![Descripción de la captura](ruta/a/la/captura.png)
*Figura X: Descripción detallada de lo que muestra la captura*
```

### Ejemplo de Pie de Imagen
```
Figura 1: Menú principal del sistema mostrando las 7 opciones disponibles
Figura 2: Proceso de registro de un nuevo alumno con validación de datos
Figura 3: Listado completo de alumnos registrados con toda su información
Figura 4: Búsqueda exitosa de alumno por DNI mostrando coincidencia
Figura 5: Estadísticas del sistema con edad promedio y distribución por cursos
```

---

## ✅ Checklist de Capturas

Marca las capturas que ya tienes:

- [ ] Menú principal
- [ ] Añadir alumno (proceso completo)
- [ ] Añadir alumno (error de validación)
- [ ] Mostrar todos los alumnos (lista completa)
- [ ] Buscar alumno por DNI (encontrado)
- [ ] Buscar alumno por nombre (encontrado)
- [ ] Estadísticas del sistema
- [ ] Eliminar alumno (con confirmación)
- [ ] Error DNI duplicado
- [ ] Búsqueda sin resultados (opcional)

---

## 🎨 Mejoras Visuales Opcionales

Si quieres que tus capturas se vean más profesionales:

1. **Terminal con tema oscuro**: Muchos consideran más profesional
2. **Fuente monoespaciada**: Courier, Consolas, Fira Code
3. **Tamaño de fuente**: 12-14pt para buena legibilidad
4. **Resaltar con flechas/cajas**: En un editor de imágenes después

---

¡Con estas capturas tendrás un informe completo y profesional que cumple con todos los requisitos de la rúbrica!
