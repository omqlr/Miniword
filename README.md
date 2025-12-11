# Miniword

Editor de texto sencillo hecho con PySide6. Incluye menús, barra de herramientas y un panel acoplable para buscar y reemplazar texto, junto con utilidades de personalización básica.

## Requisitos
- Python 3.10+ (probado con la versión incluida en `venv`)
- Dependencias: `PySide6`

1) Instalar dependencias:
```bash
pip install PySide6
```
3) Ejecutar la app:
```bash
python miniword.py
```

## Funcionalidades principales
- Crear, abrir y guardar `.txt` con atajos estándar (`Ctrl+N`, `Ctrl+O`, `Ctrl+S`); guardado automático cada 50 s sobre la ruta actual.
- Deshacer/rehacer y edición básica (cortar, copiar, pegar).
- Búsqueda y reemplazo vía menús y panel acoplable en el lateral derecho (siguiente, anterior y recuento de coincidencias).
- Personalización: selector de color de fondo y diálogo de fuente.
- Contador de palabras en la barra de estado.
- Barra de herramientas con los comandos principales y accesos rápidos.

## Estructura del repositorio
- `miniword.py`: implementación del editor de texto.

## Notas
- Los diálogos de archivos usan rutas relativas; evita rutas absolutas para portabilidad.
- Si usas otra versión de Python, reinstala el entorno virtual antes de ejecutar.
