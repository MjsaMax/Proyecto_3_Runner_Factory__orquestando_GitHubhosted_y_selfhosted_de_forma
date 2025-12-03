
Historia 1: Configuración Inicial del Repositorio y Entorno

ID: #1 ID_PULL_REQUEST: #6

Descripción:

Inicializar el repositorio con la estructura básica de carpetas y dependencias necesarias para Python/FastAPI.

Tareas:

Crear repositorio en GitHub con rama main.
Crear estructura de carpetas: app/, tests/ y .evidence/ (esta última es obligatoria para el curso).
Crear archivo .gitignore para Python.
Crear requirements.txt o pyproject.toml incluyendo fastapi, uvicorn, pytest, ruff (o flake8).

Criterios de Aceptación:

    El repo existe y tiene las carpetas creadas.
    La carpeta .evidence/ existe (aunque esté vacía, debe existir un .gitkeep).

EVIDENCIA: [COMMIT](https://github.com/MjsaMax/Proyecto_3_Runner_Factory__orquestando_GitHubhosted_y_selfhosted_de_forma/commit/bbaf1f529ddbd422b6cf512770268c03c5023001)

Responsable(s): Serrano Max


Historia 3: Pruebas Unitarias (Unit Tests)

ID: #3 ID_PULL_REQUEST: #8

Descripción:

Crear tests automatizados para asegurar que la API responde correctamente.

Tareas:

Configurar pytest.
Escribir un test para verificar que /health devuelve 200 OK.
Escribir tests básicos para /docs y /docs/{id}.

Criterios de Aceptación:

    Al ejecutar pytest, todos los tests pasan en verde.

Responsable(s): Serrano Max

EVIDENCIA: test_main.log

```bash
==================================================== test session starts =====================================================
platform linux -- Python 3.12.3, pytest-9.0.1, pluggy-1.6.0
rootdir: /mnt/c/Users/Max--/Documents/projects/repos/Proyecto_3_Runner_Factory__orquestando_GitHubhosted_y_selfhosted_de_forma
plugins: anyio-4.12.0
collected 4 items

tests/test_main.py ....                                                                                                [100%]

===================================================== 4 passed in 4.96s ======================================================
```
